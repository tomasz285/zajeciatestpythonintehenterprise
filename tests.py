import unittest
from lab1_2Kowal import GenerujKase
from lab1_2Kowal import Stan

class TestMyCalc(unittest.TestCase):
	def setUp(self):
		self.spr = GenerujKase()
		self.st = Stan(10)	
	
	#### testy klasy GenerujKase 
	
	def test_kwoty_poczatkowej(self):
		self.assertEqual(0, self.spr.kwota)	
	
	def test_wrzucania(self):
		self.assertEqual(True, self.spr.dorzuc())

	def test_dlugosci_czasu_wrzucania(self):
		self.spr.dorzuc()
		self.assertTrue(self.spr.czaswrzucania < 7)
	

	#### testy klasy Stan

	def test_ceny_przejscia_przez_bramke(self):
		self.assertTrue(self.st.kwotaminimalna < 20)
	
	def test_stanu_poczatkowego(self):
		self.assertEqual("zamknieta", self.st.stan)

if __name__ == '__main__':
	unittest.main()
