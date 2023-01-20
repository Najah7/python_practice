from pathlib import Path
import os
from glob import glob

def main():
    
    # try:
    #     os.remove('README.md')
    # except: pass
    
    files = os.listdir()
    
    # print(files)
    
    dirs = list()
    
    for file in files:
        if os.path.isdir(file):
            dirs.append(file) 
    
    exclude_dirs = [
        '.git',
        'text_to_html',
        'draw_image',
    ]

    for ex_dir in exclude_dirs:
        if ex_dir in dirs:
            dirs.remove(ex_dir) 
    
    print(dirs)
    
    title = '# Pythonの練習に色ろなモジュールを使ってみた'
    
    with open('README.md', 'w') as file:
        file.write(title+ '\n')
        for i in range(len(dirs)):
            file.write(f'- {dirs[i]}：{dirs[i]}関係のモジュールを使ってみた\n')
    


if __name__ == '__main__':
    main()