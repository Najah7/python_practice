import tempfile

# コンテクスマネージャーで勝手に削除してくれる

# tmp file
with tempfile.TemporaryFile(mode='w+') as tmp:
    tmp.write('test')
    tmp.seek(0)
    print(tmp.read())
    
    
# tmp dir
with tempfile.TemporaryDirectory() as tmp_dir:
    print(tmp_dir)