import datetime
import time

# NOTE:datetimeはログファイルの名前でよく使う。

# get what time is now
now = datetime.datetime.now()

today = datetime.date.today()


# NOTE:formatについて詳しく：https://docs.python.org/ja/3/library/datetime.html
print(now.isoformat())
print(today)
print(now.strftime('%Y年%m月%d日%H時%M分%S秒%fミリ秒'))

# make datetime object
time_obj = datetime.time(hour=6, minute=30, second=0)

print(time_obj.isoformat())

# calculate datetim object
week = datetime.timedelta(weeks=1, days=3, hours=12, seconds=60, microseconds=1)


print(now - week)

# take pause
time.sleep(2)
print('hello')

# get epoch seconds
print(time.time())