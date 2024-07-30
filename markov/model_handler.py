class ModelHandler():

    @classmethod
    def generate_model(cls, tokens):
        model = {}
        last_token = None
        for token in tokens:
            if last_token == None:
                continue

            if last_token not in model:
                model[last_token] = [token, 1]
                
            if token in model[last_token]:
                model[last_token][token] += 1

            else:
                model[last_token][token] = 1
            

            last_token = token
            
