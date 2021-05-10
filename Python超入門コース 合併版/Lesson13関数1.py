def say_hello(greeting):
    print(greeting)  # 受け取った引数をprint関数で表示させる


hello = say_hello
hello("Good Morning")


def add(num01, num02):
    print(num01 + num02)


add(6, 2)


def add(num01, num02):
    return(num01 + num02)


print(add(6, 2))

add_result = add(6, 2)
print(add_result)
