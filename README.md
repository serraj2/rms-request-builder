# RMS Request Builder

A graphical tool to build JSON bet requests from the internal Betfair RMS APIs.

## 🧰 Features

- Select environment: `nxtbs1` or `intbs1`
- Choose number of selections (1–25)
- Generates request with correct odds and event IDs
- Sends automatic refresh event calls
- Copy final request to clipboard

## ▶️ How to run

```bash
pip install -r requirements.txt
python rmsPlaceReq.py