import unittest

from tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    
    def test_tokenize_text_grammar(self) -> None:
        grammar: str = ".,...(){}[]\\/*-+!?~^\" \n"
        self.assertEqual([".", ",", "...",
                          "(", ")", "{", "}", "[", "]", 
                          "\\", "/", "*", "-", "+",
                          "!", "?", "~", "^", "\"",
                          " ", "\n"
                          ], 
                          Tokenizer.tokenize_text(grammar))

    def test_tokenize_text_accented(self) -> None:
        accented_chars: list[str] = \
                         ["á", " ", "é", " ", "í", " ", "ó", " ", "ú", " ", 
                          "à", " ", "è", " ", "ì", " ", "ò", " ", "ù", " ", 
                          "ã", " ", "ẽ", " ", "ĩ", " ", "õ", " ", "ũ", " ", 
                          "â", " ", "ê", " ", "î", " ", "ô", " ", "û", " ", 
                          "ç", " ", "Ç", " ", "ñ", " ", "Ñ"
                          ]
        for char in accented_chars:
            self.assertEqual([char], 
                             Tokenizer.tokenize_text(char))

    def test_tokenize_text_words(self) -> None:
        words: str = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(["The", " ", "quick", " ", "brown", " ", "fox", " ",
                          "jumps", " ", "over", " ", "the", " ", "lazy", " ",
                          "dog"
                          ], 
                          Tokenizer.tokenize_text(words))

    def test_tokenize_text_int(self) -> None:
        for i in range(0, 9999):
            self.assertEqual([str(i)], 
                             Tokenizer.tokenize_text(str(i)))

        num_underscored: str = "1_000_000"
        self.assertEqual(["1_000_000"], 
                         Tokenizer.tokenize_text(num_underscored))
        
        num_comma: str = "1,000"
        self.assertEqual(["1,000"], 
                         Tokenizer.tokenize_text(num_comma))

    def test_tokenize_text_decimal(self) -> None:
        for i in range(0, 1000):
            self.assertEqual([str(i) + ".51"], 
                             Tokenizer.tokenize_text(str(i) + ".51"))

        num_dec_underscored: str = "1_000_000.000_000"
        self.assertEqual(["1_000_000.000_000"], 
                         Tokenizer.tokenize_text(num_dec_underscored))

        num_dec_comma: str = "1,000.00"
        self.assertEqual(["1,000.00"], 
                         Tokenizer.tokenize_text(num_dec_comma))
        
    
    def test_tokenize_text_type_error(self) -> None:
        with self.assertRaises(TypeError):
            Tokenizer.tokenize_text(10)


if __name__ == '__main__':
    unittest.main()