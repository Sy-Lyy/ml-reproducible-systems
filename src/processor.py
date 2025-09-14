# processor.py
from typing import List

class DataProcessor:
    def __init__(self, data: List[float]):
        self.data = data


if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    print("loaded:", p.data)

# processor.py
from typing import List

class DataProcessor:
    def __init__(self, data: List[float]):
        self.data = data

    def mean(self) -> float:
        if not self.data:
            raise ValueError("Data is empty.")
        return sum(self.data) / len(self.data)

    def variance(self) -> float:
        m = self.mean()
        return sum((x - m) ** 2 for x in self.data) / len(self.data)
  if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    help(p.mean)
