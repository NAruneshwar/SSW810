import unittest

class Fraction:
    """Class Fraction creates and stores variables while also doing operations with fractions"""
    
    def __init__(self,numerator,denominator):
        """Initialise the numerator and denominator"""
        self.numerator = numerator
        self.denominator = denominator
        if(denominator==0):
            raise ValueError
    
    def __str__(self):
        """Default print function"""
        return(f"{self.numerator}/{self.denominator}")
    
    def __add__(self,other):
        """Adds two fractions using + symbol"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator+other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def __sub__(self,other):
        """subtracts two fractions using - symbol"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator-other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def __mul__(self,other):
        """Multiplies two fractions using * symbol"""
        if(self.denominator*other.denominator<0):
            resultnumerator = -1*self.numerator*other.numerator
            resultdenominator = abs(self.denominator*other.denominator) 
        else:
            resultnumerator = self.numerator*other.numerator
            resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def __truediv__(self,other):
        resultnumerator = self.numerator*other.denominator
        resultdenominator = self.denominator*other.numerator
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def __eq__(self,other):
        """takes two fractions and tests if they are equal"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator==other.numerator):
            return True
        else:
            return False
        return        
        

    def __ne__(self, other): 
        """takes two fractions and tests if they are not equal"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator!=other.numerator):
            return True
        else:
            return False
    
    def __lt__(self, other):
        """takes two fractions and tests if first one is less than second"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator<other.numerator):
            return True
        else:
            return False
    
    def __le__(self, other): 
        """takes two fractions and tests if first one is less or equal to the second"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator<=other.numerator):
            return True
        else:
            return False
    
    def __gt__(self, other):  
        """takes two fractions and tests if first one is greater than second"""       
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator>other.numerator):
            return True
        else:
            return False

    def __ge__(self, other): 
        """takes two fractions and tests if first one is greater than or equal to second"""
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator>=other.numerator):
            return True
        else:
            return False

class FractionTest(unittest.TestCase):
    def test_init(self):
        """test the fraction class"""
   
        fraction1 = Fraction(1,2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        
    
    def test_add(self):
        """Checks the add function"""
        newvalues = Fraction(1,2)+Fraction(1,2)
        fraction1 = Fraction(newvalues[0],newvalues[1])
        self.assertEqual(str(fraction1),"4/4")

    def test_sub(self):
        """Checks the Sub Function"""
        newvalues = Fraction(1,2)-Fraction(1,2)
        fraction1 = Fraction(newvalues[0],newvalues[1])
        self.assertEqual(str(fraction1),"0/4")
    
    def test_mul(self): 
        """Checks the Multiplication Function"""
        newvalues = Fraction(3,2)*Fraction(1,4)
        fraction1 = Fraction(newvalues[0],newvalues[1])
        self.assertEqual(str(fraction1),"3/8")

    def test_div(self):   
        """Checks the Devide Function"""
        newvalues= Fraction(7,10)/Fraction(4,5)
        fraction1 = Fraction(newvalues[0],newvalues[1])
        self.assertEqual(str(fraction1),"35/40")
    
    def test_equal(self):
        """Check the equals to function"""
        self.assertTrue(Fraction(7,10)==Fraction(7,10))

    
    def test_notequal(self):
        """check the not equals function"""
        self.assertTrue(Fraction(144,2)!=Fraction(8,4))
        
    
    def test_GreaterThan(self):
        """check the greater than function"""
        self.assertTrue(Fraction(9,10)>Fraction(7,10))
 
    
    def test_GreaterThanorEqualto(self):
        """check greater than or equals function"""
        self.assertTrue(Fraction(7,10)>=Fraction(7,10))
       
      
    def test_LessThan(self):
        """check the less than function"""
        self.assertTrue(Fraction(-7,10)<Fraction(15,10))
       
        

    def test_LessThanorEqualto(self):
        """check the less than or equals function"""
        self.assertTrue(Fraction(-7,10)<=Fraction(-7,10))
    
    


"""
def main():
    print("Welcome to the fraction calculator!")

    test = input("would you like to run test suit? press 'y' for yes any other for no")
    if(test=='y'):
        test_suit()
    flag=int(0)
    while(flag==0):
        try:
            num = int(input("Fraction 1 numerator: "))
            den = int(input("Fraction 1 denominator: "))
            if (den==0):
                raise ValueError
            else:
                flag=1
        except ValueError:
            print('please enter only an integer and make sure denominator is not 0')
            flag=0
    
    fraction1 = Fraction(num,den)
    operation = input("Please enter desired operation (+,-,*,/,==,<,<=,>,>=,!=) or any other key to exit the program: ")
    while operation in ['+','-','*','/','==','<','<=','>','>=','!=']:
        flag=0
        while(flag==0):
            try:                                        
                num2 = int(input("Fraction 2 numerator: "))
                den2 = int(input("Fraction 2 denominator: "))
                if(den2==0):
                    raise ValueError
                else:
                    flag=1
            except ValueError:
                print('please enter only an integer and make sure denominator is not 0')
                flag=0  

        fraction2 = Fraction(num2,den2)
        if(operation=="+"):
            newvalues = fraction1+fraction2
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="-"):
            newvalues = fraction1-fraction2
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="*"):
            newvalues = fraction1*fraction2
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="/"):
            newvalues = fraction1/fraction2
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="=="):
            fraction1==fraction2
        elif(operation=="!="):
            result = fraction1.__ne__(fraction2)
            print(result)
        elif(operation=="<"):
            result = fraction1.__lt__(fraction2)
            print(result)
        elif(operation=="<="):
            result = fraction1.__le__(fraction2)
            print(result)
        elif(operation==">"):
            result = fraction1.__gt__(fraction2)
            print(result)
        elif(operation==">="):
            result = fraction1.__ge__(fraction2)
            print(result)

        operation = input("Please enter your next operation (+,-,*,/,==) or any other key to exit the program:  ")

    print(f"So your final result was:  {fraction1}")
    print("Thank you for trying my program have a nice day!")
"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)