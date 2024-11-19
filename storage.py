class Library():
    def __init__(self):
       self._Books = {}
       self._Price = float(0)
       

    def add(self):

      print("Add the book of your choice \n")
      moretitle = input("Title:")
      moreauthor = input("Author:")
      moreprice = input("Price:")
      print(moretitle)
      print(moreauthor)
      print(moreprice)


    def sell(self):
       market = input ("Sell the book of your choice\n")
       price = input ("Put your price:")
       print(market)
       print("The price is now set at", price, "dollars" )

    def show(self):
       cost = input ("See our prices")
       cost1 = input("\n The Handmaid's Tale = 20$ \n Animal Farm = 25$ \n The Catcher in the Rye = 15$ \n The Great Gatsby = 20$ \n Things Fall Apart = 30$")
       print(cost)
       print(cost1)

    def list(self):
       books = input ("\n The Handmaid's Tale by M.Atwood \n Animal Farm by G.Orwell \n The Catcher in the Rye by J.D Salinger \n The Great Gatsby by Fitzgerald \n Things Fall Apart by C.Achebe")
       print(books)

    
       
     
    
    
""" 
    
     
    def books():  """