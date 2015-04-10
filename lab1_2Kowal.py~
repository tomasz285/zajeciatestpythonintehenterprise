#symulacja bramki - wrzucamy do niej monety 

#klasa,ktora generuje pieniadze

#druga klasa, ktora generuje stan, np., zeby przejsc przez bramke musze miec 2 zl cnt musi podjac decyzje na podstawie czegosc


# musimy dac iles czasu na otwarcie bramki i znowu

import random
from time import sleep # importujemy, zeby robic przerwy na czas otwarcia bramki

class GenerujKase(object):
	def __init__(self):
		self.kwota = 0
		self.czaswrzucania = 0
	def dorzuc(self):
		#metoda dorzuc klasy GenerujKase dorzuca monete do kwoty
		self.czaswrzucania = random.randint(0,6)
		sleep(self.czaswrzucania)
		if self.czaswrzucania > 5:
			print "Przestales wrzucac pieniadze, zwracamy te ktore wrzuciles do tej pory"
			sleep(1.5)			
			self.kwota = 0
		else:
			self.kwota += random.randint(1,5)
			print "Z powodzeniem wrzuciles pieniadz, aktualna kwota: ", self.kwota
		
		return True





class Stan:
	"""
	#stan wie jaki jest obecny stan (np bramka zamknieta (czyli mam czekac na dobra kwote), bramka otwarta (ktos przechodzi, musze iles poczekac) itp)
	"""
	def __init__(self, kw):
		self.kwotaminimalna = kw
		self.stan = "zamknieta"
	
	def otworz(self):
		#ma byc jakis czas otwierania (np 2 s)
		self.stan = "otwarta"
		print "Bramka otwarta, przechodz :)"
		sleep(2) # sleep 1.5 seconds
		
		
		#metoda generuj klasy Stan generuje warunek - minimalna kwote przy ktorej bramka sie otworzy

if __name__ == '__main__':
	ob = Stan(10)
	kasa = GenerujKase()
	while True:
		while kasa.kwota<ob.kwotaminimalna:
			if kasa.kwota == 0:
				print "\n\nDzien dobry, wrzuc wymagana kwote, aby przejsc przez bramke: ", ob.kwotaminimalna, " zlotych"
				sleep(2)
	
			kasa.dorzuc()	#dorzucam monete
			sleep(1.5)
			if kasa.kwota > 0 and kasa.kwota<ob.kwotaminimalna:
				print "Za mala kwota - bramka zamknieta"

		#print (kasa.kwota)	#drukuje aktualny stan wrzuconych pieniedzy
		ob.otworz()
		kasa.kwota = 0
	




