import yaml
import argparse
import sys
import models
from logging import getLogger, basicConfig

CONFIG_FILE =  '/usr/local/slack_sender/config.yml'

def main():

    try:
        # 引数の指定
        # parser = argparse.ArgumentParser()
        # parser.add_argument('-d', help = 'debug mode', action = 'store_true')
        # args = parser.parse_args()
        #print(args.d)

        # configファイルの読み込み
        with open(CONFIG_FILE, 'r') as yml:
          config = yaml.safe_load(yml)

        # ログの開始
        basicConfig(filename = config['LOG_FILE'], format='%(asctime)s [%(levelname)s]: %(message)s')
        logger = getLogger(__name__)

        # 標準入力を受け取り
        stdin = sys.stdin.read()

        slack_message_data = models.NotificationData(stdin, config['DEBUG_MODE'], config['API_URL'])

        # 本文を作成
        # slackに送信
        slack_message_data.send_slack()

    except Exception as e:
        logger.exception("Some problems have happened.")


if __name__ == '__main__':
    main()
