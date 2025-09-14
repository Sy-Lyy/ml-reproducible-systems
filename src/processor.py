# processor.py
from typing import List

class DataProcessor:
    def __init__(self, data: List[float]):
        self.data = data


if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    print("loaded:", p.data)
