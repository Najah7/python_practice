"""
NOTE:tarfileのmodeの基本は[r, w, a, x(圧縮無し)]、基本の後に「:」を使って圧縮・展開方法を指定。\
    圧縮方法
    ・gz: gzip
    ・bz2: bzip2
    ・xz: lzma
        

"""
import glob
import os
import shutil
import tarfile
import zipfile


# TODO:コマンドで圧縮法の指定をできるようにする。

def main():
    # zip (tarfile)
    with tarfile.open('test.tar.gz', 'w:gz') as tar:
        tar.add('tests')
    
    # unzip (tarfile)
    with tarfile.open('test.tar.gz', 'r:gz') as tar:
        tar.extractall(path='dir')
    
    os.remove('test.tar.gz')
    shutil.rmtree('dir')
        
    #zip (zipfile)
    with zipfile.ZipFile('test.zip', 'w') as zip:
        for f in glob.glob('tests/*'):
            zip.write(f)
    
    # unzip
    with zipfile.ZipFile('test.zip', 'r') as zip:
        zip.extractall('dir')
    
    os.remove('test.zip')
    shutil.rmtree('dir')


if __name__ == '__main__':
    main()