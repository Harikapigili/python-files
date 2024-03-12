def push(l):
  item=int(input())
  l.append(item)
  display(l)
def pop(l):
  l.remove(l[-1])
  display(l)
def peek(l):
  print("Top:",l[-1])
def display(l):
  for i in l:
    print(i,end=" ")
  print()
s,l="",[]
while s !="exit":
  x=input()
  if x=="push":
    push(l)
  elif x=="pop":
    pop(l)
  elif x=="peek":
    peek(l)
  elif x=="display":
    display(l)
  elif x=="exit":
    s="exit"
  else:
    print("Incorect input")
  
  
 