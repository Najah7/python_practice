import os
#NOTE:path library
import pathlib
#NOTE:global commandの略　詳しくは：https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%AD%E3%83%96
import glob
#NOTE:shell utilityの略
import shutil

# TODO:テスト用のファイルをの作成の自動化
# TODO:上記に加えてランダムなテストデータの作成も（コマンド判断）


def main():
    # make file
    with open('test.txt', 'w') as f:
        f.write('test')

    # ====os====

    print(os.getcwd())

    # returun bool     
    print(os.path.exists('test.txt'))
    print(os.path.isfile('test.txt'))
    print(os.path.isdir('file'))

    #rename
    os.rename('test.txt', 'renamed_test.txt')

    #link
    os.symlink('renamed_test.text', 'symlink')
    os.link('renamed_test.txt', 'hardlink')

    os.remove('symlink')
    os.remove('hardlink')
    os.remove('renamed_test.txt')

    os.mkdir('test_dir')
    os.mkdir('test_dir/test2_dir')
    print(os.listdir('test_dir'))


    # pathlib
    # pathlib.Path('empty.txt').touch()
    pathlib.Path('test_dir/test2_dir/empty.txt').touch()

    #shutil
    shutil.copy('test_dir/test2_dir/empty.txt',
                'test_dir/test2_dir/empty2.txt'
                )

    # glob
    print(glob.glob('test_dir/test2_dir/*'))
    shutil.rmtree('test_dir')
    
if __name__ == '__main__':
    main()


