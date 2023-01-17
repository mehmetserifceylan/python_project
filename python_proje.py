li=[]
def flatten(n):
     for i in n:
         if isinstance(i,list):
          flatten(i)
         else:
          li.append(i)
liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(liste)
print(li)



def reverse_list(n):
 n = n[::-1]
 n = [i[::-1] for i in n]
 return n

liste1=[[1, 2], [3, 4], [5, 6, 7]]


print(reverse_list(liste1))