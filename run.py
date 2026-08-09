punctuations = '"!@#$%^&*()_+=-:{}|[];<>?,./"'
my_string = "Hello!!, he said -- and went."
no_punctuation = ""
for char in my_string:
  if char not in punctuations:
    no_punctuation = no_punctuation + char
    print(no_punctuation)
