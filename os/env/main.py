import os 

from dotenv import load_dotenv
# 同じ階層から.envを探して読み込んでくれる。もしない場合は親ディレクトリに見つかるまでいく
load_dotenv()

def main():
    # もともと設定されている環境変数
    print(os.environ.get('PATH'))
    # 同じ階層の.envで設定した環境変数
    print(os.getenv('TEST'))
    

if __name__ == '__main__':
    main()