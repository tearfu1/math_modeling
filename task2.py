a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

if (a+b > c and a+c > b and b+c > a):
    print ("est'")
    if a==b==c:
        print('равносторонний')
    elif a==b or a==c or b==c:
        print('равнобедренный')
    else:
        print('никакой')
else:
    print('net')

    