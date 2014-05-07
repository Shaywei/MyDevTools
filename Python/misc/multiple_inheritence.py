class A(object):
    def f(self):
        print ('A')

class B(A):
    def f(self):
        print ('B')

class C(A):
    def f(self):
        print ('C')

class D1(B,C):
    pass

class D2(C,B):
    pass

class D3(C,B):
    def f(self):
        print ('D')

if __name__ == '__main__':
    d1 = D1()
    d2 = D2()
    d3 = D3()

    print ('d1: ', D1.__mro__)
    d1.f()

    print ('d2: ', D2.__mro__)
    d2.f()

    print ('d3: ', D3.__mro__)
    d3.f()