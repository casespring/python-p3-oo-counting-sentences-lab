#!/usr/bin/env python3

import re
class MyString:

    def __init__(self,value='') -> None:
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        # last_character = self.value[-1]
        # return self.value[-1] == "."
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        '''
        "This is a string! It has three sentences. Right?"
        --> 3
        "a. b..."
        --> 2
        "a.b..c".split('.')
        ['a','b','','c']
        '''
        # re solution
        sentence_list = re.split('[?!.]', self.value)
        print(sentence_list)
        return len([sentence for sentence in sentence_list if sentence])

        # replace/split solution
        # transformed_sentence = self.value.replace('!','.').replace('?','.')
        # print(transformed_sentence)
        # sentence_list = transformed_sentence.split('.')
        # print(sentence_list)
        # actual_sentences = []
        # for sentence in sentence_list:
        #     if sentence != '':
        #         actual_sentences.append(sentence)
        # actual_sentences = [sentence for sentence in sentence_list if sentence != '']
        # return len(actual_sentences)
        # counting solution
        # count = 0
        # prev_char = ''
        # for char in self.value:
        #     if char in ['.','?','!'] and prev_char.isalpha():
        #         count += 1
        #     prev_char = char
        # return count


string = MyString('Hello World...')
import ipdb; ipdb.set_trace()
print(string.count_sentences())
