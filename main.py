import yaml

CONFIG_FILE =  './config.yml'


def main():
  with open(CONFIG_FILE, 'r') as yml:
    config = yaml.safe_load(yml)

  print('hello world')
  print(config)

if __name__ == '__main__':
  main()
