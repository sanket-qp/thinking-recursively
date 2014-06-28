def combinations(s):
  if not s:
    return []
  # base case, for string of length 2
  elif (len(s) == 2):
    # combinations are , (string itself, first character, second charactor)
    return [s, s[0], s[1]]
  else:
    # recursive case, combinatons can be generated by combining first character AND combinations of rest of the string
    first_char = s[0]
    # combinations of rest of the string
    l = combinations(s[1:])
    # first character is itself is part of a combinations
    l.append(first_char)
    # combine first_char and rest of the combinations, also make sure not to combine first_char with ifself
    # also we don't want to forget previous combinations so extending the current list of combinations
    l.extend(["%s" % (first_char + c) for c in l if c != first_char])
    return l

def main():
  print combinations("w")

if __name__ == "__main__":
  main()
