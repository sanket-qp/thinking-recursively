from array import *

def get_char(digit, index): 
  """
  returns a character mapped to a digit on a telephone for given index
  """
  mapping = { '0':None, '1':None, '2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PRS', '8':'TUV', '9':'WXY'}
  chars = mapping.get(digit, None)
  return chars[index] if chars and index < len(chars) else None

def generate_words(digits, index, words, word):
  """
  generates words for given digits
  """
  # base case, when index reachs to the end of the word, get the word temporarily generated in the array
  if index == len(digits):    
    words.append(''.join(word))
    return
  else:
    # recursively call for each position in the word
    for i in range(3):
      ch = get_char(digits[index], i)
      # temporarily save the word in an array
      if ch: word[index] = ch
      generate_words(digits, index+1, words, word)

def main():
  digits = "484"
  words = []
  word = array('c', [' ' for _ in digits])
  generate_words(digits, 0, words, word)
  print "words : %s" % (words)

if __name__ == "__main__":
  main()
