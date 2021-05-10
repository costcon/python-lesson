class Student:  # 数学と英語の点数の平均を計算するメソッド
    def avg(self):  # メソッドの場合は引数は最低１つは必要、なので渡したい引数がない場合を考慮して必ずselfと入力する
        print((80 + 70)/2)


person1 = Student()  # 変数(person1)にインスタンス(Student())を代入してインスタンスとして使えるようになった

person1.avg()

