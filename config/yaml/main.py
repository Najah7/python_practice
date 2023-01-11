import yaml

#NOTE:defalt_flow_styleをFalseにすることでいつも見慣れたyamlファイルの形式になる。


def main():
    # 書き込み
    with open('output.yml', 'w') as yaml_file:
        yaml.dump({
            'web_server': {
                'host': '127.0.0.0',
                'port': '80'
            },
            'db_server': {
                'host': '127.0.0.0',
                'port': '3306'
            }
        }, yaml_file, default_flow_style=False)
        
    #　読み込み
    with open('output.yml', 'r') as yaml_file:
        data = yaml.load(yaml_file)
        print(data)
        
if __name__ == '__main__':
    main()