#probleml ink-->> https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/


class Solution:
	def maxProduct(self, s: str) -> int:
		def create_string(v):
			res=[]
			for i in range(n):
				if 1<<i&v:
					res.append(s[i])
			if res==res[::-1]:
				pal[v]=len(res)
		pal=dict()
		n=len(s)
		for i in range(1,pow(2,n)):
			create_string(i)
		res=0
		for x in pal:
			for y in pal:
				if not x&y:
					res=max(res,pal[x]*pal[y])
		return res
