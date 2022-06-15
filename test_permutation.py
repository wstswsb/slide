from permutation import Permutation

base_permutation = Permutation([1, 4, 3, 2])
expand_permutation = Permutation([3, 2, 4, 1, 4, 1, 3, 2])


def test_base_case_0():
    assert base_permutation.do(0b0000) == 0b0000
    assert base_permutation.undo(0b0000) == 0b0000


def test_base_case_1():
    assert base_permutation.do(0b0001) == 0b0100
    assert base_permutation.undo(0b0100) == 0b001


def test_base_case_2():
    assert base_permutation.do(0b0010) == 0b0010
    assert base_permutation.undo(0b0010) == 0b0010


def test_base_case_3():
    assert base_permutation.do(0b0011) == 0b0110
    assert base_permutation.undo(0b0110) == 0b0011


def test_base_case_4():
    assert base_permutation.do(0b0100) == 0b0001
    assert base_permutation.undo(0b0001) == 0b0100


def test_base_case_5():
    assert base_permutation.do(0b0101) == 0b0101
    assert base_permutation.undo(0b0101) == 0b0101


def test_base_case_6():
    assert base_permutation.do(0b0110) == 0b0011
    assert base_permutation.undo(0b0011) == 0b0110


def test_base_case_7():
    assert base_permutation.do(0b0111) == 0b0111
    assert base_permutation.undo(0b0111) == 0b0111


def test_base_case_8():
    assert base_permutation.do(0b1000) == 0b1000
    assert base_permutation.undo(0b1000) == 0b1000


def test_base_case_9():
    assert base_permutation.do(0b1001) == 0b1100
    assert base_permutation.undo(0b1100) == 0b1001


def test_base_case_10():
    assert base_permutation.do(0b1010) == 0b1010
    assert base_permutation.undo(0b1010) == 0b1010


def test_base_case_11():
    assert base_permutation.do(0b1011) == 0b1110
    assert base_permutation.undo(0b1110) == 0b1011


def test_base_case_12():
    assert base_permutation.do(0b1100) == 0b1001
    assert base_permutation.undo(0b1001) == 0b1100


def test_base_case_13():
    assert base_permutation.do(0b1101) == 0b1101
    assert base_permutation.undo(0b1101) == 0b1101


def test_base_case_14():
    assert base_permutation.do(0b1110) == 0b1011
    assert base_permutation.undo(0b1011) == 0b1110


def test_base_case_15():
    assert base_permutation.do(0b1111) == 0b1111
    assert base_permutation.undo(0b1111) == 0b1111


def test_expand_case_0():
    assert expand_permutation.do(0b0000) == 0b0000_0000
    assert expand_permutation.undo(0b0000_0000) == 0b0000


def test_expand_case_1():
    assert expand_permutation.do(0b0001) == 0b0010_1000
    assert expand_permutation.undo(0b0010_1000) == 0b001


def test_expand_case_2():
    assert expand_permutation.do(0b0010) == 0b1000_0010
    assert expand_permutation.undo(0b1000_0010) == 0b0010


def test_expand_case_3():
    assert expand_permutation.do(0b0011) == 0b1010_1010
    assert expand_permutation.undo(0b1010_1010) == 0b0011


def test_expand_case_4():
    assert expand_permutation.do(0b0100) == 0b0100_0001
    assert expand_permutation.undo(0b0100_0001) == 0b0100


def test_expand_case_5():
    assert expand_permutation.do(0b0101) == 0b0110_1001
    assert expand_permutation.undo(0b0110_1001) == 0b0101


def test_expand_case_6():
    assert expand_permutation.do(0b0110) == 0b1100_0011
    assert expand_permutation.undo(0b1100_0011) == 0b0110


def test_expand_case_7():
    assert expand_permutation.do(0b0111) == 0b1110_1011
    assert expand_permutation.undo(0b1110_1011) == 0b0111


def test_expand_case_8():
    assert expand_permutation.do(0b1000) == 0b0001_0100
    assert expand_permutation.undo(0b0001_0100) == 0b1000


def test_expand_case_9():
    assert expand_permutation.do(0b1001) == 0b0011_1100
    assert expand_permutation.undo(0b0011_1100) == 0b1001


def test_expand_case_10():
    assert expand_permutation.do(0b1010) == 0b1001_0110
    assert expand_permutation.undo(0b1001_0110) == 0b1010


def test_expand_case_11():
    assert expand_permutation.do(0b1011) == 0b1011_1110
    assert expand_permutation.undo(0b1011_1110) == 0b1011


def test_expand_case_12():
    assert expand_permutation.do(0b1100) == 0b0101_0101
    assert expand_permutation.undo(0b0101_0101) == 0b1100


def test_expand_case_13():
    assert expand_permutation.do(0b1101) == 0b0111_1101
    assert expand_permutation.undo(0b0111_1101) == 0b1101


def test_expand_case_14():
    assert expand_permutation.do(0b1110) == 0b1101_0111
    assert expand_permutation.undo(0b1101_0111) == 0b1110


def test_expand_case_15():
    assert expand_permutation.do(0b1111) == 0b1111_1111
    assert expand_permutation.undo(0b1111_1111) == 0b1111
