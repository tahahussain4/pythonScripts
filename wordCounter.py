#Word  counter
line = "dsdadsds dnslfdksmdlk f f"
wordArray = []
wordArrayCounter = 0
word = ""
##for i in range(0,len(line)):
##    if(line[len(line) - i - 1] == ' '):
##        if(word != ''):
##            wordArray.append(word)
##        word = ""
##    else:
##        word = word + (line[len(line)-i-1])
def appendWord(array,word):
     if(word != '' and isinstance(array,list)):
        array.append(word)

wordArray = []
for characterPos in range(len(line)):
    character = line[characterPos]
    if(character == ' '):
        appendWord(wordArray,word)
        word = ""
    else:
        word = word + (character)

    if(characterPos == len(line)-1):
        appendWord(wordArray,word)
        word = "" 
    


#CEHCK RESULT
for word in wordArray :
    print word

print len(wordArray)

