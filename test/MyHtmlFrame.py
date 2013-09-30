__author__ = 'lidong'
def aa(x,y,*z,**m):

    print("x"+x)

    print("y"+y)

    print(z)

    print(m)

username=raw_input("your name")

print(aa(username,"2","3","4","5",ss=9,sdas=20))