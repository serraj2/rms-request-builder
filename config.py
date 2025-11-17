# config.py
import os
# === Endpoint Templates ===
NAVIGATION_ENDPOINTS = {
    "nxtbs1": (
        "http://xtt-nxt.nxt.betfair/tunnel_facet_builder/betfair.com/"
        "use1-scanfd-nxtbs1.dev.fndlsb.net/www/sports/navigation/facet/v1/search?alt=json"
    ),
    "intbs1": (
        "http://xtt-nxt.nxt.betfair/tunnel_facet_builder/betfair.com/"
        "use1-scanfd-intbs1.dev.fndlsb.net/www/sports/navigation/facet/v1/search?alt=json"
    )
}

MARKET_ENDPOINTS = {
    "nxtbs1": "http://use1-mwtfd01-nxtbs1.dev.fndlsb.net:8080/market/{}",
    "intbs1": "http://use1-mwtfd01-intbs1.dev.fndlsb.net:8080/market/{}"
}

# === Headers ===
NAVIGATION_HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.9,pt-PT;q=0.8,pt;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "http://xtt-nxt.nxt.betfair",
    "Referer": "http://xtt-nxt.nxt.betfair/facet_builder/facet_builder.html",
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest"
}

NAVIGATION_PAYLOAD = {
    "textQuery": {},
    "filter": {
        "productTypes": ["SPORTSBOOK"],
        "marketBettingTypes": ["ODDS"],
        "selectBy": "RANK",
        "contentGroup": {
            "language": "en",
            "regionCode": "UK"
        },
        "maxResults": 20
    },
    "facets": [],
    "currencyCode": "GBP",
    "locale": "en_GB"
}

# === Bet Type Mapping ===
BET_TYPE_MAP = {
    1: "SINGLE",
    2: "DOUBLE",
    3: "TREBLE",
    4: "FOURFOLD",
    5: "FIVEFOLD",
    6: "SIXFOLD",
    7: "SEVENFOLD",
    8: "EIGHTFOLD",
    9: "NINEFOLD",
    10: "TENFOLD",
    11: "ELEVENFOLD",
    12: "TWELVEFOLD",
    13: "THIRTEENFOLD",
    14: "FOURTEENFOLD",
    15: "FIFTEENFOLD",
    16: "SIXTEENFOLD",
    17: "SEVENTEENFOLD",
    18: "EIGHTEENFOLD",
    19: "NINETEENFOLD",
    20: "TWENTYFOLD",
    21: "TWENTYONEFOLD",
    22: "TWENTYTWOFOLD",
    23: "TWENTYTHREEFOLD",
    24: "TWENTYFOURFOLD",
    25: "TWENTYFIVEFOLD"
}
