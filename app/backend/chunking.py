# chunking text
# phase 3 step 1

import csv
import numpy as np
from typing import List


# wine data extraction
def wine_data_extraction():
    wine = ""
    with open("app/backend/data/wine-reviews/winemag-data_first150k.csv", "r", encoding="utf-8") as file:
        wine_array = []
        #,country,description,designation,points,price,province,region_1,region_2,variety,winery
        #only take country, description, province, regiono_1, region_2
        reader = csv.DictReader(file)
        for row in reader:
            line = f"{row['country']} {row['description']} {row['province']} {row['region_1']} {row['region_2']}"
            wine_array.append(line)
    wine = " ".join(wine_array)
    print(wine)
    return wine


def chunk_text(text: str, max_words: int = 200, overlap: int = 40) -> List[str]:
    words = text.split()
    chunks = []

    i = 0
    while i < len(words):
        chunk = words[i : i + max_words]
        if not chunk:
            break
        chunks.append(" ".join(chunk))
        i += max_words - overlap
    return chunks


if __name__ == "__main__":
    wine = wine_data_extraction()
    chunks = chunk_text(wine)
