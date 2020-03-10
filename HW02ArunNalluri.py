class Fraction:
    """Class Fraction creates and stores variables while also doing operations with fractions"""
    
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return(f"{self.numerator}/{self.denominator}")
    
    def plus(self,other):
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator+other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def minus(self,other):
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator-other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def times(self,other):
        if(self.denominator*other.denominator<0):
            resultnumerator = -1*self.numerator*other.numerator
            resultdenominator = abs(self.denominator*other.denominator) 
        else:
            resultnumerator = self.numerator*other.numerator
            resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def divide(self,other):
        resultnumerator = self.numerator*other.denominator
        resultdenominator = self.denominator*other.numerator
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def equal(self,other):
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator==other.numerator):
            print("first and 2nd fractions provided are equal")    
        else:
            print("first and 2nd fractions provided are not equal")
        return

def test_suit():
    """This is called to test if the program is functioning properly"""
    
    print("Test 1 for testing multiple additions:")
    print("let first fraction be 1/2")
    fraction1 = Fraction(1,2)
    print("lets perform operation by adding 3/4 to it")
    fraction2 = Fraction(3,4)
    newvalues = fraction1.plus(fraction2)
    fraction1 = Fraction(newvalues[0],newvalues[1])
    print("now lets add 4/4 to the result")
    fraction2 = Fraction(4,4)
    newvalues = fraction1.plus(fraction2)
    fraction1 = Fraction(newvalues[0],newvalues[1])
    print(f"the result should be 72/32 program result is  {fraction1}")
    
    print("Test 2 for testing difference between two fractions:")
    print("let first fraction be 3/2")
    fraction1 = Fraction(3,2)
    print("lets perform operation by subtacting 1/4 from it")
    fraction2 = Fraction(1,4)
    newvalues = fraction1.minus(fraction2)
    fraction1 = Fraction(newvalues[0],newvalues[1])
    print(f"the result should be 10/8 program result is  {fraction1}")
    
    print("Test 3 for testing product of two fractions:")
    print("let first fraction be 3/2")
    fraction1 = Fraction(3,2)
    print("lets perform operation by multiplying it with 1/4")
    fraction2 = Fraction(1,4)
    newvalues = fraction1.times(fraction2)
    fraction1 = Fraction(newvalues[0],newvalues[1])
    print(f"the result should be 3/8 program result is  {fraction1}")
    
    print("Test 4 for testing division operation between two fractions:")
    print("let first fraction be 7/10")
    fraction1 = Fraction(7,10)
    print("lets perform operation by deviding it with 4/5 from it")
    fraction2 = Fraction(4,5)
    newvalues = fraction1.divide(fraction2)
    fraction1 = Fraction(newvalues[0],newvalues[1])
    print(f"the result should be 35/40 program result is  {fraction1}")



def main():
    """Main function takes in two fractions and operation and then calls the appropriate function"""
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
    operation = input("Please enter desired operation (+,-,*,/,==) or any other key to exit the program: ")
    while operation in ['+','-','*','/','==']:
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
            newvalues = fraction1.plus(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="-"):
            newvalues = fraction1.minus(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="*"):
            newvalues = fraction1.times(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="/"):
            newvalues = fraction1.divide(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="=="):
            fraction1.equal(fraction2)
        operation = input("Please enter your next operation (+,-,*,/,==) or any other key to exit the program:  ")

    print(f"So your final result was:  {fraction1}")
    print("Thank you for trying my program have a nice day!")

main()