s=input("enter the text")
w=s.split()
c={}
for w in w:
    c[w]=c.get(w,0)+1
print("the word is",s,"& the no of occurence of each word in a line of text is:",c)
    
