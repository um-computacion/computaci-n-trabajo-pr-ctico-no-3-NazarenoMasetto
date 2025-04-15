import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero


class TestCalculoNumeros(unittest.TestCase):

     
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

