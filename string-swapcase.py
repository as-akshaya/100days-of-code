sentence = input("enter the string:")
#''.join(c.lower() if c.isupper() else c.upper() for c in sentence)
new =sentence.swapcase() 
print(new)