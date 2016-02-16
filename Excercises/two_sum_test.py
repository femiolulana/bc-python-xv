import unittest

from two_sum import two_sum

class TwoSumTestSuite(unittest.TestCase):
  def test_list_range_4(self):
    result = two_sum([2,3,1,7], 8)
    self.assertEqual(result,[2,3])

  def test_list_range_5(self):
    result = two_sum([5, 1, 2, 3, 4], 3)
    self.assertEqual(result,[1, 2])

  def test_list_range_2(self):
    result = two_sum([1, 2], 3)
    self.assertEqual(result,[0, 1])

  def test_list_range_3(self):
    result = two_sum([5, 10, 1], 6)
    self.assertEqual(result,[0, 2])

  def test_list_range_6(self):
    result = two_sum([2, 6, 1, 5, 10, 4], 5)
    self.assertEqual(result,[2, 5])

  def test_list_range_7(self):
    result = two_sum([2, 6, 9, 1, 5, 10, 4], 5)
    self.assertEqual(result,[3, 6])

  def test_list_range_8(self):
    result = two_sum([7, 6, 0, 22, 3, 41, 6, 5], 12)
    self.assertEqual(result,[0, 7])

  def test_list_range_9(self):
    result = two_sum([7, 6, 0, 0, 13, 41, 6, 2, ], 15)
    self.assertEqual(result,[4, 7])

  def test_list_range_10(self):
    result = two_sum([3, 7, 6, 1, 22, 2, 41, 6, 5], 6)
    self.assertEqual(result,[3, 8])

  def test_list_range_14(self):
    result = two_sum([2, 0, 0, 1, 1, 1, 10, 1, 52, 20, 3, 0], 2)
    self.assertEqual(result,[0, 1])

if __name__ == "__main__":
  unittest.main()