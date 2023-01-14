import random
from string import punctuation

lowerCase1 = chr (random.randint(97,122))
lowerCase2 = chr (random.randint(97,122))
upperCase1 = chr (random.randint(65,90))
upperCase2 = chr (random.randint(65,90))
punctuationSign = chr (random.randint(33,64))
punctuationSign2 = chr (random.randint(33,64))
password = lowerCase1 + lowerCase2 + upperCase1 + upperCase2 + punctuationSign + punctuationSign2
print (password)