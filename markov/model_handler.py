from json import dumps
class ModelHandler():

    @classmethod
    def export_model(cls, model, path):
        with open(path, "w") as export_file:
            export_file.write(model)


    @classmethod
    def __normalize_model(cls, model, tokens, depth):

        normalization_factor = 1

        key_token = None

        tracker = 1
        token_bucket = []
        for token in tokens:

            if tracker <= depth:
                token_bucket.append(token)
                tracker += 1
                continue

            
            key_token = ""
            for tkn in token_bucket:
                key_token += tkn

            token_bucket.append(token)
            token_bucket.pop(0)

            total_weight = 0
            for next_token in model[key_token]:
                total_weight += next_token[1]
            
            coefficient = normalization_factor / total_weight

            for next_token in model[key_token]:
                next_token[1] *= coefficient
        
            key_token = token

        return model


    @classmethod
    def generate_model(cls, tokens, depth=3):
        model = {}
        """
        model = {
            "token1" = [
                     ["next_token_A", 1],
                     ["next_token_B", 6],
                     ["next_token_C", 4],
                     ...
                    ],
            "token2" = [
                     ...
                    ],
            ...
        }
        
        """
        tracker = 1
        token_bucket = []
        for token in tokens:

            if tracker <= depth:
                token_bucket.append(token)
                tracker += 1
                continue

            
            key_token = ""
            for tkn in token_bucket:
                #print(tkn)
                key_token += tkn
                
            token_bucket.append(token)
            token_bucket.pop(0)
            

            #Create indexes for last token
            if key_token not in model:
                model[key_token] = [[token, float(0)]]

            #Populate last tokens list of possible next tokens
            if key_token in model:
                
                for next_token in model[key_token]:
                    
                    found = False

                    if token in next_token:
                        next_token[1] += 1
                        found = True
                        break
                
                if not found:
                    model[key_token].append([token, 1])
                    
            
            key_token = token

        model = cls.__normalize_model(model, tokens, depth)

        return dumps(model)
    


    """@classmethod
    def __normalize_model(cls, model, tokens):

        normalization_factor = 1

        key_token = None

        for token in tokens:

            #Set up the first pair of tokens
            if key_token == None:
                key_token = token
                continue

            total_weight = 0
            for next_token in model[key_token]:
                total_weight += next_token[1]
            
            coefficient = normalization_factor / total_weight

            for next_token in model[key_token]:
                next_token[1] *= coefficient
        
            key_token = token

        return model
    

    @classmethod
    def generate_model(cls, tokens):
        model = {}
        \"""
        model = {
            "token1" = [
                     ["next_token_A", 1],
                     ["next_token_B", 6],
                     ["next_token_C", 4],
                     ...
                    ],
            "token2" = [
                     ...
                    ],
            ...
        }
        
        \"""
        key_token = None
        for token in tokens:

            #Set up the first pair of tokens
            if key_token == None:
                key_token = token
                continue


            #Create indexes for last token
            if key_token not in model:
                model[key_token] = [[token, float(0)]]

            #Populate last tokens list of possible next tokens
            if key_token in model:
                
                for next_token in model[key_token]:
                    
                    found = False

                    if token in next_token:
                        next_token[1] += 1
                        found = True
                        break
                
                if not found:
                    model[key_token].append([token, 1])
                    
                
            key_token = token

        model = cls.__normalize_model(model, tokens)

        return dumps(model)
    """
    