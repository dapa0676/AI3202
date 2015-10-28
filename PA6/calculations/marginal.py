def margninalProbability(engine, input, printable = True, returnable = True):
  Q = engine.marginal(input)[0]

  trueName = 'true'
  falseName = 'false'

  if input.name == 'pollution':
    trueName = 'low'
    falseName = 'high'


  true = Q.generate_index([True], range(Q.nDims))
  if printable:
    print "The marginal probability of", input.name + "=" + trueName + ":", Q[true]
  false = Q.generate_index([False], range(Q.nDims))
  if printable:
    print "The marginal probability of", input.name + "=" + falseName + ":", Q[false]

  if returnable:
    return Q[true]
  else:
    return Q[false]
