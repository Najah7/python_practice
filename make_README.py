from pathlib import Path
import os
from glob import glob

def main():
    
    try:
        os.remove('README.md')
    except: pass
    
    files =glob(f'{Path(__file__).parent}/*')
    
    files = [file.replace('./', '') for file in files]
    
    title = '# Pythonの練習に色ろなモジュールを使ってみた'
    
    with open('README.md', 'w') as file:
        file.write(title+ '\n')
        for i in range(len(files)):
            file.write(f'- {files[i]}：{files[i]}関係のモジュールを使ってみた\n')
    


if __name__ == '__main__':
    main()