class Favorite:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"{self.name}が好きです")

# key: value型配列（オブジェクト、ディクショナリー型）
animes = {
    "one": "キングダム",
    "two": "ワンピース",
    "three": "サイコパス",
    "four": "コナン",
    "five": "ハンターハンター",
    "six": "鬼滅の刃",
    "seven": "東京リベンジャーズ"
}

# key-value型配列の要素の取り出し
kingdom = Favorite(animes["one"])
kingdom.introduce()

def doSomething(arg):
    print(arg)