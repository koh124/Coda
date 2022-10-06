class Drink:
    def __init__(self, name, ):
        self.name = name

    def pour(self):
        print(self.name + "を注ぎました")

orange_juice = Drink("オレンジジュース")
orange_juice.pour()

class Coffee:
    def __init__(self, name, ):
        self.name = name

    def pour(self):
        print(self.name + "を注ぎました")

coffee = Drink("アメリカンコーヒー")
coffee.pour()