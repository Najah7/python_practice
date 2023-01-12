from pathlib import Path
import os
from glob import glob

def main():
    
    try:
        os.remove('README.md')
    except: pass
    
    files =glob(f'{Path(__file__).parent}/*')
    
    files = [file.replace('./', '') for file in files]
    
    exclude_files = ['make_README.py', 'text_to_html', 'draw_image']
    
    for file in files:
        for ex_file in exclude_files:
            if file == ex_file:
                files.remove(file) 
    
    title = '# Pythonの練習に色ろなモジュールを使ってみた'
    
    with open('README.md', 'w') as file:
        file.write(title+ '\n')
        for i in range(len(files)):
            file.write(f'- {files[i]}：{files[i]}関係のモジュールを使ってみた\n')
    


if __name__ == '__main__':
    main()