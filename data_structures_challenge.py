# question 1

#allow the user to enter integers list
numbers = input("Enter integers separated by commas: ")
# split the listof strings
split_strings = numbers.split(",")
# convert split strings to integers
empty_list = []
for number in split_strings:
    empty_list.append(int(number.strip()))

#calculate sum of numbers
total = sum(empty_list)
print("THe total number of inters you have entere is: ", total)

# # QUESTION 2
favorites_books = (
    "Python Crash Course" ,
    "Clean Code",
    "Eloquent JavaScript",
    "JavaScript",
    "Introduction to Algorithms",
)

for book in favorites_books:
    print(book)

# # QUESTION 3
personal_info = {} # initialize empty dict
#prompt user ton enter details below
name = input("Enter your Name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

#store info in the dict
personal_info["name"] = name
personal_info["age"] = age
personal_info["favorite_color"] = favorite_color

#print the output
print("This is your personal information: ")
for key, value in personal_info.items():
    print(key, value)

# QUESTION 4
set1_input = input("Enter numbers seperated by commas: ")
set1 = set(map(int, set1_input.split(",")))

set2_input = input("Enter numbers seperated by commas: ")
set2 = set(map(int, set2_input.split(",")))

common = set1.intersection(set2)
print("THe common elements in your sets are: ", common)

# QUESTION 5

#list of words
words = ["apple", "banana", "orange", "pear", "grape", "kiwi", "pineapple"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)

#week 3 assignment
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    # Prompt the user to enter the original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price after applying the discount, or the original price if no discount was applied
    if final_price != original_price:
        print("Final price after applying discount:", final_price)
    else:
        print("No discount applied. Original price:", original_price)

if __name__ == "__main__":
    main()

    # OOP ASSIGNMENT

    class Book:
        def __init__(self, title, author, publication_year, is_available=True):
            self.title = title
            self.author = author
            self.publication_year = publication_year
            self.is_available = is_available
        
        def check_out(self):
            self.is_available = False
        
        def check_in(self):
            self.is_available = True
        
        def __str__(self):
            availability = "Available" if self.is_available else "Checked Out"
            return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Availability: {availability}"

# Create instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Simulate checking out a book
book1.check_out()

# Simulate returning the book
book1.check_in()

# information about both books
print("Book 1:")
print(book1)
print("\nBook 2:")
print(book2)

