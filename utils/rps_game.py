import random  # Import the random module for generating random choices

# Define the Rock Paper Scissors game class
class RPS:
    
    # Initialize the game state
    def __init__(self, choices=('rock', 'paper', 'scissors')) -> None:
        self.user_wins = 0  # Initialize the user's wins counter
        self.computer_wins = 0  # Initialize the computer's wins counter
        self.draw = 0  # Initialize the draw counter
        self.play = 0  # Initialize the total number of plays counter
        self.data = choices  # Set the available choices for the game
        self.choice = str  # Initialize the computer's choice
    
    # Method to play a round of the game
    def game(self, guess: str) -> int:
        self.play +=1  # Increment the total number of plays counter
        
        # Check if the user's guess matches the computer's choice
        if guess == self.choice:
            self.draw += 1  # Increment the draw counter
            return 2  # Return 2 to indicate a draw
        # Check if the user wins
        elif guess == self.data[0] and self.choice == self.data[2]:
            self.user_wins += 1  # Increment the user's wins counter
            return 1  # Return 1 to indicate user win
        elif guess == self.data[1] and self.choice == self.data[0]:
            self.user_wins += 1  # Increment the user's wins counter
            return 1  # Return 1 to indicate user win
        elif guess == self.data[2] and self.choice == self.data[1]:
            self.user_wins += 1  # Increment the user's wins counter
            return 1  # Return 1 to indicate user win
        # If none of the above conditions are met, the computer wins
        else:
            self.computer_wins +=1  # Increment the computer's wins counter
            return 0  # Return 0 to indicate computer win
        
    # Method to validate user input
    def test(self,guess: str) -> bool :
        # Check if the user's guess is in the list of available choices
        if guess in self.data:
            return True  # Return True if the guess is valid
        else:
            return False  # Return False if the guess is invalid
    
    # Method to get the user's score
    def user_score(self) -> int:
        return self.user_wins  # Return the number of user wins
    
    # Method to get the computer's score
    def computer_score(self) -> int:    
        return self.computer_wins  # Return the number of computer wins
    
    # Method to get the total number of plays
    def plays(self) -> int:
        return self.play  # Return the total number of plays
    
    # Method to reset the computer's choice
    def reset(self) -> None:
        self.choice = random.choice(self.data)  # Choose a random choice for the computer
    
    # Method to represent the object as a string
    def __str__(self):
        return "The Brain "  # Return a string representation of the object
