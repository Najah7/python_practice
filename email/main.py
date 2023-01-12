from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import os

from dotenv import load_dotenv
load_dotenv()

# Gmailのメール送信の簡単なプログラミング

# NOTE: Googleのアプリ（メール、カレンダ、連絡先、Youtubeなど）を使う場合はアプリパスワードを取得して、
#       それをパスワードとして使い認証する（smtplib.SMTP.login(account, pass)）
#       取得方法は簡単でgoogleの設定の「セキュリティ」の項目にある

# NOTE:今回は扱わなかったがOutlookを使う場合はwin32comというモジュールが必要みたい


# 自分のGmailから自分のGmailにメールを送った例

# メールに使う情報
smtp_host = 'smtp.gmail.com'
smtp_port = 587 # 推奨のSMTPサーバのポート（https://kinsta.com/jp/blog/smtp-port/）
from_email = os.getenv('MY_EMAIL')
to_email = os.getenv('MY_EMAIL')
account = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')
# charset = 'iso-2022-jp'

# メールオブジェクトの作成＋必要事項の設定
msg = MIMEMultipart()
msg['subject'] = 'Test email'
msg['From'] = from_email
msg['To'] = to_email

# add plain text
msg.attach(MIMEText('test with attached file', 'plain'))

# add attached file
with open('test.txt', 'r') as f:
    attachment = MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition',
        'attachment',
        filename='test.txt')
    msg.attach(attachment)

# add image
with open('NYC_times_square.png', 'rb') as image_file:
    img = image_file.read()
    image = MIMEImage(img, name='NY photo')
    msg.attach(image)
    

    
server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(account, password)
server.send_message(msg)
server.quit()