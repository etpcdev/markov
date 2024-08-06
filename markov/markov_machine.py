from json import loads
from random import choices
from .tokenizer import Tokenizer

class MarkovMachine:

    def __init__(self, user_input=None):
        self.__model = None
        self.__user_input = user_input

    def load_model(self, model):
        self.__model = loads(model)


    def load_model_from_file(self, path):
        with open(path, "r") as f:
            model = f.read()
        
        self.load_model(model=model)
        #self.__model = loads(model)


    def generate_chain(self, length=100, depth=3):

        input_bucket = self.__tokenize_user_input()
        
        output = ""
        for tkn in input_bucket:
            output += tkn
        
        input_bucket = input_bucket[-depth:]
        state = ""
        for tkn in input_bucket:
            state += tkn
        
        #output = state
        
        for _ in range(length):
            if state not in self.__model:
                break
            input_bucket.pop(0)
            
            next_states = []
            probabilities = []
            for next_state in self.__model[state]:
                next_states.append(next_state[0])
                probabilities.append(next_state[1])
                

            next_token = choices(population=next_states,weights=probabilities)
            input_bucket.append(next_token[0])
            state = ""
            for tkn in input_bucket:
                state += tkn
            
            output += next_token[0]

        
        return output


    def __tokenize_user_input(self):
        return Tokenizer.tokenize_text(text=self.__user_input)