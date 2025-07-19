msg = input("Enter your message: ")
code = msg.split(" ")
coding = input("1 for coding, 0 for decoding: ")
if coding == "1":
    coding = True
else :
    coding = False

if coding:
    ncodes = []
    for word in code:
        if len(word) >= 3:
            r1 = "sud"
            r2 = "sij"
            nword = r1 + word[:1] + word[0] + r2
            ncodes.append(nword)
        else:
            ncodes.append(word[::-1])
    
    print(" ".join(ncodes))

else:
   
    ncodes = []
    for word in code:
        if len(word) >= 3:
            nword = word[3:-3]
            nword = nword[-1] + nword[:-1]
            ncodes.append(nword)
        else:
            ncodes.append(word[::-1])
    
    print(" ".join(ncodes))

    
