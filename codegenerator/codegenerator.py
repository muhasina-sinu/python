letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

word = input("enter a word: ")
length =len(word) 

print("Encoded word: ",end="")

for x in range(0,length):
    
    for y in range (0,24):
        
        if word[x] == letters [y]:
            print(letters[y+2], end="")
            
        elif word[x] == " ":
            print(" ",end="")
            break
    
    if word[x] == 'z':
        print("b",end = "")
    elif word[x] == "y":
        print("a",end = '')
        
                
print("\n")         
