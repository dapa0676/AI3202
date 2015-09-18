#Daniel Palmer

import sys

#global variables
openList = []
closedList = []
world = []
totalCost = 0
totalLocations = 1
heuristic = 0


for arg in sys.argv:
	with open(sys.argv[1], "r") as ins:
		for line in ins:
			world.append(line)
	if sys.argv[2] == 1:
		heuristic = 1
	elif sys.argv[2] == 2:
		heuristic = 2
	else:
		print "incorrect input"
		

        	
def manhattan (node):
	xRemaining = 9-node.x
	yRemaining = 7-node.y
	if heuristic == 1:
		total = xRemaining + yRemaining
	elif heuristic == 2:
		total = (sqrt(xRemaining*xRemaining+yRemaining+yRemaining))
	return total

def cost (node):
	cost = 0
	if world[node.x][node.y] == 0:
		cost = 10
	if world[node.x][node.y] == 0:
		cost = 20
	
class Node():
	def __init__(self,x,y,parentCostToStart):
		self.parent = None
		self.costToStart = parentCostToStart + cost(self)
		self.x = x
		self.y = y
		self.f = 0
		
def adjacent(world, node):
	adjacent = []
	for i in range(node.x-1,node.x+1):
		if (i >= 0) and (i < 10):
			if (node.y+1 >= 0) and (node.y+1 < 8):
				temp = Node(i,node.y+1,node.costToStart)
				adjacent.append(temp)
			if (node.y-1 >= 0) and (node.y-1 < 8):
				temp = Node(i,node.y-1,node.costToStart)
				adjacent.append(temp)
			
	if (node.x-1 >= 0) and (node.x-1 < 8): 
		temp = Node(node.x-1,node.y,node.costToStart)
		adjacent.append(temp)
	if (node.x+1 >= 0) and (node.x+1 < 10):
		temp = Node(node.x+1,node.y,node.costToStart)
		adjacent.append(temp)
	
	return adjacent
	
def isValid(x,y):
	isValid = True
	if x < 0 or x > 9 or y < 0 or y > 7 or world[x][y] == 2:
		isValid = False
	return isValid
	
def isDiagonal(node1, node2):
	diagonal = False
	if node2 in adjacent(world, node1):
		if node2.x != node1.x:
			if node2.y != node1.y:
				diagonal = true
	return diagonal

def astar(world):
	first = Node(0,0,0)
	first.costToStart = 0
	openList.append(first)
	while openList.len() != 0:
		minNode = openList[0]
		for i in openList:
			if cost(openList[i]) < cost(minNode):
				minNode = openList[i]
		openList.remove(minNode)
		if minNode.x != 9 and minNode.y != 7:
			closedList.append(minNode)
			totalCost += minNode.costToStart
			totalLocations +=1
			
			mintemp.f = adjacent(world, minNode)[0].costToStart + manhattan(adjacent(world, minNode)[0])
			for n in adjacent(world, minNode):
				if isValid(n.x,n.y):
					n.f = n.costToStart + manhattan(n)
					if n in openList:
						if n.f < mintemp.f:
							mintemp = n
							
						else:
							openList.append(n)
	print closedList
astar(world)
print totalLocations
print totalCost

			
						
						
					
					
				
			
		
		
		
		


		
