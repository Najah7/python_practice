import logging

import logger

""" NOTE:logのレベル
1. CRITICAL
2. ERROR
3. WARNING
4. INFO
5. DEBUG
※上の方が重要度が高い。

pythonのデフォルトのログレベルはWARNING。
なので、設定を変えない場合はWARING以上しか出力されない

"""

def main():
    
    # You can change level into debug
    CHANGE_LEVEL = True 
    
    if CHANGE_LEVEL:
        logging.basicConfig(level=logging.DEBUG, filename='output.log')
        
    logging.critical('critical')
    logging.error('error')
    logging.warning('warnig')
    logging.info('info')   
    logging.debug('debug')
    
    # configの特殊な記法。「'string %s %s' % (val1, val2)」の拡張
    # but 基本的にf-stringでOK
    logging.warning('warnig %s %s', 'test', 'test')
    
    # loggingのformatで使える変数の例
    # 詳しくはhttps://docs.python.org/3/library/logging.html?highlight=logging#module-logging
    format1 = '%{levelname}s:%{message}s'
    logging.basicConfig(format=format1)
    
    logger.output_log2()
    
    
    
    
    
    

if __name__ == '__main__':
    main()