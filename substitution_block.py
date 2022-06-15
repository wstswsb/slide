class SubstitutionBlock:
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix

    def substitute(self, block: int):
        row = self.calculate_row(block)
        column = self.calculate_column(block)
        return self.__matrix[row][column]

    def unsubstitute(self, block: int) -> list[int]:
        indexes = []
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                if self.__matrix[i][j] != block:
                    continue
                indexes.append(self.reverse_indexes(i, j))
        return indexes

    def reverse_indexes(self, i: int, j: int) -> int:
        result = 0
        result |= (i & 0b10) << 2
        result |= (j & 0b11) << 1
        result |= (i & 0b01)
        return result

    def calculate_row(self, block: int):
        return (block & 1) | (block >> 2) & 0b10

    def calculate_column(self, block):
        return (block >> 1) & 0b11