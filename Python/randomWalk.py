def takeAWalk(numSteps):
    from random import random
    stepsForwardOfStart = 0
    stepsSidewaysOfStart = 0
    for step in range(numSteps):
        if random() > 0.75:
            stepsForwardOfStart = stepsForwardOfStart + 1
            print(random())
        elif random() > 0.5:
            stepsSidewaysOfStart = stepsSidewaysOfStart + 1
        elif random() > 0.25:
            stepsForwardOfStart = stepsForwardOfStart - 1
        else:
            stepsSidewaysOfStart = stepsSidewaysOfStart - 1
    
    
    print (stepsForwardOfStart)
    print (stepsSidewaysOfStart)
