from player import get_player_choice
from computer import get_computer_choice
from logic import logic
def main():
    print("Wekcome to Rock, Paper, Scissiors!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice =get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = logic(player_choice, computer_choice)
        print(result)
        if result == "Player wins!":
            player_score += 1 
        elif result == "Computer wins!":
            computer_score += 1
        print(f"score - Player: {player_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? Yes/No:").strip().lower()
        if play_again == "Yes".lower():
            continue
        else :
            print("Thanks for playing!")
            return
        
if __name__== "__main__":  main()