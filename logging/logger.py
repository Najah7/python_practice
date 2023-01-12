import logging

# logger
# NOTE:基本的に使うのはlogger。
#       どこか一か所で基本的なloggingの設定をして
#       その設定を使ってインスタンス化したloggerをそれぞれでカスタムして使うのが一般的


def main():
    # __name__を使うことが多い。
    # なぜなら違うファイルで呼び出したときにログにわかりやすく表示されるから

    # 歴史的な背景でlogger関係の関数（ex)getLogger()）はキャメルケースを使うことが多い（違う会社が作ったらしい？？）

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.WARNING)

    # handlerの例
    # 下記はファイルに書きこむハンドラ。（ログのハンドラーはログが発生がイベント）
    # ハンドラを設定しない場合StreamHandlerが設定されているの思う（なぜなら標準出力に出力されるから）
    # ハンドラーの種類詳しくはhttps://docs.python.org/3/library/logging.handlers.html?highlight=logging%20handler#module-logging.handlers
    file_handler = logging.FileHandler('output2.log')

    logger.addHandler(file_handler)

    # filterの例
    class NoPassFilter(logging.Filter):
        def filter(self, record):
            # getMessage():ログのメッセージを取得するメソッド
            message = record.getMessage()
            return 'password' not in message

    # オブジェクト化して渡す
    logger.addFilter(NoPassFilter())

    def output_log2():
        logger.error('error from logger1')
        logging.error('error from logger2')
        # filterが適用されてるかのチェック
        logger.error('error with password')

if __name__ == '__main__':
    main()