import os
import unittest
from automato.mealyAutomato import mealyAutomato


class Test001(unittest.TestCase):
    def teste_001(self):
        file = open('testes/teste-001.cm', "r")

        correct = "INT\nID\nLPAREN\nVOID\nRPAREN\nLBRACES\nRETURN\nLPAREN\nNUMBER\nRPAREN\nSEMICOLON\nRBRACES\n"

        self.assertEqual(mealyAutomato.get_output_from_string(file.read()), correct)

        file.close()

    def teste_002(self):
        file = open('testes/teste-002.cm', "r")

        correct = "FLOAT\nID\nLPAREN\nFLOAT\nID\nCOMMA\nFLOAT\nID\nRPAREN\nLBRACES\nRETURN\nLPAREN\nID\nPLUS\nID\nRPAREN\nSEMICOLON\nRBRACES\nINT\nID\nLPAREN\nVOID\nRPAREN\nLBRACES\nFLOAT\nID\nATTRIBUTION\nID\nLPAREN\nNUMBER\nCOMMA\nNUMBER\nRPAREN\nSEMICOLON\nRETURN\nLPAREN\nNUMBER\nRPAREN\nSEMICOLON\nRBRACES\n"

        self.assertEqual(mealyAutomato.get_output_from_string(file.read()), correct)

        file.close()

    def teste_003(self):
        file = open('testes/teste-003.cm', "r")

        correct = "INT\nID\nLPAREN\nINT\nID\nRPAREN\nLBRACES\nINT\nID\nCOMMA\nID\nATTRIBUTION\nNUMBER\nCOMMA\nID\nATTRIBUTION\nNUMBER\nCOMMA\nID\nSEMICOLON\nFOR\nLPAREN\nID\nATTRIBUTION\nNUMBER\nSEMICOLON\nID\nLESS_EQUAL\nID\nSEMICOLON\nID\nATTRIBUTION\nID\nPLUS\nNUMBER\nRPAREN\nLBRACES\nID\nATTRIBUTION\nID\nPLUS\nID\nSEMICOLON\nID\nATTRIBUTION\nID\nSEMICOLON\nID\nATTRIBUTION\nID\nSEMICOLON\nRBRACES\nRETURN\nID\nSEMICOLON\nRBRACES\nINT\nID\nLPAREN\nVOID\nRPAREN\nLBRACES\nINT\nID\nATTRIBUTION\nNUMBER\nSEMICOLON\nINT\nID\nATTRIBUTION\nID\nLPAREN\nID\nRPAREN\nSEMICOLON\nRETURN\nNUMBER\nSEMICOLON\nRBRACES\n"

        self.assertEqual(mealyAutomato.get_output_from_string(file.read()), correct)

        file.close()

    def teste_004(self):
        file = open('testes/teste-004.cm', "r")

        correct = "INT\nID\nLPAREN\nINT\nID\nRPAREN\nLBRACES\nIF\nLPAREN\nID\nEQUALS\nNUMBER\nRPAREN\nRETURN\nNUMBER\nSEMICOLON\nELSE\nIF\nLPAREN\nID\nEQUALS\nNUMBER\nRPAREN\nRETURN\nNUMBER\nSEMICOLON\nELSE\nRETURN\nID\nLPAREN\nID\nMINUS\nNUMBER\nRPAREN\nPLUS\nID\nLPAREN\nID\nMINUS\nNUMBER\nRPAREN\nSEMICOLON\nRBRACES\nINT\nID\nLPAREN\nVOID\nRPAREN\nLBRACES\nINT\nID\nSEMICOLON\nID\nATTRIBUTION\nNUMBER\nSEMICOLON\nINT\nID\nATTRIBUTION\nID\nLPAREN\nID\nRPAREN\nSEMICOLON\nRETURN\nNUMBER\nSEMICOLON\nRBRACES\n"

        self.assertEqual(mealyAutomato.get_output_from_string(file.read()), correct)

        file.close()

    def teste_005(self):
        file = open('testes/teste-005.cm', "r")

        correct = "FLOAT\nID\nLPAREN\nINT\nID\nRPAREN\nLBRACES\nFLOAT\nID\nSEMICOLON\nIF\nLPAREN\nID\nLESS_EQUAL\nNUMBER\nRPAREN\nRETURN\nLPAREN\nNUMBER\nRPAREN\nSEMICOLON\nELSE\nLBRACES\nRETURN\nID\nTIMES\nID\nLPAREN\nID\nMINUS\nNUMBER\nRPAREN\nSEMICOLON\nRBRACES\nRBRACES\nINT\nID\nLPAREN\nVOID\nRPAREN\nLBRACES\nINT\nID\nATTRIBUTION\nNUMBER\nSEMICOLON\nINT\nID\nATTRIBUTION\nID\nLPAREN\nID\nRPAREN\nSEMICOLON\nRETURN\nNUMBER\nSEMICOLON\nRBRACES\n"

        self.assertEqual(mealyAutomato.get_output_from_string(file.read()), correct)

        file.close()
