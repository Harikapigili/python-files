def encryption(s,k):
  s1=""
  for i in s:
    x=ord(i)+k 
    if x<=122:
      s1+=chr(x)
    else:
      x=x-122
      s1+=chr(96+x)
  print(s1)
def decryption(s,k):
  s1=""
  for i in s:
    x=ord(i)-k
    if x>=97:
      s1+=chr(x)
    else:
      x=97-x
      s1+=chr(123-x)
  print(s1)
s=input()
k=int(input())
op=input()
if op=="Encrypt":
  encryption(s,k)
elif op=="Decrypt":
  decryption(s,k)
else:
  print("Incorrect Operation")