Flags
    -g  conditional probablity
    -j  joint probability
    -m  marginal probability

Input
    P  pollution   (p = low,  ~p = high)
    S  Smoker     (s = true, ~s = false)
    C  Cancer     (c = true, ~c = false)
    D  Dyspnoea   (d = true, ~d = false)
    X  X-Ray      (x = true, ~x = false)

Example Usage

    Marginal: python bayes.py -mD 
    Conditional: python bayes.py -g"c|~s" (quotes are necessary) 
    Joint: python bayes.py -jPSC
    
