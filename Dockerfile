FROM python:3.6

WORKDIR /usr/src/app
# ソースコードを格納する
COPY src ./

# ライブラリのインストール
RUN pip install -r requirements.txt

# Pythonを実行する

ENTRYPOINT ["python", "run.py"]