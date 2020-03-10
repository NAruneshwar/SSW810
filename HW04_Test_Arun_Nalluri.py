import unittest
from HW04_Arun_Nalluri import count_vowels , last_occurrence, my_enumerate,Fraction

class TestIteration(unittest.TestCase):
    """class is used to test the count vowels, last occurance, custom enumerate function"""

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'),3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels('!$%^**@))@*%&%^%&@((@))'),0)
        self.assertEqual(count_vowels(''),0)

    def test_last_occurance(self):
        self.assertEqual(last_occurrence(target ='k',sequence='apple'),None)
        self.assertEqual(last_occurrence('s','mississippi'),6)
        self.assertEqual(last_occurrence('42',('1','2','3','47','42','65','98','45','32','54','42','69','87')),10)
        self.assertEqual(last_occurrence('66',('')),None)

    def test_my_enumerate(self):
        self.assertEqual(list(my_enumerate("your_sequence")),list(enumerate("your_sequence")))
        self.assertTrue(list(my_enumerate("Aruneshwar")) == list(enumerate("Aruneshwar")))
        self.assertFalse(list(my_enumerate("Aruneshwar")) == list(enumerate("Arun eshwar")))
        self.assertTrue(list(my_enumerate("Aruneshwar")) != list(enumerate("Arune shwr")))



class TestFraction(unittest.TestCase):
    def test_init(self):
        """test the fraction class"""
   
        fraction1 = Fraction(1,2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1,0)
        
    
    def test_add(self):
        """Checks the add function"""
        fraction3 = Fraction(1,2)+Fraction(1,2)
        self.assertEqual(str(fraction3),"1/1")
        self.assertTrue(str(Fraction(2,4)+Fraction(4,2))!='3/1')
        self.assertFalse(str(Fraction(2,1)+Fraction(4,2))=='3/1')
        self.assertFalse(str(Fraction(2,1)+Fraction(4,2))=='6/1')
        self.assertTrue(str(Fraction(-2,1)+Fraction(4,-2))=='-4/1')


    def test_sub(self):
        """Checks the Sub Function"""
        fraction3 = Fraction(1,2)-Fraction(1,2)
        self.assertEqual(str(fraction3),"0/1")
        self.assertTrue(str(Fraction(1,2)-Fraction(-1,4))=="3/4")
        self.assertFalse(str(Fraction(1,2)-Fraction(-1,4))!="3/4")


    def test_mul(self): 
        """Checks the Multiplication Function"""
        fraction3 = Fraction(4,2)*Fraction(1,4)
        self.assertEqual(str(fraction3),"1/2")
        self.assertNotEqual(str(Fraction(8,2)*Fraction(1,9)),"1/2")
        self.assertTrue(str(Fraction(8,2)*Fraction(2,16))=="1/2")
        self.assertFalse(str(Fraction(8,2)*Fraction(2,-16))=="1/2")
        self.assertTrue(str(Fraction(8,2)*Fraction(2,-16))=="-1/2")


    def test_div(self):   
        """Checks the Devide Function"""
        fraction3= Fraction(7,10)/Fraction(4,5)
        self.assertEqual(str(fraction3),"7/8")
        self.assertNotEqual(str(Fraction(7,10)/Fraction(4,5)),"9/8")
        self.assertTrue(str(Fraction(7,10)/Fraction(-4,5))=="-7/8")
        self.assertFalse(str(Fraction(7,10)/Fraction(4,8))=="7/8")        

    
    def test_equal(self):
        """Check the equals to function"""
        self.assertTrue(Fraction(7,10)==Fraction(14,20))
        self.assertFalse(Fraction(1,2)==Fraction(2,8))
        self.assertEqual(Fraction(-1,2),Fraction(4,-8))
        self.assertNotEqual(Fraction(1,2),Fraction(4,-8))

    
    def test_notequal(self):
        """check the not equals function"""
        self.assertTrue(Fraction(7,10)!=Fraction(-6,10))
        self.assertFalse(Fraction(7,90)==Fraction(9,10))
        self.assertEqual(Fraction(-6,10),Fraction(-6,10))
        self.assertNotEqual(Fraction(7,10),Fraction(-6,10))
        
    
    def test_GreaterThan(self):
        """check the greater than function"""
        self.assertTrue(Fraction(9,10)>Fraction(7,10))
        self.assertTrue(Fraction(9,10)>Fraction(7,10))
        self.assertTrue(Fraction(9,10)>Fraction(7,10))
        self.assertTrue(Fraction(9,10)>Fraction(7,10))
 
    
    def test_GreaterThanorEqualto(self):
        """check greater than or equals function"""
        self.assertTrue(Fraction(7,10)>=Fraction(7,10))
        self.assertFalse(Fraction(7,10)>=Fraction(7,8))
       
      
    def test_LessThan(self):
        """check the less than function"""
        self.assertTrue(Fraction(-7,10)<Fraction(15,10))
        self.assertFalse(Fraction(7,1)<Fraction(15,10))

    def test_LessThanorEqualto(self):
        """check the less than or equals function"""
        self.assertTrue(Fraction(-7,10)<=Fraction(-7,10))
        self.assertTrue(Fraction(-7,1)<=Fraction(-7,10))
        self.assertFalse(Fraction(7,1)<=Fraction(7,10))

    
    def test_simplify(self):
        """"Check the simplify command"""
        self.assertTrue((str(Fraction(9, 27).simplify()) == str(Fraction(1, 3))))
        self.assertFalse(Fraction(9, 27).simplify() == Fraction(1, 6))
        self.assertTrue(Fraction(9, 27) != Fraction(10, 3))    
        self.assertTrue(Fraction(81,9),Fraction(18,2))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)