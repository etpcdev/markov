from json import dumps
class ModelHandler():

    @staticmethod
    def export_model(model: str, path: str) -> None:
        """Save the model to a file designated by path. 
        (Must be a JSON compatible string)"""

        with open(path, "w") as f:
            f.write(model)


    @staticmethod
    def __normalize_model(model:  dict[str, list[str, float]], 
                          tokens: list[str], 
                          depth:  int) -> dict[str, list[str, float]]:
        """Normalize the probabilities of each token key to 0-1."""
        normalization_factor: float = 1

        depth_tracker: int = 1
        token_bucket: list[str] = []
        for token in tokens:

            if depth_tracker <= depth:
                token_bucket.append(token)
                depth_tracker += 1
                continue
            
            key_token: str = ""
            for tkn in token_bucket:
                key_token += tkn

            token_bucket.append(token)
            token_bucket.pop(0)

            total_weight: float = 0
            for next_token in model[key_token]:
                total_weight += next_token[1]
            
            coefficient: float = normalization_factor / total_weight

            for next_token in model[key_token]:
                next_token[1] *= coefficient

        return model


    @classmethod
    def generate_model(cls, tokens: list[str], depth: int = 3) -> str:
        """Generate a model as JSON using a list of tokens."""
        model: dict[str, list[str, float]] = {}

        depth_tracker: int = 1
        token_bucket: list[str] = []
        for token in tokens:

            #Get the first n tokens (defined by depth) to use as a key.
            if depth_tracker <= depth:
                token_bucket.append(token)
                depth_tracker += 1
                continue

            #Constructs tokens to be used as keys in the model.
            key_token: str = ""
            for tkn in token_bucket:
                key_token += tkn
                
            token_bucket.append(token)
            token_bucket.pop(0)
            
            #Creates an index for the key token.
            if key_token not in model:
                model[key_token] = [[token, float(0)]]

            #Populate key token's list of transitions.
            if key_token in model:

                for next_token in model[key_token]:
                    found: bool = False

                    if token in next_token:
                        next_token[1] += 1
                        found = True
                        break
                
                if not found:
                    model[key_token].append([token, 1])

        model = cls.__normalize_model(model, tokens, depth)

        return dumps(model)