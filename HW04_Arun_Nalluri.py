import unittest


def GCD(x,y):
    """Takes two inputs and returns the Greatest common divisor and returns it"""
    while(y): 
        x, y = y, x % y 
    return x 

class Fraction:
    """Class Fraction creates and stores variables while also doing operations with fractions"""
    
    def __init__(self,numerator,denominator):
        """Initialise the numerator and denominator"""
        self.numerator = numerator
        self.denominator = denominator
        if denominator==0:
            raise ZeroDivisionError("denominator can not be 0")
    
    def __str__(self):
        """Default print function"""
        return(f"{self.numerator}/{self.denominator}")
    
    def __add__(self,other):
        """Adds two fractions using + symbol"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        resultnumerator = numerator+numerator2
        resultdenominator = self.denominator*other.denominator 
        return (Fraction(resultnumerator,resultdenominator).simplify())
         
         

    def __sub__(self,other):
        """subtracts two fractions using - symbol"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        resultnumerator = numerator-numerator2
        resultdenominator = self.denominator*other.denominator 
        return (Fraction(resultnumerator,resultdenominator).simplify())
        

    def __mul__(self,other):
        """Multiplies two fractions using * symbol"""
        if(self.denominator*other.denominator<0):
            resultnumerator = -1*self.numerator*other.numerator
            resultdenominator = abs(self.denominator*other.denominator) 
        else:
            resultnumerator = self.numerator*other.numerator
            resultdenominator = self.denominator*other.denominator 
        return (Fraction(resultnumerator,resultdenominator).simplify())

        
    def __truediv__(self,other):
        """Devides two fraction using / symbol"""
        resultnumerator = self.numerator*other.denominator
        resultdenominator = self.denominator*other.numerator
        return (Fraction(resultnumerator,resultdenominator).simplify())
        
    def __eq__(self,other):
        """takes two fractions and tests if they are equal"""
        numerator1=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator1==numerator2):
            return True
        else:
            return False
                

    def __ne__(self, other): 
        """takes two fractions and tests if they are not equal"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator!=numerator2):
            return True
        else:
            return False
    
    def __lt__(self, other):
        """takes two fractions and tests if first one is less than second"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator<numerator2):
            return True
        else:
            return False
    
    def __le__(self, other): 
        """takes two fractions and tests if first one is less or equal to the second"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator<=numerator2):
            return True
        else:
            return False
    
    def __gt__(self, other):  
        """takes two fractions and tests if first one is greater than second"""       
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator>numerator2):
            return True
        else:
            return False

    def __ge__(self, other): 
        """takes two fractions and tests if first one is greater than or equal to second"""
        numerator=self.numerator*other.denominator
        numerator2=self.denominator*other.numerator
        if(numerator>=numerator2):
            return True
        else:
            return False

    def simplify(self):
        """simplifing the fraction to least common dinominator"""
        theHCF= GCD(self.numerator,self.denominator)
        return Fraction(int(self.numerator/theHCF),int(self.denominator/theHCF))


def count_vowels(s):
    """Used to count the vowels in the sequence"""
    s = s.lower()
    counter=0
    for x in s:
        if(x in ['a','e','i','o','u']):
            counter+=1
    
    return counter

def last_occurrence(target, sequence):
    """Used to return the last occurence of the target in the sequence"""
    counter=0
    if target not in sequence:
        return None
    for x in sequence:
        if x == target:
            result = counter
        counter+=1
    return result

def my_enumerate(seq):   
    """this emulates the enumerate function"""
    counter = 0   
    for k in seq:
        yield(counter,k)
        counter+=1