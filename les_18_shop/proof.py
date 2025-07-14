Product.objects.create(
    name=product['name'],
    category=product['category'],
    supplier=product['supplier'],
    price=product['price'],
    quantity=product['quantity'],
    article=product['article'],
    available=product['available']
)

