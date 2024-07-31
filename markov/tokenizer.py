import re
"""
Accepts a body of text and returns a list of all the tokens in order.
"""
class Tokenizer():
    
    #Tokenizes Unicode text
    @classmethod
    def tokenize_text(cls, text: str) -> list[str] | None:
        
        pattern = cls.__compileRegex(mode="text")
        matches = pattern.finditer(text)

        tokens = []
        for i in matches:
            tokens.append(i[0])

        return tokens or None
        

    #if newlines are a problem, replace them with a placeholder like § <-- paragraph symbol

    def __compileRegex(mode="text") -> re.Pattern:
        if mode == "text":
            elipses = r'\.\.\.'
            numbers = r'([0-9]+(?:\.*_*,*[0-9]*)+)'
            words = r'\w+'
            spaces = r' '
            grammar = r'\W'
            new_line = "\n"
            pattern = elipses + "|" + numbers + "|" + words + "|" + spaces + "|" + grammar + "|" + new_line
        
        return re.compile(pattern)
