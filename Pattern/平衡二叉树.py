class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True  # 特判

        st = collections.deque([])  # 准备迭代的栈
        seen = collections.defaultdict(int)  # 标记每个节点已经取过的子节点
        rank = collections.defaultdict(int)  # 记录每个节点的高度

        node = root  # 初始，从root开始
        while st or node:
            while node:
                st.append(node)  # 把手上的节点挂起来先~
                if not node.left and not node.right:  # 如果他没有子节点，直接打破循环
                    break
                if node.left:  # 如果没有打断，就是有子节点，从左边开始（如果左子节点存在的话）
                    seen[node] = 1  # 标记左子节点已经取过，下一次取右边
                    node = node.left
                else:
                    seen[node] = 2  # 标记一下
                    node = node.right  # 如果没有左节点，那就取右边。。。
            node = st[-1]  # 从栈取最后入栈的节点
            if seen[node] == 1:  # 如果是之前没有加入过字典的节点，seen[node]默认是0，所以会跳到下面else
                seen[node] += 1  # 如果seen[node]是1，说明这个节点已经取过左边。现在把标记改一下，+1
                node = node.right  # 现在取右边，右边存在，就没问题，继续迭代。
                # 如果右边不存在，那么node变成None，再次进入循环会跳过第一阶段，然后从栈里再取一个节点。
            else:
                if abs(rank[node.left] - rank[node.right]) > 1: return False  # 走到这里，说明此节点的子节点全部取过了。
                                                                        # 判断一下两子节点的高度差，如果大于1，返回false。
                rank[node] = max(rank[node.left],rank[node.right]) + 1  # 记录此节点的高度，此节点的高度等于两子节点的最大值+1，
                                                                        # 如果子节点不存在，默认rank[None]是等于0的
                  # 弹出此节点
                del seen[st.pop()]
                node = None  # 手上节点记为空，进入下一个循环。或者栈此时也是空的，跳出循环。
        return True  # 穷尽了每一个节点，都没有返回false，说明是完全平衡树