def rotate(s, index):
  """
  rotates a word from given index onwards
  example:
  "abcd" => length: 4, here is what happens if we rotate this word 4 times
  "bcda"
  "cdab"
  "dabc"
  "abcd" => after 4th rotation, it becomes the original word
  """
  # we'll have to split the list from index so that we can only rotate the charaters starting after index
  left = s[:index]
  right = s[index:]

  # shift each character to the left
  # "abcd" => "bcda"
  rotated = right[1:]
  #rotated.append(right[0])
  rotated += right[0]
  # merged the rotated and left to form a complete word
  s = left + rotated
  return s
    

def permute(s, index, final):
  # base case
  if index == len(s) - 1:
    final.append(s)
    return
  else:
    # recursive case
    for i in range(index, len(s)):
      # rotate the word for it's length
      s = rotate(s, index)
      # permute the rest of the word (index + 1)
      permute(s, index + 1, final)

def permute_string(s):
  # just convert the string in to list so we can access it by index
  permutations = []
  permute(s, 0, permutations)
  print permutations

def main():
  permute_string("abcd")

if __name__ == "__main__":
  main()
