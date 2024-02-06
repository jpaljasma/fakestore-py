from fakestoreapi.products import Products
from fakestoreapi.base import ApiRequestException
from tabulate import tabulate
import locale
import textwrap

locale.setlocale(locale.LC_ALL, "en_US")


# Color-coding and formatting
RED_START = "\033[91m"
GREEN_START = "\033[32m"
GREY_START = "\033[90m"
BOLD_START = "\u001b[1m"
ITALIC_START = "\033[3m"
END = "\033[0m"


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
    print(f"{RED_START}{BOLD_START}[ERROR]{END}\tAccessing Products API failed:", erx)
    exit()

headers = ["Id", "Product Title", "Category", "Price"]
data = []
for prod in products:
    data.append(
        [
            prod["id"],
            truncate(prod["title"], 50),
            prod['category'].title(),
            locale.currency(prod["price"], grouping=True),
        ]
    )

print(tabulate(data, headers=headers))
