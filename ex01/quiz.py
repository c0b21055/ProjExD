import random
# 問題の作成
quizzes = {}
quizzes['問題1'] = {'問題文':'サザエの旦那の名前は?',  '正解':['ますお','マスオ']}
quizzes['問題2'] = {'問題文':'カツオの妹の名前は？', '正解':['わかめ','ワカメ']}
quizzes['問題3'] = {'問題文':'タラオはカツオから見てどんな関係？', '正解':['甥','おい','甥っ子','おいっこ']}

# 出題 ランダムに選択
key, value = random.choice(list(quizzes.items()))
print(key, value['問題文'])

# 解答
answer = input('答えるんだ :')


if  answer in (value['正解']):
    print('正解！')
else:
    print("出直してこい")