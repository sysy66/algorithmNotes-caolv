# 字典树模板
# 676. 实现一个魔法字典


class Trie:
    def __init__(self):
        self.child = dict()
        self.is_finished = False
        
