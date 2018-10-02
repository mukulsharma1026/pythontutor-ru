############ python program for finding factorial #####################################
def fac(n): #recursive function for finding the factorial
  if n <= 1:
    return 1
    
  else :
    return (n*fac(n-1))
    
f = int(input("enter the no. for finding the factorial"))
print(fac(n))

########################################################################
