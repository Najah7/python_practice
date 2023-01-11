import tempfile

# コンテクスマネージャーで勝手に削除してくれる

def main():
    # tmp file
    with tempfile.TemporaryFile(mode='w+') as tmp:
        tmp.write('test')
        tmp.seek(0)
        print(tmp.read())
        
        
    # tmp dir
    with tempfile.TemporaryDirectory() as tmp_dir:
        print(tmp_dir)
        
if __name__ == '__main__':
    main()