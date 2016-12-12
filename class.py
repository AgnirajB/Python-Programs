# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = map(float, raw_input().strip().split())
c,d = map(float, raw_input().strip().split())

class Complex:

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return Complex((self.real+other.real),(self.imag+other.imag))
    def __sub__(self,other):
        return Complex((self.real-other.real),(self.imag-other.imag))
    def __mul__(self,other):
        return Complex(((self.real*other.real)-(self.imag*other.imag)),((self.real*other.imag)+(other.real*self.imag)))
    def __div__(self,other):
        return Complex((((self.real*other.real)+(self.imag*other.imag))/((other.real*other.real)+(other.imag*other.imag))),(((self.imag*other.real)-(self.real*other.imag))/((other.real*other.real)+(other.imag*other.imag))))
    def __mod__(self):
        return Complex(((self.real**2+self.imag**2)**(0.5)),0)
    def __complex__(self):
        if(self.imag >= 0):
            print "%.2f+%.2fi" % (self.real,self.imag)
        else:
            print "%.2f%.2fi" % (self.real,self.imag)

c1 = Complex(a,b)
c2 = Complex(c,d)
Complex.__complex__(Complex.__add__(c1,c2))1
Complex.__complex__(Complex.__sub__(c1,c2))
Complex.__complex__(Complex.__mul__(c1,c2))
Complex.__complex__(Complex.__div__(c1,c2))
Complex.__complex__(Complex.__mod__(c1))
Complex.__complex__(Complex.__mod__(c2))
y
