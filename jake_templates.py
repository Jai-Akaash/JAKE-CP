class DisJointSet :
	def __init__(self,n):
		self.rank =  [0 for _ in range(n + 1)]
		self.parent = [i for i in range(n + 1)]
	def FindParent(self,Node):
		if self.parent[Node] == Node:
			return Node
		self.parent[Node] = self.FindParent(self.parent[Node])
		return self.parent[Node]
	def unionByRank(self,u,v):
		Upu = self.FindParent(u)
		Upv = self.FindParent(v)
		if self.rank[Upu] > self.rank[Upv]:
			self.parent[Upv] = Upu
		elif self.rank[Upu] < self.rank[Upv]:
			self.parent[Upu] = Upv
		else:
			self.parent[Upv] = Upu
			self.rank[Upu] += 1
g = DisJointSet(5)
g.unionByRank(1,2)
g.unionByRank(3,4)
print(g.FindParent(1),g.FindParent(2),g.FindParent(5))
