import unittest

from markov_machine import MarkovMachine


class TestMarkovMachine(unittest.TestCase):
    
    mkv = MarkovMachine()
    test_tokens: list[str] = ['Once', ' ', 'upon', ' ', 'a', ' ', 'time']

    def test_load_model(self):
        pass

    def test_load_model_from_file(self):
        pass

    def test___init_state(self):
        state:       str        = None
        token_queue: list[str]  = None
        
        state, token_queue = self.mkv._MarkovMachine__init_state(
            self.test_tokens, depth=1)
        
        self.assertEqual("time", state)
        self.assertEqual(['time'], token_queue)

        state, token_queue = self.mkv._MarkovMachine__init_state(
            self.test_tokens, depth=2)
        
        self.assertEqual(" time", state)
        self.assertEqual([' ', 'time'], token_queue)

        state, token_queue = self.mkv._MarkovMachine__init_state(
            self.test_tokens, depth=3)
        
        self.assertEqual("a time", state)
        self.assertEqual(['a', ' ', 'time'], token_queue)

        state, token_queue = self.mkv._MarkovMachine__init_state(
            self.test_tokens, depth=4)
        
        self.assertEqual(" a time", state)
        self.assertEqual([' ', 'a', ' ', 'time'], token_queue)

        state, token_queue = self.mkv._MarkovMachine__init_state(
            self.test_tokens, depth=5)
        
        self.assertEqual("upon a time", state)
        self.assertEqual(['upon', ' ', 'a', ' ', 'time'], token_queue)
                         
        
    def test___init_output(self):
        
        self.assertEqual("Once upon a time", 
                         self.mkv._MarkovMachine__init_output(self.test_tokens))

    def test_get_next_token(self):
        pass

    def test_get_next_state(self):
        pass

    def test_generate_text(self):
        pass

    if __name__ == '__main__':
        unittest.main()