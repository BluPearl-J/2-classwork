#4
#using FILTER() CREATE A PYTHON FUNCTION
#THAT FILTERS ALL THE WORDS WITH MORE THAN 5 CHARACTERS FROM THE FOLLOWING LIST
#SAMPLE
#WORDS=["apple","banana","kiwi","grapes","cherry"]
#output: ["apple","kiwi"]
def filter_words (arr):
 for word in arr:
  if (len(word))>5:
    result=(map(filter_words, word))
    answer=(map(filter_words, word))
    return(result)
    print(answer)
    


words_array=["apple","banana","kiwi","grapes","cherry"]
print(filter_words(words_array))
