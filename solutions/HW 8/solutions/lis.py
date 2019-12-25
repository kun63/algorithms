__author__ = "Zhang, He"

from collections import defaultdict 
def lis(s):
	a = [float("-inf")] + list(s) + [float("inf")]
	n = len(a)
	d = defaultdict(int)
	back = defaultdict(lambda: -1)
	trackmax, indexmax = 0,0
	for j in range(1,n):
		for k in range(j):
			if a[k] < a[j] or a[j] == float("inf"):
				temp = d[k] + 1 
			if temp > d[j]:
				d[j] = temp
				back[j] = k
		if j<n-1 and d[j] > trackmax:
			trackmax = d[j]
			indexmax = j
	return solution(indexmax,a,back)

def solution(i,a,back):
	if i < 1:
		return ""
	return solution(back[i],a,back) + str(a[i])

if __name__=="__main__":
	print(lis("aebbcg"))
	print(lis("zyx"))
	print(lis("1234567890"))
