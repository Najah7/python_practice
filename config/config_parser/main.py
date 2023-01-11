import configparser


def main():
    #NOTE: MySQLなどのコンフィグに使う書式（詳しくはoutput_config.iniを参照）
    config = configparser.ConfigParser()

    config['DEFAULT'] = {
        'debug': True
    }

    config['web_server'] = {
        'host': '127.0.0.1',
        'port': 80,
    }

    config['db_server'] = {
        'host': '127.0.0.0',
        'port': '3306'
    }

    # 書き込み
    with open('output.ini', 'w') as config_file:
        config.write(config_file)
        
    # 読み込み
    config2 = configparser.ConfigParser()

    config2.read('output.ini')
    print(config2['web_server']['host'])
    
if __name__ == '__main__':
    main()