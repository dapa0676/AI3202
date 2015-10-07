#Dan Palmer
#PA 5 
#collaboration with Dan Mathews
import sys
import math

#global vars
stateSet = []
actionSet = []
world=[]

discount = 0.9
epsilon = 0.0
delta = 100000000000

dir_UP = "U"
dir_DOWN = "D"
dir_LEFT = "L"
dir_RIGHT = "R"
previousDirection = ""

pr_success = 0.8
pr_fail = 0.1
	
class node():
	def __init__(self):
		self.util = 0
		self.reward = 0
		self.occupied = 0
		self.walkable = 1
		self.discount = 0
		self.direction = "B"
		self.x = 0
		self.y = 0
	
	def setReward(self, reward):
		self.reward = reward
	def setWalkable(self, walkable):
		self.walkable = walkable
	def setCoord(self, x, y):
		self.x = x
		self.y = y
	def setUtil(self,util):
		self.util = util
	def setDirection(self, direction):
		self.direction = direction
		
	def getUtil(self):
		return self.util
	def getCoord(self):
		return (self.x, self.y)
	def getReward(self):
		return self.reward
	def getDirection(self):
		return self.direction
	def getWalkable(self):
		return self.walkable
	
def parse():
	global epsilon
	if (sys.argv[1] == "W"):
		OpenedFile = open("World1MDP.txt")
	world = [x.split(" ") for x in OpenedFile.read().split("\n") if x]
	epsilon = float(sys.argv[2])
	return world


def nodeDec(inputMatrix):
	Matrix=[[0 for i in range(10)]for j in range(8)]
	for i in range(8):
		for j in range(10):
			Matrix[i][j] = node()
			Matrix[i][j].setCoord(i, j)
        
	for i in range(8):
		for j in range(10):
			temp = int(inputMatrix[i][j])
			if temp == 1:
				Matrix[i][j].setReward(-1)
				Matrix[i][j].occupied = True
			elif temp == 2:
				Matrix[i][j].setWalkable(0)
			elif temp == 3:
				Matrix[i][j].setReward(-2)
				Matrix[i][j].occupied = True
			elif temp == 4:
				Matrix[i][j].setReward(1)
				Matrix[i][j].occupied = True
			elif temp == 50:
				Matrix[i][j].setReward(0)
				Matrix[i][j].occupied = True
			elif temp == 0:
				Matrix[i][j].setReward(0)
	
	return Matrix

def calculateUtil(node, nodeMatrix):
	utilPrime = 0
	expectedUtil = []
	currentX, currentY = node.getCoord()
	global previousDirection
	
	
	#up utility
	if currentX + 1 >= 8 or previousDirection == "D":
		upUtility = 0
	else:
		if nodeMatrix[currentX + 1][currentY].getWalkable() == 0:
			upUtility = 0
		else:
			upUtility = nodeMatrix[currentX+1][currentY].getUtil()
			print "Current x, current y, upUtility", currentX+1, currentY, upUtility
		
	
	#down utility
	if currentX - 1 < 0 or previousDirection == "U":
		downUtility = 0
	else:
		if nodeMatrix[currentX - 1][currentY].getWalkable() == 0:
			downUtility = 0
		else: 
			downUtility = nodeMatrix[currentX - 1][currentY].getUtil()
		
	#right utility
	if currentY + 1 > 7 or previousDirection == "L":
		rightUtility = 0
	else:
		if nodeMatrix[currentX][currentY + 1].getWalkable() == 0:
			rightUtility = 0
		else: 
			rightUtility = nodeMatrix[currentX][currentY + 1].getUtil()
	
	#left utility
	if currentY - 1 < 0 or previousDirection == "R":
		leftUtility = 0
	else:	
		if nodeMatrix[currentX][currentY - 1].getWalkable() == 0:
			leftUtility = 0
		else:
			leftUtility = nodeMatrix[currentX][currentY - 1].getUtil()

		
	
	#right	
	expectedUtil.append(((pr_success*rightUtility + pr_fail*upUtility + pr_fail*downUtility),dir_RIGHT))
	
	#left
	expectedUtil.append(((pr_success*leftUtility + pr_fail*upUtility + pr_fail*downUtility),dir_LEFT))
	
	#up
	expectedUtil.append(((pr_success*upUtility + pr_fail*leftUtility + pr_fail*rightUtility),dir_UP))
	
	#down
	expectedUtil.append(((pr_success*downUtility + pr_fail*rightUtility + pr_fail*leftUtility),dir_DOWN))
	
	U = node.getUtil()

	maxEU = max(expectedUtil)
	
	
	if currentY == 7 and currentX == 9:
		utilPrime = 50
	else:
		utilPrime = float(node.getReward() + discount * maxEU[0])


	#print utilPrime
	node.setUtil(utilPrime)
	#print "direction of node: "
	print currentX, currentY
	print expectedUtil
	print maxEU[0]
	
	#print maxEU[1]
	
	node.setDirection(maxEU[1])
	return abs(U - node.getUtil())
	



def main():
	world = parse()
	nodeMatrix = nodeDec(world) #create matrix of instantiated nodes, each with appropriate rewards, walls set unwalkable
	global epsilon
	global delta
	global discount
	
	
	while (delta > (epsilon * (1-discount)/discount)):
		#print delta
		#print ((1-discount)/discount)
		delta = 0.0
		for i in range(8):
			for j in range(10):
				tempDelta = calculateUtil(nodeMatrix[i][j],nodeMatrix) 
				
				if tempDelta > delta:
					delta = tempDelta
	
	currentNode = nodeMatrix[0][0]
	while (currentNode.getUtil() != 50):
		global previousDirection
		
		currentX, currentY = currentNode.getCoord()
		#print currentX, currentY
	
		#print currentNode.getDirection()
		
		if currentNode.getDirection() == "R": 
			currentNode = nodeMatrix[currentX][currentY+1]
			previousDirection = "R"
			#print currentNode.getUtil()
			#print "RIGHT "
		elif currentNode.getDirection() == "L":
			currentNode = nodeMatrix[currentX][currentY-1]
			previousDirection = "L"
			#print currentNode.getUtil()
			#print "LEFT "
		elif currentNode.getDirection() == "D":
			currentNode = nodeMatrix[currentX-1][currentY]
			previousDirection = "D"
			#print currentNode.getUtil()
			#print "DOWN "
		elif currentNode.getDirection() == "U":
			currentNode = nodeMatrix[currentX+1][currentY]
			previousDirection = "U"
			#print currentNode.getUtil()
			#print "UP "
		
main()
	
