from json import loads
from random import choices
from typing import Any


class MarkovMachine:

    __slots__ = "__model"

    def __init__(self, model: dict[str, Any] | None = None) -> None:
        """Create a markov chain machine with or without a model.
        The model must be structured as dict[str, list[str, float]].
        Only initialize it if the model was manyally loaded from a 
        JSON compatible string.

        Args:
            model (dict[str, Any] | None, optional): structured model. 
                Defaults to None.
        """
        
        self.__model: dict[str, Any] | None = model
        

    def load_model(self, model: str) -> None:
        """Load an existing model.(JSON)

        Args:
            model (str): JSON formatted model.
        """
        
        self.__model = loads(model)

    def load_model_from_file(self, path: str) -> None:
        """Load a model from a file. (JSON)

        Args:
            path (str): Path of the JSON file to load.
        """
        
        with open(path, "r") as f:
            model: str = f.read()
        
        self.load_model(model=model)


    @staticmethod
    def __init_state(input_tokens: list[str], 
                     depth: int = 3) -> tuple[str, list[str]]:
        """Initialize the state of the machine.

        Args:
            input_tokens (list[str]): Initial tokens provided from user.
            depth (int, optional): N. of tokens per key. Defaults to 3.

        Returns:
            tuple[str, list[str]]: State and tokens to use as first key.
        """
        
        state: str = ""
        input_tokens = input_tokens[-depth:]
        
        for tkn in input_tokens:
            state += tkn
        
        return (state, input_tokens)
    
    @staticmethod
    def __init_output(input_tokens: list[str]) -> str:
        """Initialize the output.

        Args:
            input_tokens (list[str]): All tokens provided by user.

        Returns:
            str: String consisting of all user provided tokens.
        """
        
        output_text: str = ""
        
        for tkn in input_tokens:
            output_text += tkn
            
        return output_text
    

    def get_next_token(self, state: str) -> str | None:
        """Generates the next transition state.

        Args:
            state (str): Current key string.

        Returns:
            str | None: The next token chosen by weight.
        """
        
        if state not in self.__model:
            return None

        next_states:    list[str]   = []
        probabilities:  list[float] = []

        for transition in self.__model[state]:
            next_states.append(transition[0])
            probabilities.append(transition[1])
            
        return choices(population=next_states,
                       weights=probabilities)[0]
    
    def get_next_state(self, next_token: str, 
                       input_queue: list[str]) -> tuple[str,list[str]]:
        """Updates the machine's state.

        Args:
            next_token (str): Token chosen by get_next_token()
            input_queue (list[str]): Current tokens in queue.

        Returns:
            tuple[str,list[str]]: New state, and updated queue.
        """
        
        input_queue.append(next_token)
        input_queue.pop(0)

        state: str = ""
        
        for tkn in input_queue:
            state += tkn

        return (state, input_queue)
    

    def generate_text(self, *, input_tokens: list[str], 
                      output_length: int = 100, depth: int = 3) -> str:
        """Generates a string of up to output_length tokens, 
        using a model and tokenized user input.

        Args:
            input_tokens (list[str]): Seed tokens provided by user.
            output_length (int, optional): How many tokens to generate. 
                Defaults to 100.
            depth (int, optional): How many tokens to use per key. 
                Must be the same as the model. 
                Defaults to 3.

        Returns:
            str: The generated text.
        """
        
        input_queue:    list[str]  = input_tokens
        output_text:    str        = self.__init_output(input_queue)
        state:          str
        
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