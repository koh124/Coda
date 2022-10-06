# 文法
print(1 == 2)     # 合同演算式は"=="
print(1 != 3)     # not equal

# is文法はイコール演算子のような役割を果たす
a = 1
b = 1
print(a is b)     # True
c = 0
d = 1
print(c is d)     # False

# 厳密な型どうしの比較を行っている
print(1 == '1')     # False
print(0 == '0')     # False
print(0 == '')      # False
print(0 == False)     #論理型と数値の10の比較は成立する True
print(1 == True)      #True

# None型というものがある模様
print(None)           # None
print(0 == None)      # False

# 1と0は2値論理型の関係が成立するようになっている模様（すべてTrue）
# 当然、1⇒True, 0⇒Falseに対応させても成立する
print(not 0 == 1)
print(not 1 == 0)
print(not (not 0) == 0)     # 否定の否定が真に戻る
print(not (not 1) == 1)

# ただし、0の否定に関しては1以外の色んな真値と一致する模様
print(not 0 == 2)
print(not 0 == '2')

# 0と文字型の比較は成立しないくせに
print(0 == 'string')      # False

# not 1と文字列の比較はTrueらしい
print(not 1 == '1')       # True
print(not 1 == '0')       # True
print(not 1 == 'string')  # True

# 0の否定は様々な真値との比較を受け入れる模様
print(not 0 == 102)       # True
print(not 0 == '102')     # True