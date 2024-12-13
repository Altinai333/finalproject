class Library():
    def __init__(self):
       self.books = {}
       self.moreprice = float(0)
       self.moretitle = ""
       self.moreauthor = ""
       
       
    def add(self):
       print("Add the book of your choice \n")
       self.moretitle = input("Title:")
       self.moreauthor = input("Author:")
       self.moreprice = input("Price:")
       self.books[self.moretitle] = {"writer":self.moreauthor, "price": self.moreprice}
       print(self.books)
       print(self.moreprice)
       print(self.moretitle, "by", self.moreauthor, "is now added to the bookstore")

       
    def sell(self):
       self.moretitle = input ("Sell the book of your choice\n")
       price = input ("Put your price:")
       print(self.moretitle)
       print("You sold your book for", price, "dollars" )
       self.books.pop(self.moretitle)
       print(self.books)

    def show(self):
       cost = input ("See our prices")
       cost1 = input("\n The Handmaid's Tale = 20$ \n Animal Farm = 25$ \n The Catcher in the Rye = 15$ \n The Great Gatsby = 20$ \n Things Fall Apart = 30$")
       print(cost)
       print(cost1)

    def list(self):
       for a in self.books:
          print(a, self.books[a]["writer"])
          print(self.books[a]["price"])


    def options(self):
       myfile = open('myfile.txt', 'w')
       self.books[self.moretitle] = {"writer":self.moreauthor, "price": self.moreprice}
       for a in self.books:
         myfile.write(a)
         myfile.write("\n")
         myfile.write(self.books[a]["writer"])
         myfile.write("\n")
         myfile.write(self.books[a]["price"])
         myfile.write("\n")
       myfile.close()
       myfile.write("\n")
       print(myfile)


       
    






    
       
     
    
    
