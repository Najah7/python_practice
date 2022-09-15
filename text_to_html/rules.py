
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
    
    type = 'heading'
    def condition(self, block):
        return not '\n' in block \
            and len(block) <= 70 \
            and not (block[-1] == ':' or block[-1] == '.' or block[-1] == '。')
            
class TitleRule(Rule):
    """
    表題とは文章の最初のブロックでかつ見出しであるもの。

    Args:
        Rule (_type_): _description_
    """
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
    """
    リスト項目とは「-」で始まるパラグラフ
    書式付けの処理の一環として、この「-」は削除する

    Args:
        Rule (_type_): _description_
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
    
class ListRule(Rule):
    """
    リストは、リスト項目ではないブロックとリスト項目の間から始まり、
    連続した項目の最後のモノが終わるところまで。

    Args:
        Rule (_type_): _description_
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        if not self.inside \
            and ListItemRule.condition(self, block):
                handler.start(self.type)
                self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    """
    パラグラフとは単に他のどのルールにも当てはまらないブロック

    Args:
        Rule (_type_): _description_
    """
    type = 'paragraph'
    def condition(self, block):
        return True