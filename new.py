text = 'hello sanchez martin '
shifted = 3 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def myEncyption():
  for char in text:
    a = alphabet.find(char)
    print (a,char)
myEncyption()