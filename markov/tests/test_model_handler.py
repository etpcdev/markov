import unittest
import json

from model_handler import ModelHandler


class TestModelHandler(unittest.TestCase):

    sample_text: list[str] = ['This', ' ', 'is', ' ', 'a', ' ', 'sample', ' ', 
                              'text', 'text', ' ', 'etc', '.']
    
    def test_generate_model_depth_1(self) -> None:
        
        model_str: str = ModelHandler.generate_model(tokens=self.sample_text, 
                                                     depth=1)
        model: dict[str, list[str, float]] = json.loads(model_str)
        self.assertEqual(model["text"], [['text', 0.5],[' ', 0.5]])

    def test_generate_model_depth_3(self) -> None:
        
        model_str: str = ModelHandler.generate_model(tokens=self.sample_text, 
                                                     depth=3)
        model: dict[str, list[str, float]] = json.loads(model_str)
        self.assertEqual(model["This is"], [[' ', 1.0]])
