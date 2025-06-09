# CODEX UNIQLO Tracker

該範例提供一個簡易的 `uniqlo_tracker.py` 腳本，可模擬追蹤 UNIQLO 商品價格。首次執行時會將內建的 base64 編碼商品清單解碼至 `price_data/products.csv`，隨後每次執行都會更新價格。

## 執行方式

```bash
python3 uniqlo_tracker.py
```

腳本會印出商品目前價格，如價格低於上次紀錄，則顯示降價訊息，同時會把新價格寫回 `price_data/products.csv`。
