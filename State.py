from Transition import Transition


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []
        self.conditions = []  # são do alfabeto de entrada, não posso ter em um estado, uma condição levando para 2 estados

    def addTransition(self, condition, destinationState, output):
        if condition not in self.conditions:
            self.transitions.append(Transition(condition, destinationState, output))
            self.conditions.append(condition)

    def getByCondition(self, condition):
        for transition in self.transitions:
            if condition == transition.condition:
                return transition

        return None
