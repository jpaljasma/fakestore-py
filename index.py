from fakestoreapi.products import Products
from fakestoreapi.base import ApiRequestException
from tabulate import tabulate
import locale
import textwrap

locale.setlocale(locale.LC_ALL, "en_US")


def truncate(s: str, limit: int = 40) -> str:
    """
    Truncates a string `s` with a character `limit`, and appends `...` as a placeholder
    """
    return textwrap.shorten(s, width=limit, placeholder="...")


p = Products()

products = []
try:
    products = p.list()
except ApiRequestException as erx:
    print("[Error] accessing Products API:", erx)

headers = ["Id", "Product Title", "Price"]
data = []
for prod in products:
    data.append(
        [
            prod["id"],
            truncate(prod["title"], 32),
            locale.currency(prod["price"], grouping=True),
        ]
    )

print(tabulate(data, headers=headers))
