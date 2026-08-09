punctuations = '"!@#$%^&*()_+=-:{}|[];<>?,./"'

def punctuation_removal(my_string):
  for char in my_string:
    if char not in punctuations:
      no_punctuation = no_punctuation + char
      print(no_punctuation)

punctuation_removal("Hello!!, he said -- and went.")
