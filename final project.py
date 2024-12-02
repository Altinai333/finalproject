from storage import Library 

data = Library()

while True:
  print("\n Welcome to the bookstore !")

  person = input("\n A. See our catalog of books \n B. Add books \n C. Sell books \n D. See the price of our books \n E.Quit \n Enter the letter that corresponds to your choice: " " ")

  if person == "A":
    print("Here are the books we have:\n") 
    data.list()

  elif person == "B":
    data.add()

  elif person == "C":
    data.sell()

  elif person == "D":
    data.show()

  elif person == "E":
    quit()
  

