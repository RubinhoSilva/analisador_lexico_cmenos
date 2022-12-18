from automata.fa.Mealy import Mealy


class Automata:
    def __init__(self, inputAlphabet, initialState, defaultState=None, defaultOutput=''):
        self.inputAlphabet = inputAlphabet
        self.initialState = initialState
        self.defaultState = defaultState
        self.defaultOutput = defaultOutput
        self.states = []
        self.outputAlphabet = []

        if defaultState is not None:
            self.states.append(defaultState)

    def addState(self, state):
        self.states.append(state)

    def getDict(self, stataName):
        dic = {}
        for alphabet in self.inputAlphabet:
            for state in self.states:
                if stataName == state.name:
                    if alphabet in state.conditions:
                        # condição existe, posso adicionar ela mesmo
                        transition = state.getByCondition(alphabet)
                        # print(transition)
                        dic[alphabet] = (transition.destinationState.name, transition.output)
                    else:
                        # condição não existe, adiciono o padrão
                        dic[alphabet] = (self.defaultState.name, self.defaultOutput)

        return dic

    def getMealyAutomata(self):
        statesName = []
        for state in self.states:
            statesName.append(state.name)

        dicStatesTransitions = {}
        for state in self.states:
            dicStatesTransitions[state.name] = self.getDict(state.name)

        return Mealy(statesName, self.inputAlphabet, self.outputAlphabet, dicStatesTransitions, self.initialState.name)
