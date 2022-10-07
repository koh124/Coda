import unittest
import sample

class Calculate(unittest.TestCase):

  # pytestはメソッド名の頭に"test"とついたものを実行してテストする
  def test_get_result(self):
    calc = sample.Calculate(100)
    result = calc.get_result()
    self.assertEqual(result, 200) # アサーション

if __name__ == '__main__':
  unittest.main()

# ↓コマンドラインで実行するとテストできる
# pytest
