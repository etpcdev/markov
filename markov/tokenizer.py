import re


class Tokenizer():

    @classmethod
    def tokenize_text(cls, text: str) -> list[str]:
        """Tokenize a body of text.

        Args:
            text (str): Body of text to tokenize.

        Returns:
            list[str]: List of tokens.
        """

        pattern: re.Pattern                  = cls.__compile_regex()
        matches: re.Iterator[re.Match[str]]  = pattern.finditer(text)
        tokens:  list[str]                   = []
        
        for match in matches:
            tokens.append(match[0])

        return tokens

    @staticmethod
    def __compile_regex() -> re.Pattern:
        """Defines what a token consists of.

        Returns:
            re.Pattern: Regex pattern.
        """
        
        elipses:    str = r'\.\.\.'
        numbers:    str = r'([0-9]+(?:\.*_*,*[0-9]*)+)'
        words:      str = r'\w+'
        spaces:     str = r' '
        grammar:    str = r'\W'
        new_line:   str = "\n"

        pattern:    str = (       
            elipses     + "|" + 
            numbers     + "|" + 
            words       + "|" + 
            spaces      + "|" + 
            grammar     + "|" + 
            new_line
        )
        
        return re.compile(pattern)
