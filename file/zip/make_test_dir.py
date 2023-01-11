import os
import pathlib
import shutil

file_paths = ['tests/test.txt', 'tests/test2.txt']

os.mkdir('tests')

pathlib.Path(file_paths[0]).touch()

shutil.copy(file_paths[0],
            file_paths[1]
            )


for i in range(2):
    with open(file_paths[i], 'w') as f:
        f.write(f'this is test{i+1}')
        
