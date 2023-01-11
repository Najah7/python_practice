import sys

"""
基本的なファイルの操作

NOTE:mode=[w, a, r, r+, w+, a+, t, b]
※「+」のついているのは読み書き（挙動の順番が違うだけ）
※t:テキスト, b:バイナリ

"""

def main():
    # 書き込み
    with open('test.txt', 'w') as f:
        f.write('test\n')
        print('output used by print function', file=f)
        
    print_message('読み込み（すべて）') 
    
    with open('test.txt', 'r') as f:
        text = f.read()
        print(text)
        
    print_message('読み込み（一行ずつ）')
    
    with open('test.txt', 'r') as f:
        while True:
            line = f.readline()
            print(line)
            if not line: break
            
    print_message('読み込み（指定の文字数ずつ）')
    
    with open('test.txt', 'r') as f:
        chunk = 5
        while True:
            word = f.read(chunk)
            print(word)
            if not word: break
            
    print_message('seekを使った移動系')
    
    """
    下記に示したものは、あえて長い変数名にした。自分の可読性ベースで
    
    NOTE:seekはディスクのシークが由来している。（本来はメモリ形に格納されていたとしても、意識する必要なし）
    """
    
    with open('test.txt', 'r') as f:
        print(f.tell()) # Tell me where I am now.
        
        n_char_I_wanna_read = 3
        print(f.read(n_char_I_wanna_read))
         
        n_char_I_wanna_move = 2
        f.seek(n_char_I_wanna_move)
        print(f.tell())
        print(f.read(n_char_I_wanna_read))


def print_message(message):
    print(f'===={message}====')        
        
if __name__ == '__main__':
    main()

