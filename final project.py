from storage import Library 


while True:
  print("\n Welcome to the bookstore")

  person = input("\n A. See our catalog of books \n B. Add books \n C. Sell books \n D.Quit")

  list = "Animal Farm by George Orwell", "The Handmaid's Tale by Margaret Atwood", "The Catcher in the Rye by J.D Salinger", "The Great Gatsby by Fitzgerald", "Things Fall Apart by Chinua Achebe"

  if person == "A":
    print(list)

  if person == "B":
    Library.add()

  if person == "C":
    Library.sell()

  if person == "Q":
    quit()
  







