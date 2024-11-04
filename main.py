from art import logo, vs  # Imports the logo and vs ASCII art from the art module
import random  # Imports the random module for selecting random items
from game_data import data  # Imports the data list from the game_data module

# List of vowels used to determine "a" or "an" in descriptions
vowels = ["A", "E", "I", "O", "U"]


# Function to select a random item from data for "A" and format the output
def dict_a_files():
    dict_a = random.choice(data)  # Selects a random dictionary from data
    names = dict_a['name']  # Gets the name of the person/character
    description = dict_a['description']  # Gets the description of the person/character

    # Determines if "a" or "an" should be used based on the first letter of the description
    if description[0] in vowels:
        pronoun_a = "an"
    else:
        pronoun_a = "a"

    country = dict_a['country']  # Gets the country of the person/character
    follower_a = dict_a['follower_count']  # Gets the follower count

    # Creates a formatted string to display details about "A"
    compare_a = f"Compare A: {names}, {pronoun_a} {description}, from {country} "
    print(compare_a)  # Prints the details of "A"
    return follower_a  # Returns the follower count of "A"


# Function to select a random item from data for "B" and format the output
def dict_b_files():
    dict_b = random.choice(data)  # Selects a random dictionary from data
    names = dict_b['name']  # Gets the name of the person/character
    description = dict_b['description']  # Gets the description of the person/character

    # Determines if "a" or "an" should be used based on the first letter of the description
    if description[0] in vowels:
        pronoun_b = "an"
    else:
        pronoun_b = "a"

    country = dict_b['country']  # Gets the country of the person/character
    follower_b = dict_b['follower_count']  # Gets the follower count

    # Creates a formatted string to display details about "B"
    compare_b = f"Against B: {names}, {pronoun_b} {description}, from {country} "
    print(compare_b)  # Prints the details of "B"
    return follower_b  # Returns the follower count of "B"


# Function to start and play the game
def play_game():
    should_continue = True  # Flag to control the game loop
    selected_follower = None  # Variable to hold the follower count of the selected option
    other_follower = None  # Variable to hold the follower count of the non-selected option
    current_score = 0  # Tracks the player's score
    user_answer = ""  # Tracks if the user answer was correct

    print(logo)  # Prints the logo at the start of the game

    while should_continue:
        # Clears the screen and shows the score if the user was right on the previous turn
        if user_answer:
            print("\n" * 100)
            print(logo)
            print(f"You're right, Current Score: {current_score}")

        # Get random follower counts for A and B
        follower_a = dict_a_files()
        print(vs)  # Prints the "vs" ASCII art to show comparison
        follower_b = dict_b_files()

        # Prompts the user to make a choice between "A" or "B"
        user_choice = input("Who has more followers, 'A' or 'B': ").lower()

        # Sets selected_follower and other_follower based on the user's choice
        if user_choice == "a":
            selected_follower = follower_a
            other_follower = follower_b
        elif user_choice == "b":
            selected_follower = follower_b
            other_follower = follower_a

        # Checks if the user's selected follower count is greater than the other
        if selected_follower > other_follower:
            current_score += 1  # Increments score if user is correct
            user_answer = True  # Sets user_answer to True to clear the screen next turn
            continue
        elif selected_follower < other_follower:
            final_score = current_score  # Stores the final score
            print("\n" * 100)
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {final_score}")
            should_continue = False  # Ends the game if the user is wrong


# Starts the game
play_game()
