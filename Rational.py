def gcd(n1,n2):
    n1=abs(n1)
    n2=abs(n2)
    r=1
    while r!=0:
        q=n1//n2
        r=n1-q*n2
        n1=n2
        n2=r
    return n1
class Rational:
    def __init__(self, numerator=0, denominator=1):
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) \
        * int(numerator/divisor)
        self.__denominator = int(abs(denominator)/divisor)
# add a rational number to this rational number
# a/b + c/d = (ad + bc)/bd
    def __add__(self, secondNum):
        print(secondNum)
        print(type(secondNum))
        n = self.__numerator * secondNum[1] + \
        self.__denominator * secondNum[0]
        d = self.__denominator * secondNum[1]
        return Rational(n,d)
# subtract a rational number from this rational number
# a/b - c/d = (ad - bc)/bd
    def __sub__(self, secondNum):
        n = self.__numerator * secondNum[1] - self.__denominator * secondNum[0]
        d = self.__denominator * secondNum[1]
        return Rational(n,d)
# multiply a rational number by this rational number
# a/b * c/d = ac/bd
    def __mul__(self, secondNum):
        n = self.__numerator * secondNum[0]
        d = self.__denominator * secondNum[1]
        return Rational(n,d)
# divide a rational number by this rational number
# (a/b) / (c/d) = ad/bc
    def __truediv__(self, secondNum):
        n = self.__numerator * secondNum[1]
        d = self.__denominator * secondNum[0]
        return Rational(n,d)
# return the rational number as a float
    def __float__(self):
        return self.__numerator / self.__denominator
# return the rational number as an integer
    def __int__(self):
        return int(self.__float__())
# return a string representation of the rational number
    def __str__(self):
        if self.__denominator==1:
            return str(self.__numerator)
        else:
            return str(self.__numerator)+"/"+str(self.__denominator)

# comparison opeators
    def __lt__(self, secondNum):
        return self.cmp(secondNum) < 0
    def __le__(self, secondNum):
        return self.cmp(secondNum) <= 0
    def __gt__(self, secondNum):
        return self.cmp(secondNum) > 0
    def __ge__(self, secondNum):
        return self.cmp(secondNum) >= 0
# compare two numbers
    def cmp(self, secondNum):
        temp = self - secondNum
        if temp[0] > 0: # self > secondNum
            return 1
        elif temp[0] < 0: # self < secondNum
            return -1
        else: # self = seconcNum
            return 0
# return numerator and denominator using an index operator
    def __getitem__(self,index):
        if index==0:
            return self.__numerator
        else:
            return self.__denominator


def main():
    r1 = Rational(6,8)
    r2 = Rational(2,3)
    # Output:
    print("r1 is",r1) # r1 is 3/4
    print("r2 is",r2) # r2 is 2/3
    print(r1,"+",r2,"=",r1+r2) # 3/4 + 2/3 = 17/12
    print(r1,"-",r2,"=",r1-r2) # 3/4 - 2/3 = 1/12
    print(r1,"*",r2,"=",r1*r2) # 3/4 * 2/3 = 1/2
    print(r1,"/",r2,"=",r1/r2) # 3/4 / 2/3 = 9/8
    print(r1,">",r2,"is",r1 > r2) # 3/4 > 2/3 is True
    print(r1,">=",r2,"is",r1 >= r2) # 3/4 >= 2/3 is True
    print(r1,"<",r2,"is",r1 < r2) # 3/4 < 2/3 is False
    print(r1,"<=",r2,"is",r1 <= r2) # 3/4 <= 2/3 is False
    print(r1,"==",r2,"is",r1 == r2) # 3/4 == 2/3 is False
    print(r1,"!=",r2,"is",r1 != r2) # 3/4 != 2/3 is True
    print("int(r2) is", int(r2)) # int(r2) is 0
    print("float(r2) is", float(r2)) # float(r2) is 0.6666666666666666
    print("r2[0] is", r2[0]) # r2[0] is 2
    print("r2[1] is", r2[1])
main()
