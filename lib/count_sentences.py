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
        last_character = self.value[len(self.value)-1]
        return last_character == "."
        # self.value.endswith(".")
    
    def is_question(self):
        last_character = self.value[len(self.value)-1]
        return last_character == "?"
        # self.value.endswith(".")

    def is_exclamation(self):
        last_character = self.value[len(self.value)-1]
        return last_character == "!"
        # self.value.endswith(".")


    def count_sentences(self):
        # re solution
        # sentence_list = re.split('[?!.]', self.value)
        # print(sentence_list)
        # return len([sentence for sentence in sentence_list if sentence])

        # replace/split
        transformed_sentence = self.value.replace('!','.').replace('?', '.')
        print(transformed_sentence)
        sentence_list = transformed_sentence.split('.')
        print(sentence_list)
        actual_sentences = []
        for sentence in sentence_list:
            if sentence != '':
                actual_sentences.append(sentence)
        return len(actual_sentences)

        # actual_sentences = [sentence for sentence in sentence_list if sentence != '']
        
        ## counting solution
       
            

        
  



string = MyString('This, well, is a sentence. This')
