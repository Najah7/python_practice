from msilib.schema import Condition
from turtle import Turtle


class Rule:
    """
    全てのルールの基底クラス
    
    自分note
      サブクラスがtypeを持つ必要あり
    """
    
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
    
class HeadingRule(Rule):
    """
    見出しとは、最長70字で、最終文字が「:」「.」「。」でない単一の行。

    Args:
        Rule (_type_): _description_
    """
    
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)