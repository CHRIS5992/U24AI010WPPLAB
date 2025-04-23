import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "You win this round!"
        else:
            self.computer_wins += 1
            return "Computer wins this round!"

    def has_winner(self):
        return self.user_wins > self.rounds // 2 or self.computer_wins > self.rounds // 2

    def play(self):
        while self.current_round < self.rounds:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice, try again.")
                continue
            
            computer_choice = self.get_computer_choice()
            print("Computer chose:", computer_choice)
            print(self.find_winner(user_choice, computer_choice))

            self.current_round += 1
            if self.has_winner():
                break

        if self.user_wins > self.computer_wins:
            print("You won the game!")
        elif self.computer_wins > self.user_wins:
            print("Computer won the game!")
        else:
            print("It's a tie game!")

game = Rock_paper_scissors(3)
game.play()
