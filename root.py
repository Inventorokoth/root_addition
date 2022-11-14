"""add the individual numbers of a given number till only one number remains and cant be added any more
"""
#definging the integers

#definig the main function to add those numbers
num=str(input('enter the number'))  
def root(num):
   array=[]
   sum=0
   for x in num:
      array.append(int(x))
      print(array)
      length=array.__len__()
      c=length-1
      print(c)
      sum=sum +array[c]
   if sum>9:
      new=str(sum)
      root(new)
   else:
      print(sum) 
root(num)