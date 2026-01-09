is_prime=0
n=int(input("Enter a number"))
if n<=1:
    print("Not prime")
else:
    for i in range(2,n+2):
        if n%i==0:
            is_prime=1

            if is_prime:
                print("Prime")
            else:
                print("Not a Prime")
            