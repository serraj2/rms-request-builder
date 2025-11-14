import tkinter as tk
from tkinter import ttk
import requests
import sys
import time
import json
import random
from datetime import datetime
from config import (
    NAVIGATION_ENDPOINTS,
    MARKET_ENDPOINTS,
    REFRESH_ENDPOINT,
    REFRESH_HEADERS,
    NAVIGATION_HEADERS,
    NAVIGATION_PAYLOAD,
    BET_TYPE_MAP
)

def fetch_market_ids_from_navigation(env):
    nav_endpoint = NAVIGATION_ENDPOINTS[env]
    try:
        response = requests.post(nav_endpoint, headers=NAVIGATION_HEADERS, json=NAVIGATION_PAYLOAD)
        response.raise_for_status()
        data = response.json()
        return [str(item.get("sportsbookMarketId")) for item in data.get("results", []) if item.get("sportsbookMarketId")]
    except Exception as e:
        print(f"❌ Failed to fetch market IDs: {e}")
        return []

def fetch_market_data(market_id, env):
    market_url = MARKET_ENDPOINTS[env]
    try:
        response = requests.get(market_url.format(market_id))
        response.raise_for_status()
        return response.json()
    except:
        return []

def parse_fractional_odds(odds_str):
    try:
        return odds_str.split('/')
    except:
        return None, None

def parse_iso_datetime_to_epoch(iso_str):
    try:
        return int(datetime.fromisoformat(iso_str.replace("Z", "+00:00")).timestamp() * 1000)
    except:
        return None

def collect_all_selections(market_ids, env):
    collected_event_ids = set()
    selections = []
    for market_id in market_ids:
        data = fetch_market_data(market_id, env)
        if not data or not isinstance(data, list):
            continue

        entry = data[0]
        market_def = entry.get("marketDefinition", {})
        market_info = market_def.get("market", {})
        event_info = market_def.get("event", {})
        event_id_ramp = event_info.get("id", {}).get("rampId")
        if event_id_ramp:
            collected_event_ids.add(str(event_id_ramp))
        sport_variant = event_info.get("sportVariant", {}).get("id", {})
        sport_info = event_info.get("sportInfo", {}).get("id", {})
        prices = entry.get("prices", [])
        inplay = market_info.get("inplay", False)
        event_start = parse_iso_datetime_to_epoch(event_info.get("startTime", ""))

        for runner in market_def.get("runners", []):
            identifier_id = runner.get("id", {}).get("identifierId")
            selection_id = runner.get("id", {}).get("rampId")
            name = runner.get("name")
            price = next((p for p in prices if str(p.get("id", {}).get("identifierId")) == str(identifier_id)), {})
            num, denom = parse_fractional_odds(price.get("winFractionalOdds", "0/1"))
            odds = price.get("winDecimalOdds", 1.0)

            selections.append({
                "runnerId": {"marketId": market_id, "selectionId": selection_id},
                "selectionName": name,
                "selectionPrice": {"numerator": num, "denominator": denom},
                "isInplay": inplay,
                "eventStartTime": event_start,
                "linkedExchangeMarketId": None,
                "marketType": market_info.get("type", {}).get("name"),
                "marketTypeId": str(market_info.get("type", {}).get("id", {}).get("supplierId")),
                "sportVariantId": str(sport_variant.get("rampId")),
                "eventTypeId": str(event_info.get("id", {}).get("rampId")),
                "eventId": str(event_info.get("id", {}).get("rampId")) if event_info.get("id", {}).get("rampId") else "" ,
                "marketFeedsId": market_info.get("id", {}).get("rampId"),
                "marketRampId": market_info.get("id", {}).get("rampId"),
                "selectionRampId": selection_id,
                "betOdds": odds
            })
    return selections

def build_request(account_id, count, env):
    market_ids = fetch_market_ids_from_navigation(env)
    all_sel = collect_all_selections(market_ids, env)
    if len(all_sel) < count:
        raise ValueError(f"Only {len(all_sel)} unique selections available, but {count} requested.")
    chosen = random.sample(all_sel, count)
    total_odds = 1.0
    contexts = []
    for sel in chosen:
        total_odds *= sel["betOdds"]
        context = sel.copy()
        context.pop("betOdds", None)
        contexts.append(context)

    refresh_ids = list(set(sel.get("eventId") for sel in chosen if sel.get("eventId") and sel.get("eventId").isdigit()))
    def build_refresh_payload(event_ids):
        return [
            {"destinationId": "betfair_us", "eventId": int(eid)}
            for eid in event_ids if eid.isdigit()
        ]

    def send_refresh_request(payload):
        try:
            response = requests.post(
                REFRESH_ENDPOINT,
                headers=REFRESH_HEADERS,
                json=payload
            )
            print("Refresh request status:", response.status_code)
        except Exception as e:
            print("Error sending refresh request:", e)

    refresh_payload = build_refresh_payload(refresh_ids)
    print("Sending refresh for event IDs:", refresh_ids)
    send_refresh_request(refresh_payload)

    return {
        "timestamp": int(time.time()),
        "userContext": {
            "accountId": account_id,
            "countryOfResidence": "USA",
            "physicalLocation": "US",
            "currency": "USD",
            "channel": "INTERNET"
        },
        "betContexts": [{
            "betNo": 1,
            "betType": BET_TYPE_MAP[count],
            "numLines": 1,
            "stakePerLine": 10,
            "betOdds": round(total_odds, 2),
            "selectionContexts": contexts
        }]
    }

def launch_gui():
    def on_generate():
        output.delete("1.0", tk.END)
        feedback_label.config(text="")
        try:
            sel = int(selection_var.get())
            acc = int(account_var.get())
            if not (1 <= sel <= 25):
                feedback_label.config(text="Selections must be between 1 and 25.")
                return
            if acc <= 0:
                feedback_label.config(text="User ID must be a positive integer.")
                return
            result = build_request(acc, sel, env_var.get())
            if "error" in result:
                feedback_label.config(text=result["error"])
                return
            output.insert(tk.END, json.dumps(result, indent=2))
        except ValueError as ve:
            feedback_label.config(text=str(ve))
        except Exception as e:
            output.insert(tk.END, f"Error: {e}")
        except Exception as e:
            output.delete("1.0", tk.END)
            output.insert(tk.END, f"Error: {e}")

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(output.get("1.0", tk.END).strip())
        root.update()

    root = tk.Tk()
    root.resizable(True, True)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.resizable(True, True)  # Allow the window to be resized
    root.title("RMS REQUEST BUILDER")

    tk.Label(root, text="NUMBER OF SELECTIONS").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    selection_var = tk.StringVar(value="1")
    tk.Entry(root, textvariable=selection_var, validate='key', validatecommand=(root.register(lambda P: len(P) <= 2), '%P')).grid(row=0, column=1, padx=5, pady=5, sticky="w")

    tk.Label(root, text="USER ID").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    account_var = tk.StringVar()
    tk.Entry(root, textvariable=account_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(root, text="ENVIRONMENT").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    env_var = tk.StringVar(value="nxtbs1")
    tk.OptionMenu(root, env_var, "nxtbs1", "intbs1").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    ttk.Button(root, text="GENERATE", command=on_generate).grid(row=3, column=0, columnspan=2, pady=5)

    # Add scrollbars
    scrollbar_y = tk.Scrollbar(root, orient="vertical")

    output = tk.Text(root, height=20, width=80, wrap="none", yscrollcommand=scrollbar_y.set, )
    output.grid(row=4, column=0, columnspan=2, sticky="nsew")
    scrollbar_y.grid(row=4, column=2, sticky="ns")
    scrollbar_y.config(command=output.yview)

    # Allow dynamic resizing of text box
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    ttk.Button(root, text="COPY", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=5)

    feedback_label = tk.Label(root, text="", fg="red")
    feedback_label.grid(row=6, column=0, columnspan=2, pady=(0,10))

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
