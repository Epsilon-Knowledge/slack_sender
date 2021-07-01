import yaml
import argparse

CONFIG_FILE =  './config.yml'

def main():

    # configファイルの読み込み
    with open(CONFIG_FILE, 'r') as yml:
      config = yaml.safe_load(yml)

    print('hello world')
    print(config)

  # 引数の指定
    parser = argparse.ArgumentParser()
    parser.add_argument("mail_body", help = "the body of mail you want to transfer to slack.")
    args = parser.parse_args()

    print(args.mail_body)

if __name__ == '__main__':
    main()
