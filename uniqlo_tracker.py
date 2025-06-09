import os
import csv
import base64
import random

DATA_DIR = 'price_data'
SAMPLE_CSV_B64 = (
    "cHJvZHVjdF9pZCxwcm9kdWN0X25hbWUscHJpY2UKMTIzLFVuaXFsbyBULVNoaXJ0LDE5Ljk5Cj"
    "Q1NixVbmlxbG8gSmVhbnMsMzkuOTkK"
)


def ensure_sample_csv():
    os.makedirs(DATA_DIR, exist_ok=True)
    csv_path = os.path.join(DATA_DIR, 'products.csv')
    if not os.path.exists(csv_path):
        data = base64.b64decode(SAMPLE_CSV_B64)
        with open(csv_path, 'wb') as f:
            f.write(data)
    return csv_path


def load_products(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def fetch_current_price(product_id):
    # TODO: Replace with real fetching from UNIQLO site
    return round(random.uniform(10, 50), 2)


def save_products(csv_path, products):
    fieldnames = ['product_id', 'product_name', 'price']
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


def main():
    csv_path = ensure_sample_csv()
    products = load_products(csv_path)

    for product in products:
        current_price = fetch_current_price(product['product_id'])
        last_price = float(product['price'])
        if current_price < last_price:
            print(f"{product['product_name']} 降價 {last_price} -> {current_price}")
        else:
            print(f"{product['product_name']} 目前價格 {current_price}")
        product['price'] = str(current_price)

    save_products(csv_path, products)


if __name__ == '__main__':
    main()
