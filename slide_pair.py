import re
from typing import NamedTuple


class SlidePair(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int

    def left(self, num: int):
        return (num >> 4) & 0b1111

    def right(self, num: int):
        return num & 0b1111

class SlidePairLoader:
    def load_list_from_file(self, filename: str) -> list[SlidePair]:
        with open(filename, 'r', encoding="cp1251") as file:
            content = file.read()
        nums = self._extract_nums(content)
        return [
            SlidePair(*nums[i-4: i])
            for i
            in range(4, len(nums) + 1, 4)
        ]

    def _extract_nums(self, content: str) -> list[int]:
        nums = re.findall(r"[0,1]{8}", content)
        return [int(num, 2) for num in nums]
