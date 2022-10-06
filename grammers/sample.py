import math
print(math.sqrt(4))

# コメントアウト
# ここはコメントです

"""
三重引用符
ダブルクオテーションとシングルクオテーションをこのように使うとエラーが発生しない
複数行書く場合のコメントとして使用されている
文字列型という扱いなので、ちゃんと変数に入れて持ち運びできる
"""
'''
こちらも同様にエラーが発生しない
'''

# 三重引用符を使った文字列を変数に格納
comment = """
三重引用符が入っています
"""
print(comment)

# 各行末には改行コード"\n"が含まれており、行末にバックスラッシュを入れることで削除できる
blank = """\
このコメントは改行が含まれない\
"""
print(blank)

# 変数
variable = 'Hello world!'
print(variable)
# Hello world!

# 定数宣言はないので、慣習的に大文字で変数名を定義する
# 上書きしないように気をつける
POKEMON_NAME = "Garchomp"

# 【文字列】
# print "Hello World"
# print 'Hello Python'

# 文字列の中にバックスラッシュを挿入できる
# \nで改行、\tでtab
# バックスラッシュはoption + ¥（mac）
escape = "he\nllo wor\tld"
print(escape)
# he
# llo wor ld

# 文字列も演算できる
print("hello" * 2)
# hellohello
print("hello" + " world")
# hello world

# 比較演算子は文字数の比較をboolで返す
print("hello" > "hello")
# false
print("hello" > "hear")
# true
print("hello" >= "hello")
# true

# 変数を埋め込むには%を使って引数を渡す
# 渡す型によって書式が異なる
# %s = str（文字）, %d = decimal（整数）, %f = float（浮動小数点）
# 違う型を渡すとエラーになる
name = "kohei"
sex = "male"
print("name: %s, sex: %s" % (name, sex))
# name: kohei, sex: male

# formatを使っても変数を埋め込める
city = "Tokyo"
country = "Japan"
print("I live in {0}, {1}".format(city, country))

# 文字列リテラルを使うと簡単に変数展開できる
str = f"{country}"
print(str)

# 【論理記号】
# True, Falseは大文字で書かないとエラーになる
print(True and False)
print(True or False)
print(not True)

# if文は条件式のあとにコロン、処理はインデント
# elseifはご覧の通り
number = 51
if number % 3 == 0 and number % 5 == 0:
    print("15の倍数です")
elif number % 3 == 0:
    print("3の倍数です")
elif number % 5 == 0:
    print("5の倍数です")
else:
    print("3の倍数でも5の倍数でもありません")

# "1以上 and 9以下"をシンプルに記述できる
num = 1
if 1 <= num <= 9:
    print("1以上かつ9以下")

# 三項演算子
score = 100
print("100点" if score == 100 else "100点未満")

# 【ループ処理】
# rangeは0〜9の数字が入った配列をつくる
# inは後続の配列の要素を一つずつ取り出す
for i in range(10):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 1):
    print(i)
# 1~9が出力される

# カウントダウン
for i in range(10, 0, -1):
    print(i)
# 10~1が出力される

# continueでスキップ処理を行う
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue
    print(i)

# 二重配列の要素を2つずつ取り出すこともできる
for name, sex in [["kohei", "male"], ["hey", "male"]]:
    print(name)
    print(sex)

# forループの最後にelseを書くことができて、終了時の処理を書ける
for i in range(10):
    print(i)
else:
    print("0から9まで出力")

# whileループ
i = 0
while i < 5:
    i += 1
    if i == 4:
        print(f"ループはi = {i}で終了")

# 【関数】
# 関数の定義


def sayGreeting(word):
    print(word)


# 関数の呼び出し
sayGreeting("Hello world!")

# 引数をformatで埋め込む


def favoriteFruit(fruit):
    print("My favorite fruit is {0}".format(fruit))


favoriteFruit("Apple")

# 関数の引数にはデフォルト値を使える


def Date(month="02", date="12"):
    print('日付は%s/%s' % (month, date))


Date()
Date("01", "28")
# 渡すときに引数名を書くことができ、順番は関係ない
Date(date="31", month="08")

# 戻り値


def addNumber(num1, num2):
    return num1 + num2


print(addNumber(2, 2))

# passを記述すると関数を無視できる
# あとで書きたいときなどに使う


def something():
    pass


# エラーが発生しない
# 戻り値はNone
something()
print(something())

# 変数のスコープ
# 関数内で定義されるとローカルスコープ
# 関数の外で定義されるとグローバルスコープ
scope = "global"


def varScope():
    scope = "local"
    print(scope)


# 関数で上書きされたローカル変数が出力
varScope()
# ローカルで変数を宣言してもグローバル変数は変わらず
print(scope)

varSafe = "safe"


def scopeError():
    # 通常はグローバル変数をローカルで使うことはできる
    print(varSafe)
    # ローカルで変数を定義する前にグローバルで定義済みの同名の変数を使うことはできない（エラー）
    # print(scope)
    scope = "local"


scopeError()


# グローバル変数をローカルで書き換えるにはglobalを使う
varGlobal = "This is global"


def reWriteGlobal():
    global varGlobal
    varGlobal = "This is also global"


# 書き換える前のグローバル変数
print(varGlobal)
# 書き換えたあとのグローバル変数
reWriteGlobal()
print(varGlobal)

# 【クラス】


class User:
    # クラス属性、アトリビュート、プロパティと言ったりする
    name = "kohei"
    country = "Japan"


# インスタンスを生成
user = User()
print(user.name)
print(user.country)


# クラスにもpassを使える
class Empty:
    pass

# プロパティはインスタンス生成後に設定することもできる
exists = Empty()
exists.info = "this attr is added after making empty instance"
print(exists.info)

# インスタンスメソッド
class Human:
    # メソッド、振る舞いと言ったりする
    # 受け取れる引数を最低一つ設定する必要がある
    # 第一引数には呼び出したインスタンス自身が格納される（インスタンス変数）
    # selfじゃなくてもいい
    def run(test):
        print("human is running")

    def runAgain(self):
        self.run()


human = Human()
human.run()
human.runAgain()

# クラスメソッド
class Seasons:
    four_seasons = ["spring", "summer", "autumn", "winter"]
    season_index = 0
    # クラスの中からクラスプロパティを参照することはできる
    print(season_index)

    # これがないとエラー（デコレーター）
    @classmethod
    def season(cls):
        # クラスメソッドの中からはクラスプロパティはクラス経由でないと参照できない
        print(cls.four_seasons[cls.season_index])
        if cls.season_index == 3:
            cls.season_index = 0
        else:
            cls.season_index += 1

Seasons.season()
Seasons.season()


# コンストラクタ
class Computer:
    def __init__(self, name):
        self.name = name

computer1 = Computer("mac")
computer2 = Computer("windows")
print(computer1.name)
print(computer2.name)

# クラス変数
class Calculate:
    # クラス及びインスタンスで共有して使える変数を設定することができる
    count = 0

    def __init__(self, number):
        Calculate.count += 1
        self.number = number

# クラスの外からアクセスできる
print(f"first count is {Calculate.count}")
one = Calculate("one")
print(f"my count is {one.count}")
two = Calculate("two")
print(f"I can also access my count \"{Calculate.count}\" directly from Class")

# アクセス権
# pythonにはpublic、privateはない
# だがクラスの外からアクセスできないようにする機能がある
class Cafe:
    def __init__(self, name, place):
        # "name"と"__name"は別のプロパティとして区別される
        self.name = name
        self.place = place

        # クラスの外からアクセスできないようにするにはプロパティ名の前に__をつける
        self.__name = "__" + name
        self.__place = "__" + place

        # どちらもクラスの中からは出力できることが分かる
        print(self.name)
        print(self.__name)
# ここからクラス外

starbucks = Cafe("Starbucks", "Shinjuku")

# nameはクラス外からアクセスできるが、
# __nameはアクセスできないことが分かる（エラー）
print(starbucks.name)
# print(starbucks.__name)

# __nameの頭に_クラス名をつけるとアクセスできるようになっている
# _Cafeと__nameの間に.（ピリオド）が入らないので注意
print(starbucks._Cafe__name)


# クラス継承
class programmingLang:
    # 親クラスのコンストラクタ
    def __init__(self, lang, framework):
        self.lang = lang
        self.framework = framework
        self.helloWorld()

    def helloWorld(self):
        print(f"親クラスのメソッド: Hello {self.lang}")
        print(f"親クラスのメソッド: フレームワークは{self.framework}です")

    # 子クラスで呼び出せることを確認する用のメソッド
    def add(self, arg1, arg2):
        return arg1 + arg2

    def thisIsForOverRide(self):
        print("オーバーライドされる前です")


class frontProgrammingLang(programmingLang):
    # 子クラスのコンストラクタ
    def __init__(self, lang, framework):
        # 親クラスを継承できていればプロパティがセットされているが...
        # 親クラスのコンストラクタが機能していない（エラー）
        # print(self.lang, self.framework)

        #だが 親クラスのメソッドは共有して使えることが分かる
        print(self.add(5, 5))

        # super()を使うと親クラスのコンストラクタを呼び出すことができる
        super().__init__(lang, framework)
        # 今度はエラーにならない
        print(self.lang, self.framework)

        # 親クラスでセットされたプロパティを書き換えることができる
        self.lang = "html"
        self.framework = "Bootstrap"
        print(self.lang, self.framework)

    def multiple(self, arg1, arg2):
        return arg1 * arg2

    # メソッドのオーバーライドができる
    def thisIsForOverRide(self):
        print("オーバーライドした後です")

# 親クラスのオブジェクトを生成する
python = programmingLang("python", "Django")
print(python.lang, python.framework)

javascript = frontProgrammingLang("Javascript", "Vue.js")

# 何でも呼び出せるようになる
print(javascript.add("今日は", "いい天気です"))
# 子クラスのコンストラクタで書き換えたプロパティが適用されていることが分かる
javascript.helloWorld()

# 子クラスに定義されたメソッドを子クラスが使うことができるが
print(javascript.multiple(3, 4))
# 親クラスのインスタンスから呼び出すことはできない
# print(python.multiple(5, 6))

# 子クラスでメソッドをオーバーライドすることができる
python.thisIsForOverRide()
javascript.thisIsForOverRide()

# モジュールの読み込み
# モジュールは読み込んだときに一度実行される
# 変数は読み込めない

# import ファイル名（すべて読み込み）
# モジュールにアクセスするときは"ファイル名.モジュール名"
import favorite
lionking = favorite.Favorite("ライオンキング")
lionking.introduce()

# モジュールは関数でもよい
favorite.doSomething("did something")

# from ファイル名 import クラス名, クラス名, ...（モジュール指定）
from drink import Drink, Coffee
apple_juice = Drink("アップルジュース")
apple_juice.pour()

ice_coffee = Coffee("アイスコーヒー")
ice_coffee.pour()

# 【配列操作】
Languages = ["Japanese", "English", "Chinese"]

# 要素の取り出し
print(Languages[0])

# 代入しながら出力することはできない（エラー）
# print(Languages[0] = "Spanish")

# 要素の更新
Languages[0] = "Spanish"
print(Languages[0])

# 配列の要素の数
print(len(Languages))

# 要素の追加
Languages.append("Italic")
print(Languages[3])

# リストどうしの結合
evens = [0, 2, 4, 6, 8]
odds = [1, 3, 5, 7, 9]
print(evens + odds)

# appendを使わない追加
array = []
for i in range(1, 10):
    # 配列どうしの演算でしか追加できないことに注意
    array += [i]
print(array)

# 空のリスト
print([])

# こういう配列初期化の方法もある
print([""] * 3)
print([None] * 5)

# 要素の文字列結合
messages = ["私は", "朝食に", "オートミールを", "食べました"]
# str型オブジェクトから呼び出せるメソッドなので注意
str1 = ""
print(str1.join(messages))
# 区切り文字も入れられる
str2 = " "
print(str2.join(messages))

# 例外処理
def Divide(a, b):
    try:
        result = a/b
        print(f"{a}/{b} = {int(result)}をトライしました")
        # pythonに標準搭載のexception
    except ZeroDivisionError:
        print("not by zero")
    else: print("例外処理はなし")
    finally: print("必ず最後に処理される")
Divide(10, 2)
Divide(5, 0)

# 自分で例外処理をつくる
class Exception(Exception):
    pass

def output():
    try:
        for i in range(100):
            if i**2 > 5000:
                raise Exception("over 5000")
            else: print(i**2)
    except Exception as e:
        print(f"エラーメッセージは{e}")
output()

from unicodedata import decimal

# randomモジュールのchoice関数は配列からランダムに要素を取得
# 三項演算子
import random
bools = [True, False]
res = random.choice(bools)
print("answer" if res else "miss")

# typeはデータ型のオブジェクトを返してくれる
# __name__でデータ型の文字列を返してくれる
print(type({1: "first", 2:"two", 3:"three"}))
print(type(True).__name__)