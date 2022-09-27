import random
import string
import time


cha1=26
cha2=10
cha3=8
cha4=2

random_list = [random.choice(string.ascii_uppercase) for cha1 in range(cha2)]
random_chr = "".join(random_list)

print("対象文字：")
print(random_chr)

time_sta = time.time()

print("表示文字：")
cha5=random.sample(random_list, cha3)
print(cha5)

ans=input("欠損文字はいくつあるでしょうか？：")

if int(ans)==cha4:
    print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
    cha6=input("1つ目の文字を入力してください：")
    cha7=input("2つ目の文字を入力してください：")

    time_end = time.time()
    times=time_end-time_sta

    if (cha6 and cha7) in random_list:
        if (cha6 or cha7)  in cha5:
            print("不正解です。またチャレンジしてください。")
        else:
            print("正解です")
            print(f"タイムは{times}です。")
            break


else:
    print("不正解です。またチャレンジしてください。")

