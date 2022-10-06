class Calculate:
  # コンストラクタでメンバ変数に引数の演算結果をいれる
  def __init__(self, arg1) -> None:
    self.result = arg1*2

  # ゲッター
  def get_result(self):
    return self.result
