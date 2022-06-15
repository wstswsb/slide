from substitution_block import SubstitutionBlock
from permutation import Permutation
from slide_pair import SlidePairLoader, SlidePair

PE = [3, 2, 4, 1, 4, 1, 3, 2]
P = [1, 4, 3, 2]
S1 = [
    [1, 1, 2, 0],
    [3, 2, 3, 0],
    [0, 0, 1, 3],
    [3, 2, 1, 2],
]
S2 = [
    [2, 2, 0, 3],
    [1, 1, 0, 0],
    [3, 3, 2, 2],
    [0, 3, 1, 1],
]
mask = [1, 1, 1, 1]

s1 = SubstitutionBlock(S1)
s2 = SubstitutionBlock(S2)
p = Permutation(P)
pe = Permutation(PE)
slide_pairs = SlidePairLoader().load_list_from_file("Анализ_варианта 4.txt")


def find_s_merged_input(s1_inputs: list[int], s2_inputs: list[int]):
    result = []
    for s1_inp in s1_inputs:
        for s2_inp in s2_inputs:
            merged_input = ((s1_inp & 0b1111) << 4) | (s2_inp & 0b1111)
            result.append(merged_input)
    return result


def process_f(input_f: int, output_f: int) -> list[int]:
    pe_input = pe.do(input_f)

    undo_p = p.undo(output_f)
    s1_out = (undo_p >> 2) & 0b11
    s2_out = undo_p & 0b11
    s1_inputs = s1.unsubstitute(s1_out)
    s2_inputs = s2.unsubstitute(s2_out)
    s_merged_inputs = find_s_merged_input(s1_inputs, s2_inputs)
    return [
        pe_input ^ s_input_variant
        for s_input_variant
        in s_merged_inputs
    ]


def process_f1(slide_pair: SlidePair) -> list[int]:
    input_f = slide_pair.right(slide_pair.x1)
    output_f = slide_pair.right(slide_pair.x2) ^ slide_pair.left(slide_pair.x1)
    keys = process_f(input_f, output_f)
    return keys


def process_f_last(slide_pair: SlidePair) -> list[int]:
    input_f = slide_pair.right(slide_pair.y2)
    output_f = slide_pair.left(slide_pair.y2) ^ slide_pair.right(slide_pair.y1)
    keys = process_f(input_f, output_f)
    return keys


def count_keys(input_keys: list[int], output_keys: list[int]) -> dict[int, int]:
    keys = {key: 0 for key in input_keys + output_keys}
    for input_key in input_keys:
        if input_key in output_keys:
            keys[input_key] += 1
    return keys


def present_keys(counted_keys: dict[int, int]) -> str:
    result = ""
    for key, value in counted_keys.items():
        if value == 0:
            continue
        result += f"{key:09_b} -> {value}\n"
    return result


def main():
    input_keys = []
    output_keys = []
    for pair in slide_pairs:
        input_keys += process_f1(pair)
        output_keys += process_f_last(pair)
    counted_keys = count_keys(input_keys, output_keys)
    print(present_keys(counted_keys))


if __name__ == '__main__':
    main()
