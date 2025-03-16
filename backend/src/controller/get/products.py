from models import product, filtered_products
from schemas import Filter


def product_id(id):
    result = product(id)
    return result


def products_filtered(data: Filter):
    result = filtered_products(data)
    return result
