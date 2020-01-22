from slackbot.bot import respond_to
import pandas as pd
import re
import random
import unicodedata

eki = pd.read_excel('wor_dict.xlsx', header=1)
eki = eki.dropna(subset=['読み'])
word_list = eki.groupby('読み')['読み'].count()
first_list = list(pd.Series(word_list.index.values, word_list.values))
w_list = list(pd.Series(word_list.index.values, word_list.values))
history = [w_list[0]]
flag = False
last_word = w_list[0]

SMALL_TO_NORMAL = {
    'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お',
    'っ': 'つ',
    'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ',
}
def small2large(a):
    if a in SMALL_TO_NORMAL:
        return SMALL_TO_NORMAL[a]
    else:
        return a
print('load finished!')
@respond_to(r'.*')
def siritori_func(message):
    global flag
    global last_word
    re_hiragana = re.compile(r'^[あ-ん]+$')
    status_hira = re_hiragana.fullmatch(message.body['text'])  # fullmatch:完全一致
    if status_hira:
        if message.body['text'] == 'しりとり':

            message.reply('しりとりを開始するよ！\n駅名をひらがなで入力してね。同じ駅名は２回以上使用してはならないよ！\n最初の単語は：\n' + last_word)
            w_list.remove(last_word)
            flag = True
        if flag:
            if message.body['text'] in first_list:
                if message.body['text'] in history:
                    message.reply('それはもう使った単語だよ！')
                else:
                    if message.body['text'][0] != last_word[-1]:
                        message.reply(last_word[-1]+"から始まる駅名を答えてね")
                    else:
                        history.append(message.body['text'])
                        w_list.remove(message.body['text'])
                        last_spell = small2large(unicodedata.normalize("NFKD", message.body['text'][-1])[0])
                        rep_list = [word for word in w_list if word[0] == last_spell]
                        if len(rep_list) >= 1:
                            last_word = random.choice(rep_list)
                            message.reply('次の駅名は：'+last_word)
                            history.append(last_word)
                            w_list.remove(last_word)
                        elif len(rep_list) == 0:
                            message.reply('もう知ってる駅名ないや！\n僕の負けだね。。おめでとう！')
                        if message.body['text'][-1] == 'ん':
                            message.reply('「ん」がついたから君の負けだよ！')
            elif last_word == 'あいおい':
                pass
            else:
                message.reply("その駅は知らないな～。\n別の駅を探してみて！")
    elif message.body['text'] == 'exit':
        message.reply("しりとりを終えるよ。お疲れ様～")
        return 0
    else:
        message.reply("平仮名で駅名を入力してね～")



