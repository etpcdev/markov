from json import loads
from random import choices
from .tokenizer import Tokenizer

class MarkovMachine:

    def __init__(
            self, 
            model: dict[str, list[str, float]] | None = None
            ) -> None:
        """Create a markov chain machine with or without a model."""
        self.__model: dict[str, list[str, float]] | None = model
        

    def load_model(self, model: str) -> None:
        """Load an existing model.(JSON)"""
        self.__model = loads(model)

    def load_model_from_file(self, path: str) -> None:
        """Load a model from a file. (JSON)"""
        with open(path, "r") as f:
            model: str = f.read()
        
        self.load_model(model=model)


    @staticmethod
    def __init_state(input_tokens: list[str], depth: int = 3) -> str:
        """Initialize the state of the machine."""
        state: str = ""
        for tkn in input_tokens:
            state += tkn
        return (state, input_tokens[-depth:])
    
    @staticmethod
    def __init_output(input_tokens: list[str]) -> str:
        """Initialize the output."""
        output_text: str = ""
        for tkn in input_tokens:
            output_text += tkn
        return output_text
    

    def get_next_token(self, state: str) -> str | None:
        """Generates the next transition state."""
        if state not in self.__model:
            return None

        next_states: list[str] = []
        probabilities: list[float] = []

        for transition in self.__model[state]:
            next_states.append(transition[0])
            probabilities.append(transition[1])
            
        return choices(population=next_states,weights=probabilities)[0]
    
    def get_next_state(
                    self, 
                    next_token: str, 
                    input_queue: list[str]
                    ) -> tuple[str,list[str]]:
        """Updates the machine's state."""
        input_queue.append(next_token)
        input_queue.pop(0)

        state: str = ""
        for tkn in input_queue:
            state += tkn

        return (state, input_queue)
    

    def generate_text(
                    self, *,
                    input_tokens: list[str], 
                    output_length: int = 100, 
                    depth: int = 3
                    ) -> str:
        """Generates a string of up to length tokens, 
        using a model and tokenized user input."""
        input_queue: list[str] = input_tokens
        output_text: str = self.__init_output(input_queue)
        state: str
        state, input_queue = self.__init_state(input_queue, depth)
        
        for _ in range(output_length):
            next_token: str | None = self.get_next_token(state)
            if next_token:
                state, input_queue = self.get_next_state(next_token, 
                                                        input_queue)
                output_text += next_token
            else:
                break
        
        return output_text