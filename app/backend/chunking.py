# chunking text
# phase 3 step 1

import numpy as np
import pandas as pd
from typing import List


def create_row_text(row):
    country = row["country"]
    description = row["description"]
    province = row["province"]
    region_1 = row["region_1"]
    region_2 = row["region_2"]

    return f"{country} {description} {province} {region_1} {region_2}"


# wine data extraction
def wine_data_extraction(file: str):
    dataframe = pd.read_csv(
        file, usecols=["country", "description", "province", "region_1", "region_2"]
    )
    data_list = dataframe.apply(create_row_text, axis=1).tolist()
    return " ".join(data_list)


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
