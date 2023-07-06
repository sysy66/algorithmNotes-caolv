# 字典树
# 676. 实现一个魔法字典


class Trie:
    def __init__(self):
        self.is_finished = False
        self.child = dict()