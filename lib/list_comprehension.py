#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0 ]
input_num = [0,1,3,5,7,8,9]
output_num=return_evens(input_num)
print(output_num)

pass

def make_exclamation(sentence_list):
    return[sentence + "!" for sentence in sentence_list]
input_sentense=["Hello", "I'm doing great", "Python is fun"]
output_sentense=make_exclamation(input_sentense)
print(output_sentense)

pass