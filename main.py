import yaml
import argparse
import sys
import models
import email

CONFIG_FILE =  '/usr/local/slack_sender/config.yml'

def main():

    # 引数の指定
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help = 'debug mode', action = 'store_true')
    args = parser.parse_args()

    # configファイルの読み込み
    with open(CONFIG_FILE, 'r') as yml:
      config = yaml.safe_load(yml)


    # 標準入力を受け取り
    stdin = sys.stdin.read()

    # DEBUG
    # print('stdin: ' + stdin)

    # # DEBUG
    # print('arguments: ' + str(args.d))
    msg = email.message_from_string(stdin)
    print(type(msg))
    print(msg.get('Date'))
    print(msg.get('Return-Path'))
    print(msg.get('From'))
    print(msg.get('Subject'))
    #print(msg.items())
    print(msg.get_payload(decode = False))


    # 本文を作成

    # slackに送信


if __name__ == '__main__':
    main()
