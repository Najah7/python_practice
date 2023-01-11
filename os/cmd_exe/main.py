import os
import subprocess

# NOTE:現在非推奨↓
os.system('ls')

# 現在推奨↓
subprocess.run(['ls', '-al'])

# exe in shell
# これだとパイプが使える。しかしshell injectionの危険性には注意。
subprocess.run('ls -al | grep test', shell=True)

# 安全にパイプ機能を使う方法:popenを使う
# NOTE:popenとはプロセスへのファイルポインタをオープンするもの
#       サブプロセスを実行し、そのプロセスの標準入出力との間にパイプラインを確立
#       使い方はファイルのポインタを扱う感じでIOオブジェクトを返す。
process1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['grep', 'test'], stdin=process1.stdout, stdout=subprocess.PIPE)

process1.stdout.close()

print(process2.communicate()[0])
