# Follower Count Game

## Introduction

Hello! This is a simple Python game where I get to compare two people (or characters) with different follower counts and guess which one has more followers. It's a great way to practice conditional statements, loops, and using functions.

## How the Game Works

1. I start the game by running the `play_game()` function.
2. Two random people (or characters) will appear, each with a description and country.
3. I have to choose whether "A" or "B" has more followers.
4. If I’m correct, I score a point, and the game continues.
5. If I’m wrong, the game ends, and my final score is displayed.

## Code Walkthrough

### 1. Importing Modules and Data

The game imports two main items:
- `random`: For choosing random people or characters.
- `data`: This is a list of dictionaries, where each dictionary holds information like name, description, country, and follower count.

### 2. `dict_a_files()` and `dict_b_files()` Functions

These two functions are used to generate the details for the people shown as "A" and "B" each round. Here's how each function works:

- It randomly picks a person (or character) from the `data` list.
- It formats the information into a printable statement like "Compare A: Name, a description, from country."
- It checks if the description starts with a vowel. If it does, it uses "an"; otherwise, it uses "a."
- It returns the follower count of that person to use in comparisons.

### 3. The `play_game()` Function

This is the main function where the game runs. Here's what it does:

- It shows the game logo and loops through rounds until the player is wrong.
- In each round:
  - It calls the `dict_a_files()` and `dict_b_files()` functions to get the follower counts for "A" and "B".
  - It asks me to guess which one has more followers.
  - If I’m right, I earn a point, and the game continues.
  - If I’m wrong, it ends the game and shows my final score.

### Running the Game

1. Run the `play_game()` function.
2. Follow the prompts in the terminal to make guesses.
3. Keep playing until I guess incorrectly to get the highest score possible!

## Key Concepts I Learned

- **Conditionals**: I used `if` and `else` statements to check if my guesses were correct.
- **Functions**: The game is organized into functions to make the code easier to read and manage.
- **Loops**: A `while` loop allows the game to keep running until the player is wrong.

Happy guessing, and I hope you enjoy playing the Follower Count Game!
