# Movie Ticket Booking System
# Demonstrates variables, conditionals, loops, functions and lists

# List of movies
movies = [
    {"name": "Avengers", "price": 10},
    {"name": "Black Panther", "price": 12},
    {"name": "Spider-Man", "price": 11},
    {"name": "The Batman", "price": 13}
]

# List to store bookings
bookings = []


# Function to show movies
def show_movies():
    print("\nAvailable Movies:")
    for i in range(len(movies)):
        movie = movies[i]
        print(i + 1, "-", movie["name"], "- $", movie["price"])


# Function to calculate price
def calculate_total(price, quantity):

    total = price * quantity

    # Discount for group booking
    if quantity >= 5:
        discount = total * 0.10
        total = total - discount
        print("You received a 10% discount!")

    return total


# Function to book ticket
def book_ticket():

    name = input("Enter your name: ")

    show_movies()

    choice = int(input("Select a movie number: "))

    if choice < 1 or choice > len(movies):
        print("Invalid selection.")
        return

    selected_movie = movies[choice - 1]

    quantity = int(input("How many tickets do you want? "))

    total_price = calculate_total(selected_movie["price"], quantity)

    booking = {
        "name": name,
        "movie": selected_movie["name"],
        "tickets": quantity,
        "total": total_price
    }

    bookings.append(booking)

    print("\nBooking Successful!")
    print("Customer:", name)
    print("Movie:", selected_movie["name"])
    print("Tickets:", quantity)
    print("Total Price: $", total_price)


# Function to view bookings
def view_bookings():

    if len(bookings) == 0:
        print("\nNo bookings yet.")
        return

    print("\n===== Booking Summary =====")

    for booking in bookings:
        print(
            "Customer:", booking["name"],
            "| Movie:", booking["movie"],
            "| Tickets:", booking["tickets"],
            "| Total: $", booking["total"]
        )


# Menu display
def show_menu():

    print("\n====== Movie Ticket System ======")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. View My Bookings")
    print("4. Exit")


# Main program loop
def main():

    while True:

        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            show_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Please try again.")


# Run the program
main()