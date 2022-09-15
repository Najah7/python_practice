import sys
import sys
import re

import handlers
import util
import rules

class Parser:
    """
    Parserはテキストファイルを読み込み、ルールの適用とハンドラの制御を行う。
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
        
    def parse(self, file):
        self.handler.start('document')
        for block in util.blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')
        
class BasicTextParser(Parser):
    """
    コンストラクタ内でルールとフィルタを追加する特定目的のParser

    Args:
        Parser (_type_): _description_
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(rules.ListRule())
        self.addRule(rules.ListItemRule())
        self.addRule(rules.TitleRule())
        self.addRule(rules.HeadingRule())
        self.addRule(rules.ParagraphRule())
        
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(https://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = handlers.HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
