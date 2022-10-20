from abc import ABC, ABCMeta, abstractmethod

# インターフェース（仕様、本質、実装）
class FileManagerInterface(ABC):

  @abstractmethod
  def writeFile(self): pass # ファイルに書き込む

  @abstractmethod
  def exec(self): pass # コードを実行する（dockerを呼ぶ）
