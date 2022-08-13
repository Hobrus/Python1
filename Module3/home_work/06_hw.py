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
for element in items:
    brand = element["brand"]
    if brands.count(brand) == 0:
        brands.append(brand)
print(*brands, sep=", ", end=".\n")

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here
brands = []
goods = []
for element in items:
    brand = element["brand"]
    if brands.count(brand) == 0:
        brands.append(brand)
    goods.append(brand)
#for brand in brands:
#    goods.count(brand)
#    print(goods.count(brand))
max_brands = []
max_goods = 0
for brand in brands:
    if goods.count(brand) > max_goods:
        max_brands = [brand]
        max_goods = goods.count(brand)
    elif goods.count(brand) == max_goods:
        max_brands.append(brand)
#print(brands)
#print(goods)
print(*max_brands, sep=", ", end=".\n")

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
max_price = 0
max_brands = []
for element in items:
    el_price = element["price"]
    el_brand = element["brand"]
    if el_price > max_price:
        max_price = el_price
        max_brands = [el_brand]
    elif el_price == max_price:
        if max_brands.count(el_brand) == 0:
            max_brands.append(el_brand)

print(*max_brands, sep=", ", end=".\n")
