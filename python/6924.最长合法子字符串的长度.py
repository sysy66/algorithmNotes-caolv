# 6924.最长合法子字符串的长度.py
# https://leetcode.cn/problems/length-of-the-longest-valid-substring/description/
# lang=python

# 解法：字典树的简单应用+双指针


class Trie:
	def __init__(self):
		self.a = {}
		self.is_finished = False


class Solution:
	def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
		root = Trie()

		for word0 in forbidden:
			cur = root
			for ch in word0:
				if ch not in cur.a:
					cur.a[ch] = Trie()
				cur = cur.a[ch]
			cur.is_finished = True

		ans = 0
		left = right = len(word)
		while True:
			ans = max(ans, right - left)
			left = ptr = left - 1
			if left == -1:
				break
			cur = root
			for i in range(left, right):
				if word[i] not in cur.a: break
				cur = cur.a[word[i]]
				if cur.is_finished:
					right = ptr
					break
				ptr += 1

		return ans


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(word="cbaaaabc", forbidden=["aaa", "cb"]))
	# 输出：4
	print(func(word="leetcode", forbidden=["de", "le", "e"]))
	# 输出：4

	t_1 = time.time()
	print(t_1 - t_0)

