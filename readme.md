# slack_sender

## 概要

標準入力で受け取ったメールを整形し、Slack webhook APIを使用してSlackに投稿するスクリプトである。

## 前提条件

python3系が導入されていること。

requirements.txtのパッケージがインストールされていること。

## 使い方

### 送信先の設定

`config.yml` - `API_URL`にSlack Incoming Webhookで発行したAPI URLを記載する。

- API URLの発行方法は以下を参照する。

- - https://qiita.com/ik-fib/items/b4a502d173a22b3947a0
  - https://api.slack.com/messaging/webhooks

### 送信コマンド

スクリプトなどで実行する場合は以下のようなコマンドを実行する。

```
# echo版
echo "some message you'd like to send" | python main.py

# cat版
cat << EOF | python main.py
some message1
some message2
some message3
EOF
```

postfixの`/etc/aliases`でメールを標準入力としてコマンドにわたすことが可能である。  
これを利用するには`/etc/aliases`で以下のように記載する。

```
# rootのメールをslackに送る
root: '| python main.py'
```

なお`python`コマンドは後述の環境で作った場合、`. /path/to/activate`を実行するか`python` → `/path/to/python`に置き換えること。

## venv+pipによるslack_sender用python環境構築方法

OSはUbuntu Focal Fossaとする。  
apt以外はCentOS系でも同じなので参考にする。

```
対象サーバーにログインし、rootユーザーにスイッチする。
date && uname -n && id

# リポジトリをクローン
cd /usr/local/ && pwd
git clone https://github.com/Epsilon-Knowledge/slack_sender.git

# pythonインストール
apt install -y python3
dpkg -l python3

# venv環境を作る
python3 -m venv /usr/local/venv/slack_sender
ll /usr/local/venv/slack_sender/bin

# pipアップデート
/usr/local/venv/slack_sender/bin/pip list
/usr/local/venv/slack_sender/bin/pip install -U pip
/usr/local/venv/slack_sender/bin/pip list

# 必要なパッケージをインストール
/usr/local/venv/slack_sender/bin/pip install -r /usr/local/slack_sender/requirements.txt
/usr/local/venv/slack_sender/bin/pip list

# テスト時など`python`と実行したときに自動でvenvで作成したpythonが使われるようにしたいときは以下のコマンドを実行する。
# . /usr/local/venv/slack_sender/bin/activate

# スクリプトに仕込むとき等、直接python仮想環境のpythonコマンドを実行するときは以下のように実行する。
# /usr/local/venv/slack_sender/bin/python /usr/local/slack_sender/main.py

```





