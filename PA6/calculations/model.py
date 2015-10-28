try:
    from IPython import embed
except:
    pass

import sys
from numpy import *
from pbnt.Graph import *
from pbnt.Distribution import *
from pbnt.Node import *


#Globals for changing distributions of smoker and pollution
smokerFalse = 0.7
smokerTrue = 0.3
pollutionLow = 0.9 
pollutionHigh = 0.1

def BayesModel():
  #Initialize the Cancer Bayes Network

  numberOfNodes = 5

  #name the nodes
  pollution = 0
  smoker = 1
  cancer = 2
  xray = 3
  dyspnoea = 4

  pNode = BayesNode(0, 2, name="pollution")
  sNode = BayesNode(1, 2, name="smoker")
  cNode = BayesNode(2, 2, name="cancer")
  xNode = BayesNode(3, 2, name="xray")
  dNode = BayesNode(4, 2, name="dyspnoea")

  #pollution
  pNode.add_child(cNode)

  #smoker
  sNode.add_child(cNode)

  #cancer
  cNode.add_parent(pNode)
  cNode.add_parent(sNode)
  cNode.add_child(xNode)
  cNode.add_child(dNode)

  #xray
  xNode.add_parent(cNode)

  #dyspnoea
  dNode.add_parent(cNode)

  nodes = [pNode, sNode, cNode, xNode, dNode]

  #create distributions
  #pollution distribution
  pDistribution = DiscreteDistribution(pNode)
  index = pDistribution.generate_index([],[])
  pDistribution[index] = pollutionHigh, pollutionLow
  pNode.set_dist(pDistribution)

  #smoker distribution
  sDistribution = DiscreteDistribution(sNode)
  index = sDistribution.generate_index([],[])
  sDistribution[index] = smokerFalse, smokerTrue
  sNode.set_dist(sDistribution)

  #cancer
  dist = zeros([pNode.size(), sNode.size(), cNode.size()], dtype=float32)
  # P = High -> 0, S = False -> 0
  dist[0,1,] = [0.95, 0.05]
  dist[0,0,] = [0.98,0.02]
  dist[1,1,] = [0.97, 0.03]
  dist[1,0,] = [0.999,0.001]
  cDistribution = ConditionalDiscreteDistribution(nodes=[pNode, sNode, cNode], table=dist)
  cNode.set_dist(cDistribution)

  #xray
  dist = zeros([cNode.size(), xNode.size()], dtype=float32)
  dist[1,] = [0.1,0.9]
  dist[0,] = [0.8,0.2]
  xDistribution = ConditionalDiscreteDistribution(nodes=[cNode, xNode], table=dist)
  xNode.set_dist(xDistribution)

  #dyspnoea
  dist = zeros([cNode.size(), dNode.size()], dtype=float32)
  dist[1,] = [0.35,0.65]
  dist[0,] = [0.7, 0.3]
  dDistribution = ConditionalDiscreteDistribution(nodes=[cNode, dNode], table=dist)
  dNode.set_dist(dDistribution)

  return BayesNet(nodes)

