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
       self.books[self.moretitle] = {self.moreauthor, self.moreprice}
       print(self.books)
       print(self.moretitle, "by", self.moreauthor, "is now in the bookstore")

       
    def sell(self):
       self.moretitle = input ("Sell the book of your choice\n")
       price = input ("Put your price:")
       print(self.moretitle)
       print("The price is now set at", price, "dollars" )
       my_sell.pop 

    def show(self):
       cost = input ("See our prices")
       cost1 = input("\n The Handmaid's Tale = 20$ \n Animal Farm = 25$ \n The Catcher in the Rye = 15$ \n The Great Gatsby = 20$ \n Things Fall Apart = 30$")
       print(cost)
       print(cost1)

    def list(self):
       self.books = input("\n The Handmaid's Tale by M.Atwood \n Animal Farm by G.Orwell \n The Catcher in the Rye by J.D Salinger \n The Great Gatsby by Fitzgerald \n Things Fall Apart by C.Achebe")
       print(self.books)
       my_list = {"\n The Handmaid's Tale by M.Atwood \n Animal Farm by G.Orwell \n The Catcher in the Rye by J.D Salinger \n The Great Gatsby by Fitzgerald \n Things Fall Apart by C.Achebe"}
       my_list.update({'Romeo and Juliet by Shakespeare'})
       print(my_list)


"have the option to save changes" 


    
       
     
    
    
