from abc import abstractmethod

class DockerInterface:

  @abstractmethod
  def run(): # コンテナを立ち上げる
    pass

  @abstractmethod
  def build(): # イメージをビルドする
    pass

  @abstractmethod
  def tag(): # コンテナに名前をつける
    pass

  @abstractmethod
  def volume():
    pass
