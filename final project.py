from storage import Library 


while True:
  print("\n Welcome to the bookstore !")

  person = input("\n A. See our catalog of books \n B. Add books \n C. Sell books \n D. See the price of our books \n E.Quit \n Enter the letter that corresponds to your choice: " " ")

  if person == "A":
    print("Here are the books we have:\n") 
    Library.list(self)

  elif person == "B":
    Library.add(self)

  elif person == "C":
    Library.sell(self)

  elif person == "D":
    Library.show(self)

  elif person == "E":
    quit()
  







