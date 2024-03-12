def enqueue(l):
  item=int(input())
  l.append(item)
  display(l)
def dequeue(l):
  l.pop(0)
  display(l)
def display(l):
  for i in l:
    print(i,end=" ")
  print()
l=[]
while(True):
  x=input()
  if x=="enqueue":
    enqueue(l)
  elif x=="dequeue":
    dequeue(l)
  elif x=="exit":
    break
  else:
    print("Incorect Input")
  