while True:
  word = input("What word would you like to know the length of? \n")
  print('\n' + str(len(word)) + ' letters\n')

  repeat = input('Would you like to run the program again (y/n) \n')
  print('')
  if repeat.lower() == 'n':
    break
  