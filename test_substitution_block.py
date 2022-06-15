from substitution_block import SubstitutionBlock

s_block = SubstitutionBlock(
    [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ]
)


def test_calculate_row_case_0():
    assert s_block.calculate_row(0b0000) == 0


def test_calculate_row_case_1():
    assert s_block.calculate_row(0b0001) == 0b1


def test_calculate_row_case_2():
    assert s_block.calculate_row(0b0010) == 0


def test_calculate_row_case_3():
    assert s_block.calculate_row(0b0011) == 0b1


def test_calculate_row_case_4():
    assert s_block.calculate_row(0b0100) == 0


def test_calculate_row_case_5():
    assert s_block.calculate_row(0b0101) == 0b1


def test_calculate_row_case_6():
    assert s_block.calculate_row(0b0110) == 0


def test_calculate_row_case_7():
    assert s_block.calculate_row(0b0111) == 0b1


def test_calculate_row_case_8():
    assert s_block.calculate_row(0b1000) == 0b10


def test_calculate_row_case_9():
    assert s_block.calculate_row(0b1001) == 0b11


def test_calculate_row_case_10():
    assert s_block.calculate_row(0b1010) == 0b10


def test_calculate_row_case_11():
    assert s_block.calculate_row(0b1011) == 0b11


def test_calculate_row_case_12():
    assert s_block.calculate_row(0b1100) == 0b10


def test_calculate_row_case_13():
    assert s_block.calculate_row(0b1101) == 0b11


def test_calculate_row_case_14():
    assert s_block.calculate_row(0b1110) == 0b10


def test_calculate_row_case_15():
    assert s_block.calculate_row(0b1111) == 0b11


def test_calculate_column_case_0():
    assert s_block.calculate_column(0b0000) == 0


def test_calculate_column_case_1():
    assert s_block.calculate_column(0b0001) == 0


def test_calculate_column_case_2():
    assert s_block.calculate_column(0b0010) == 0b1


def test_calculate_column_case_3():
    assert s_block.calculate_column(0b0011) == 0b1


def test_calculate_column_case_4():
    assert s_block.calculate_column(0b0100) == 0b10


def test_calculate_column_case_5():
    assert s_block.calculate_column(0b0101) == 0b10


def test_calculate_column_case_6():
    assert s_block.calculate_column(0b0110) == 0b11


def test_calculate_column_case_7():
    assert s_block.calculate_column(0b0111) == 0b11


def test_calculate_column_case_8():
    assert s_block.calculate_column(0b1000) == 0


def test_calculate_column_case_9():
    assert s_block.calculate_column(0b1001) == 0


def test_calculate_column_case_10():
    assert s_block.calculate_column(0b1010) == 0b1


def test_calculate_column_case_11():
    assert s_block.calculate_column(0b1011) == 0b1


def test_calculate_column_case_12():
    assert s_block.calculate_column(0b1100) == 0b10


def test_calculate_column_case_13():
    assert s_block.calculate_column(0b1101) == 0b10


def test_calculate_column_case_14():
    assert s_block.calculate_column(0b1110) == 0b11


def test_calculate_column_case_15():
    assert s_block.calculate_column(0b1111) == 0b11


def test_undo_indexes_case_0():
    assert s_block.reverse_indexes(0b00, 0b00) == 0b0000


def test_undo_indexes_case_1():
    assert s_block.reverse_indexes(0b00, 0b01) == 0b0010


def test_undo_indexes_case_2():
    assert s_block.reverse_indexes(0b00, 0b10) == 0b0100


def test_undo_indexes_case_3():
    assert s_block.reverse_indexes(0b00, 0b11) == 0b0110


def test_undo_indexes_case_4():
    assert s_block.reverse_indexes(0b01, 0b00) == 0b0001


def test_undo_indexes_case_5():
    assert s_block.reverse_indexes(0b01, 0b01) == 0b0011


def test_undo_indexes_case_6():
    assert s_block.reverse_indexes(0b01, 0b10) == 0b0101


def test_undo_indexes_case_7():
    assert s_block.reverse_indexes(0b01, 0b11) == 0b0111


def test_undo_indexes_case_8():
    assert s_block.reverse_indexes(0b10, 0b00) == 0b1000


def test_undo_indexes_case_9():
    assert s_block.reverse_indexes(0b10, 0b01) == 0b1010


def test_undo_indexes_case_10():
    assert s_block.reverse_indexes(0b10, 0b10) == 0b1100


def test_undo_indexes_case_11():
    assert s_block.reverse_indexes(0b10, 0b11) == 0b1110


def test_undo_indexes_case_12():
    assert s_block.reverse_indexes(0b11, 0b00) == 0b1001


def test_undo_indexes_case_13():
    assert s_block.reverse_indexes(0b11, 0b01) == 0b1011


def test_undo_indexes_case_14():
    assert s_block.reverse_indexes(0b11, 0b10) == 0b1101


def test_undo_indexes_case_15():
    assert s_block.reverse_indexes(0b11, 0b11) == 0b1111
