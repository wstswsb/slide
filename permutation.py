class Permutation:
    def __init__(self, order: list[int]):
        self.__order = order
        self.__unique_order = self._create_unique_order(self.__order)

    def do(self, block: int) -> int:
        binary_block_view = self.get_binary_view(block)
        permuted_binary_block_view = "".join(
            [
                binary_block_view[i - 1]
                for i in self.__order
            ]
        )
        return int(permuted_binary_block_view, 2)

    def undo(self, block: int) -> int:
        binary_block_view = self.get_binary_view(block)
        template = ["" for _ in range(len(self.__unique_order))]
        for index, position in enumerate(self.__unique_order):
            template[position - 1] = binary_block_view[index]
        return int("".join(template), 2)

    def get_binary_view(self, block: int):
        binary_view = f"{block:>04b}"
        if len(binary_view) > 4:
            binary_view = f"{block:>08b}"
        return binary_view

    def _create_unique_order(self, order: list[int]) -> list[int]:
        result = []
        for item in order:
            if item in result:
                continue
            result.append(item)
        return result
