import pytest

import drills
from trees import root

"""
Binary Tree
      1
    2   3
   5 6 7 8
"""


def test_pre_rec():
    assert drills.solution_pre_rec(root) == [1, 2, 5, 6, 3, 7, 8]
    assert drills.solution_pre_rec(None) == []


def test_pre_iter():
    assert drills.solution_pre_iter(root) == [1, 2, 5, 6, 3, 7, 8]
    assert drills.solution_pre_iter(None) == []


def test_in_rec():
    assert drills.solution_in_rec(root) == [5, 2, 6, 1, 7, 3, 8]
    assert drills.solution_in_rec(None) == []


def test_in_iter():
    assert drills.solution_in_iter(root) == [5, 2, 6, 1, 7, 3, 8]
    assert drills.solution_in_iter(None) == []


def test_post_rec():
    assert drills.solution_post_rec(root) == [5, 6, 2, 7, 8, 3, 1]
    assert drills.solution_post_rec(None) == []


def test_post_iter():
    assert drills.solution_post_iter(root) == [5, 6, 2, 7, 8, 3, 1]
    assert drills.solution_post_iter(None) == []


def test_level_recur():
    ans = [[1], [2, 3], [5, 6, 7, 8]]
    result = drills.solution_level_recur(root)
    for row, ans_row in zip(result, ans):
        assert row == ans_row
    assert drills.solution_level_recur(None) == []


def test_level_iter():
    ans = [[1], [2, 3], [5, 6, 7, 8]]
    result = drills.solution_level_iter(root)
    for row, ans_row in zip(result, ans):
        assert row == ans_row
    assert drills.solution_level_iter(None) == []
