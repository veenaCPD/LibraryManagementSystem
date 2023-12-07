import pickle
import os

##########      Books section  ##########


## Add new book in the register
def add_book():
    try:
        book_no = input("Enter Book No. > ")
        book_name = input("Enter Book Name > ")
        book = [book_no , book_name ]
		
		# Open a Books DB in Write mode
        file = open('books.dat', 'ab')
        pickle.dump(book, file)
        file.close()
        print ("Book added")
    except ValueError:
        print("Invalid input")
        
		

## Display all the available books in the register        
def display_all():
    
        # Open a Books DB in Read mode
        with open('books.dat', 'rb') as file:
            try:
                while True:
                    books = pickle.load(file)
                    print(books)
            except EOFError:
                print("")
        
     

## Search for a specific book , give either book no. or book name as search criteria	 
def search_book(booksearchtxt):
        with open("books.dat", 'rb') as file:
            try:
                while True:
                    books = pickle.load(file)
                    if (books[0] == booksearchtxt or books[1] == booksearchtxt) :
                        print ("Book no. = " + books[0])
                        print("Book name = " + books[1])
                        print("We have your book !!!\n")
                        break
            except EOFError:
                print("")
				
				
				
        
        
  ##########      Members section  ##########      
        
		
## Add new member to library		
def add_member():
    try:
        
        member_no = input("Enter registration no. > ")
        member_name = input("Enter member name > ")
        member = [member_no + ":" +  member_name ]
        file = open('members.dat', 'ab')
        pickle.dump(member,file)
        file.close()
        print ("Member added\n")
    except ValueError:
        print("Invalid input")
        
		
		
		
		
   ##########      Transactions section  ##########   
   
   
## Issue book to a member   
def issue_book():
    
    try:
        book_no = input("Enter Book No. > ")
        member_no = input("Enter Member No. > ")
        
        book = [book_no , member_no]
        file = open('issuebooks.dat', 'ab')
        pickle.dump(book, file)
        file.close()
        print ("Book issued")
    except ValueError:
        print("Invalid input")
        


## Return book from member
def return_book():
    
    try:
        book_no = input("Enter Book No. > ")
        member_no = input("Enter Member No. > ")
        
        book = [book_no, member_no]
        file = open('returnedbooks.dat', 'ab')
        pickle.dump(book, file)
        file.close()
        print ("Book returned")
    except ValueError:
        print("Invalid input")        
                
				

##########      Main entry point , execution will start form here  ##########  


## While loop will run till user enter either 'q' or 'Q'
                
while True:
    print("Welcome to Veena's Library !!!")
    print("1 : Add book in register")
    print("2 : Show all books from register")
    print("3 : Search for book in register")
    print("4 : Register new member")
    print("5 : Issue book")
    print("6 : Return book")
    
    print("Q : Quit")
    ch = input("Enter choice > ")
    
    if (ch == '1'):        
        add_book()
    elif (ch == '2'):
        display_all()
    elif (ch == '3'):
        searchtext = input("Enter book no. or book name > ")
        search_book(searchtext)
    elif (ch == '4'):
        add_member()
    elif (ch == '5'):
        issue_book()
    elif (ch == '6'):
        return_book()
    elif(ch == 'q' or ch == 'Q'):
        print("Have a nice day !!! Bye Bye !!!")
        break