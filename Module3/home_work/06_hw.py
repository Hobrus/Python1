# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here
brands = []
for item in items:
    brands.append(item["brand"])
brands = set(brands)
print(*brands, sep=", ")

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here
brands_count = {brand: 0 for brand in brands}
for item in items:
    brands_count[item['brand']] = brands_count[item['brand']] + 1
max_count = max(brands_count.values())
max_count_brands = [brand for brand, count in brands_count.items() if count == max_count]
print(*max_count_brands, sep=", ")

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
max_price = 0
for item in items:
    if item['price'] > max_price:
        max_price = item['price']
max_price_brands = []
for item in items:
    if item['price'] == max_price:
        max_price_brands.append(item['brand'])
print(*max_price_brands, sep=", ")
