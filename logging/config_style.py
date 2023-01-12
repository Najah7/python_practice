import logging

logger = logging.getLogger(__name__)

# just massage
logger.error('something wrong')

# JSON style
#　NOTE:キーバリューの方が検索性が高かったり、分析、解析などに向くことがる
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'something worong'
})

