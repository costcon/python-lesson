class Student:  # 数学と英語の点数の平均を計算するメソッド
    def avg(self, math, english):  # メソッドの場合は引数は最低１つは必要、なので渡したい引数がない場合を考慮して必ずselfと入力する
        print((math + english)/2)


person1 = Student()  # 変数(person1)にインスタンス(Student())を代入してインスタンスとして使えるようになった

person1.avg(30, 70)

# アトリビュートについて

person1.name = "sato"

print(person1.name) #未定義のアトリビュートはエラーになる

# person2 = Student()
# print(person2.name)

#上記だとエラー発生する。アトリビュートはインスタンスごとに必要
#その不便さを解消するのがコンストラクタ(初期かメソッド)・・・インスタンス化する時に自動的に実行されるメソッド
#そのため後から使うアトリビュートは初期かメソッドで自動的に作っておけばいい

