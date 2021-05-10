class Student1:  # 数学と英語の点数の平均を計算するメソッド

    def __init__(self):  # コンストラクタ（初期かメソッド）
        self.name = ""  # ””は空の値を代入している

    def avg(self, math, english):  # メソッドの場合は引数は最低１つは必要、なので渡したい引数がない場合を考慮して必ずselfと入力する
        print((math + english)/2)


person1 = Student1()  # 変数(person1)にインスタンス(Student())を代入してインスタンスとして使えるようになった
person1.name = "sato"
print(person1.name)  # 未定義のアトリビュートはエラーになる

person2 = Student1()
person2.name = "tanaka"
print(person2.name)

# アトリビュートはインスタンス化と同時に代入することができる


class Student2:  # 数学と英語の点数の平均を計算するメソッド

    def __init__(self, name):  # コンストラクタ（初期かメソッド）
        self.name = name  # ””は空の値を代入している

    def avg(self, math, english):  # メソッドの場合は引数は最低１つは必要、なので渡したい引数がない場合を考慮して必ずselfと入力する
        print((math + english)/2)


# 変数(person1)にインスタンス(Student())を代入してインスタンスとして使えるようになった
person1 = Student2("sato")
print(person1.name)  # 未定義のアトリビュートはエラーになる

person2 = Student2("tanaka")
print(person2.name)
