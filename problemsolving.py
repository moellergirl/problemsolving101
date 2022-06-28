# 1.	Reverse a string (HINT: Review the Algorithms + Problem Solving PowerPoint!)
    #    a.	Write code that takes a string as input and returns the string reversed
    #   b.	i.e. “Hello” will be returned as “olleH”

    #find the index of the last letter of word
    # last_index= [len(word)-1]
    #print each letter one at a time 
    # word='Hello'
    #print hello from the 4 index to 0 index in a for loop
    # for index in range(len(word)-1,-1,-1):
        # print(word[index])

word='Hello'
reversed_word=''
for index in range(len(word)-1,-1,-1):
    reversed_word +=word[index]
print (reversed_word)




#2.	Capitalize letter
# a.	Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
    # - write out string with two words all lower case
my_words='fat bottom'
# both the first letters of each word need to be converted from lower case to upper case. 'Fat Bottom" How do I get the first letter of each word to convert into capital letters? I could use index to get to a single letter of each word.
#find the leangth of the words so I can calculate which index space needs to be capitialized. Count letters and spaces? 
my_words='fat bottom'
x=len(my_words)
print (x)
#now I need to identify at what positon 'f' and 'b' are located
my_words='fat bottom'
x=my_words.find('f','b')
print(x)


