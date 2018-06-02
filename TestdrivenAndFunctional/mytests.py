import unittest
from mycode import *

class Tests(unittest.TestCase):

    def test_grenzen_test(self):
        self.assertEqual(grenzen_test(1, 2), 2)
        self.assertEqual(grenzen_test(-3, 2056), 2056)
        self.assertEqual(grenzen_test(-10, -25), -10)

    def test_array_uebergabe(self):
        self.assertEqual(array_uebergabe(1, 100).min(), 1)
        self.assertEqual(array_uebergabe(1, 100).max(), 99)
        

        #Ánmerkung / Frage:
        #Die anderen Funktionen im Programm kann man nicht testen da sie auf User-Inputs basieren ( user_input / die while-Schleife ). Jedenfalls fällt mir nicht ein wie das realisierbar sein sollte ohne die Eingabe des Users vorherzusehen.
        

#Ausführung der Tests am Ende des Durchlaufes
if __name__ == '__main__':  
    unittest.main()