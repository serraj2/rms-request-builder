# config.py

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

REFRESH_ENDPOINT = "https://da.paddypower.com.nxt.ppbdev.com/admin-services/service/refresh/events"

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

REFRESH_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en;q=0.9,pt-PT;q=0.8,pt;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://da.paddypower.com.nxt.ppbdev.com",
    "priority": "u=1, i",
    "referer": "https://da.paddypower.com.nxt.ppbdev.com/admin-services/",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Cookie": (
        "SESSION=YmZlMjBhZmEtNzYyMi00NGJkLWIxOTUtMTNmM2MyMzQ4ZmY2; "
        "_ga=GA1.2.552475128.1754484294; "
        "_gid=GA1.2.2077152948.1754484294; "
        "__cf_bm=sWxv5XdGNEetdI4avKVM3ftntDQPECGwrkzEi9LJYJE-1754485924-1.0.1.1-"
        "neuZcyR9WtRF5.0iuAAzcyZbZVt1PKaJwr0c_8Atve6hQFkuXlI.MrHXeT546MOopkWi.lTl5NSx.V8VivZ5UbetXfqnAPa5uFvWYBFWfLw; "
        "_gat_gtag_UA_132972192_2=1"
    )
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
