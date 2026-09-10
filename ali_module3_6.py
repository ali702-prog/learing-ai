from fastapi import FastAPI
import math

app = FastAPI()


items = [
    "Item 1", "Item 2", "Item 3", "Item 4", "Item 5",
    "Item 6", "Item 7", "Item 8", "Item 9", "Item 10",
    "Item 11", "Item 12", "Item 13", "Item 14", "Item 15",
    "Item 16", "Item 17", "Item 18", "Item 19", "Item 20"
]


@app.get("/items")
def get_items(page: int = 1, size: int = 5):

    start = (page - 1) * size
    end = start + size

    page_items = items[start:end]

    total_items = len(items)
    total_pages = math.ceil(total_items / size)

    return {
        "page": page,
        "size": size,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": page_items
    }