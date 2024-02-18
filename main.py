import json  # Import the json module to work with JSON files
from rps_game import RPS  # Import the RPS class from the rps_game module

# Function to load the configuration from config.json
def load_config():
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)  # Read and parse the JSON data
    return config_data

# Main function to run the game
def main():
    config = load_config()  # Load the configuration data
    default_choices = config["default_choices"]  # Extract the default choices from the configuration

    # Print a welcome message
    print("Welcome Let's play Rock Paper Scissors")
    
    # Create an instance of the RPS class with the default choices
    play = RPS(default_choices)
    
    # Main game loop
    while True:
        # Prompt the user to enter their choice
        guess = input("Enter rock, paper, scissors, or 'q' to quit: ").lower().strip()
        
        # Check if the user wants to quit
        if guess != 'q':
            # Check if the user's input is a valid choice
            if play.test(guess):
                # Reset the computer's choice and play a round of the game
                play.reset()
                winner = play.game(guess)
                
                # Determine the winner of the round and print the result
                if winner == 2:
                    print("-----------------------------------------")
                    print("Oops, that was a draw!")
                    print(f"Computer   : {play.choice.upper()}")
                    print(f"YOU        : {guess.upper()}")
                    print("-----------------------------------------")
                elif winner == 1:
                    print("-----------------------------------------")
                    print("YOU WON!")
                    print(f"Computer   : {play.choice.upper()}")
                    print(f"YOU        : {guess.upper()}")
                    print("-----------------------------------------")
                else:
                    print("-----------------------------------------")
                    print("YOU LOSE!")
                    print(f"Computer   : {play.choice.upper()}")
                    print(f"YOU        : {guess.upper()}")
                    print("-----------------------------------------")
            else:
                # Print an error message for invalid input
                print("[-] Incorrect keyword")
                print("[!] Choose between", ", ".join(default_choices))
        else:
            # Exit the game if the user chooses to quit
            break
            
    # Print the final results of the game
    print('[+] Results')
    print("-----------------------------------------")
    print(f"Played      : {play.play}")
    print(f"Draw        : {play.draw}")
    print(f"YOU         : {play.user_score()}")
    print(f"Computer    : {play.computer_score()}")
    print("-----------------------------------------")

# Entry point of the script
if __name__ == "__main__":
    main()
