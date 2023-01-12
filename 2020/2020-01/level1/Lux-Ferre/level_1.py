import nltk

vowels = ["a", "e", "i", "o", "u"]
consonants = ["w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q"]

def main():
   #input_text = "Aberdeen Python is a fun event. We all love coding Python!"
   #input_text = "Aberdeen-way ython-Pay is-way a-way un-fay event-way. e-Way all-way ove-lay oding-cay ython-Pay!"
   menu_choice = input("Do you want to translate to [P]ig-Latin or from Pig-Latin to [E]nglish.")[0]
   input_text = input("What would you like to translate? ")

   if menu_choice.lower() == "p":
      output_string = pig_me(input_text)
   elif menu_choice.lower() == "e":
      output_string = unpig_me(input_text)

   print(output_string)

def pig_me(sentence):
   tokens = nltk.word_tokenize(sentence)
   output_string = ""

   for token in tokens:
      if token[0].lower() in vowels:
         token = token+"-way"
         output_string = output_string + token + " "
      elif token[0].lower() in consonants:
         token = "{}-{}ay ".format(token[1:], token[0])
         output_string = output_string + token
      else:
         output_string = output_string[:-1] + token + " "

   return output_string

def unpig_me(sentence):
   tokens = nltk.word_tokenize(sentence)
   output_string = ""

   for token in tokens:
      if len(token) == 1:
         output_string = output_string[:-1] + token + " "
      elif token[-3].lower() == "w":
         output_string = output_string + token[:-4] + " "
      else:
         output_string = output_string + "{}{} ".format(token[-3],token[:-4])

   return output_string

if __name__ == '__main__':
    main()