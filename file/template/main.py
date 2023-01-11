import string

def main():
    """
    Please chose your template file.
    
    You can write $ befor a word to use variable in your template file.
    
    """
    
    file_name = input('template file: ')
    
    with open(file_name) as f:
        strings = f.read()

    template = string.Template(strings)
    
    # TODO:テンプレートファイルから変数を抽出することで、変数の内容も対話型で決めるように。
    
    contents = template.substitute(name='trou', content='welcome to my site')

    print(contents)
    
if __name__ == '__main__':
    main()