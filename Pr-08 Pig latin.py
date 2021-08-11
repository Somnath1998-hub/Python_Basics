"""

The Pig Latin language for secret message transfer


Here we convert the message into pig latin language so it will transfer secretly
First we split input sentence into words.
If the word starts with the vowel  then we add ‘yay’ before the word.
Similarly if word starts with consonants then we find first vowel in word then split that word into two part.
We write new word as  part after vowel + the part before vowel + ‘ay’
e.g.
1) Happy new year. => appyhay ewnay earyay. 
2) Hello everyone => ellohay yayeveryone.  
  


"""

# get sentence

original = input("please type a sentence. :").strip().lower()

#split sentence into words

words = original.split()

#loop throug word and convert it into pig latin

new_words =[]

for word in words:
    if word[0] in "aeiou":
        new_word = "yay" + word
        new_words.append(new_word)
        
    else:
        o_pos = 0
        for letter in word:
            if letter not in "aeiou":
                o_pos=o_pos+1
                
            else:
                break
            
        con = word[:o_pos]
        rem = word[o_pos:]
        new_word = rem + con + "ay"
        new_words.append(new_word)

# stick word back together

output = " ".join(new_words)

#output the final string

print(output)
