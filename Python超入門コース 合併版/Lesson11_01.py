for i in range(5): #rangeの範囲内で繰り返す
    print(i)


for i in range(5):
    if i == 3:
        break #ある条件で停止する
    print(i)


for i in range(5):
    if i == 3:
        continue  #ある条件をスキップして続ける
    print(i)


for i in range(3):
    for j in range(3):
        print(i, j, sep="-")  # sep引数をハイフンにすることでわかりやすくする
