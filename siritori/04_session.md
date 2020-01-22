# セッション4
## BOTの中身を準備しよう

### アプリケーションの作成
1. セッション1を参考に、以下の名称でアプリケーションを作成

```
プロジェクト名「SiritoriBotProject」
```

2．プロジェクトの直下に「run.py」、「slackbot_settings.py」を作成し、それぞれ以下のように記述

- run.py

```
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()
```

- slackbot_settings.py

```
# BOTアカウントのAPIトークンを設定
API_TOKEN = "{自分のAPIトークンを入力}"

# どの応答にも当てはまらない場合に返すメッセージを設定
DEFAULT_REPLY = "{好きなメッセージを入力}"

# プラグインスクリプトを置いてあるサブディレクトリ名を設定
PLUGINS = ['plugins']
```

3. プロジェクトの直下に「plugins」というディレクトリを作成
4. pluginsの配下に「` __init__.py `」と「reply.py」を作成

- ` __init__.py `

```
# 中身は空
```

- reply.py

```
from slackbot.bot import respond_to

@respond_to('しりとり')
def siritori_func(message):
    message.reply('今日はやりません')
    
```

### アプリケーションの起動
1. プロジェクトウィンドウ上でrun.pyを選択して右クリック→実行
2. 実行ウィンドウが表示され、start slackbotが表示されたことを確認

### セッションのまとめ
- requirements.txtのことを覚えてましたか？
- 次のセッションで実際に動くか試してみよう

### 参考
- [PyCharm - 公式ヘルプ](https://pleiades.io/help/pycharm/managing-dependencies.html)