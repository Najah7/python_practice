import logging.config

# NOTE:シンプルにキー＆バリューで指定するパターン。
# わかりやすく分離できるのは良い点、pythonと違う形式になるのは考慮点
# 個人的にはJSON形式に親しみがあるからdictがいいかも

def main():

    # You can chose to read config info from file(True) or dict(False)
    READ_FILE = True

    if READ_FILE:
        logging.config.fileConfig('logging.ini')
    else:
        logging.config.dictConfig({
            'version':1,
            'formatters':{
                'sampleFormatter':{
                    'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
                }
            },
            'handlers': {
                'sampleHandlers': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'sampleFormatter',
                    'level': logging.DEBUG
                }
            },
            'root': {
                'handlers': ['sampleHandlers'],
                'level': logging.WARNING,
            },
            'loggers': {
                'simpleExample': {
                    'handlers': ['sampleHandlers'],
                    'level': logging.DEBUG,
                    'propagate': 0
                }
            }
        })

    logger = logging.getLogger('simpleExample')


    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    
if __name__ == '__main__':
    main()