a=int(input("enetr value for a"))
b=int(input("enter value for b"))
for i in range(1,min(a,b)+1):
      if a %i==0 and b%i==0:
         gcd=i
print(gcd)
