import random
import string
import time


all_alp=26
random_alp1=10
random_alp2=8
dell=2

random_list = [random.choice(string.ascii_uppercase) for all_alp in range(random_alp1)]
random_chr = "".join(random_list)

print("対象文字：")
print(random_chr)

time_sta = time.time()

print("表示文字：")

new_random=random.sample(random_list, random_alp2)
print(new_random)

ans=input("欠損文字はいくつあるでしょうか？：")

if int(ans)==dell:
    print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
    cha1=input("1つ目の文字を入力してください：")
    cha2=input("2つ目の文字を入力してください：")

    time_end = time.time()
    times=time_end-time_sta

    if (cha1 and cha2) in random_list:
        if (cha1 or cha2)  in new_random:
            print("不正解です。またチャレンジしてください。")
        else:
            print("正解です")
            print(f"タイムは{times}です。")
            


else:
    print("不正解です。またチャレンジしてください。")

