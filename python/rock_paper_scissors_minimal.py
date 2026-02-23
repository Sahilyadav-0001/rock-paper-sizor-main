import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Set theme colors
        self.bg_color = "white"
        self.text_color = "black"
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.player_choice = ""
        self.computer_choice = ""
        self.choices = ["rock", "paper", "scissors"]
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Score display at the top
        score_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        score_frame.pack(fill="x", pady=(30, 0))
        
        # Player score
        player_frame = tk.Frame(score_frame, bg=self.bg_color)
        player_frame.pack(side="left", expand=True)
        
        player_label = tk.Label(
            player_frame,
            text="player",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        )
        player_label.pack()
        
        self.player_score_label = tk.Label(
            player_frame,
            text="0",
            font=("Arial", 24),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.player_score_label.pack()
        
        # Computer score
        computer_frame = tk.Frame(score_frame, bg=self.bg_color)
        computer_frame.pack(side="left", expand=True)
        
        computer_label = tk.Label(
            computer_frame,
            text="computer",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        )
        computer_label.pack()
        
        self.computer_score_label = tk.Label(
            computer_frame,
            text="0",
            font=("Arial", 24),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.computer_score_label.pack()
        
        # Tie score
        tie_frame = tk.Frame(score_frame, bg=self.bg_color)
        tie_frame.pack(side="left", expand=True)
        
        tie_label = tk.Label(
            tie_frame,
            text="tie",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        )
        tie_label.pack()
        
        self.tie_score_label = tk.Label(
            tie_frame,
            text="0",
            font=("Arial", 24),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.tie_score_label.pack()
        
        # Result display in the middle
        self.result_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.result_frame.pack(expand=True, fill="both")
        
        self.result_label = tk.Label(
            self.result_frame,
            text="Choose your move",
            font=("Arial", 24),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.result_label.pack(pady=50)
        
        # Hand icons at the bottom
        hand_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        hand_frame.pack(side="bottom", fill="x", pady=(0, 50))
        
        # Create hand buttons
        self.create_hand_buttons(hand_frame)
        
    def create_hand_buttons(self, parent_frame):
        # Create a frame for the hand buttons
        button_frame = tk.Frame(parent_frame, bg=self.bg_color)
        button_frame.pack()
        
        # Rock button (fist)
        rock_frame = tk.Frame(button_frame, bg=self.bg_color)
        rock_frame.pack(side="left", padx=50)
        
        rock_button = tk.Button(
            rock_frame,
            text="✊",
            font=("Arial", 60),
            bg=self.bg_color,
            fg=self.text_color,
            bd=0,
            command=lambda: self.play("rock")
        )
        rock_button.pack()
        
        # Paper button (open hand)
        paper_frame = tk.Frame(button_frame, bg=self.bg_color)
        paper_frame.pack(side="left", padx=50)
        
        paper_button = tk.Button(
            paper_frame,
            text="✋",
            font=("Arial", 60),
            bg=self.bg_color,
            fg=self.text_color,
            bd=0,
            command=lambda: self.play("paper")
        )
        paper_button.pack()
        
        # Scissors button (peace sign)
        scissors_frame = tk.Frame(button_frame, bg=self.bg_color)
        scissors_frame.pack(side="left", padx=50)
        
        scissors_button = tk.Button(
            scissors_frame,
            text="✌️",
            font=("Arial", 60),
            bg=self.bg_color,
            fg=self.text_color,
            bd=0,
            command=lambda: self.play("scissors")
        )
        scissors_button.pack()
        
    def play(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.choices)
        
        result = self.determine_winner(self.player_choice, self.computer_choice)
        self.update_scores(result)
        self.update_display(result)
        
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"
            
    def update_scores(self, result):
        if result == "win":
            self.player_score += 1
            self.player_score_label.config(text=str(self.player_score))
        elif result == "lose":
            self.computer_score += 1
            self.computer_score_label.config(text=str(self.computer_score))
        else:  # tie
            self.tie_score += 1
            self.tie_score_label.config(text=str(self.tie_score))
            
    def update_display(self, result):
        # Convert choices to emoji
        player_emoji = self.choice_to_emoji(self.player_choice)
        computer_emoji = self.choice_to_emoji(self.computer_choice)
        
        if result == "win":
            result_text = f"{player_emoji} x {computer_emoji}\nYou win!"
        elif result == "lose":
            result_text = f"{player_emoji} x {computer_emoji}\nComputer wins!"
        else:  # tie
            result_text = f"{player_emoji} x {computer_emoji}\ntie"
            
        self.result_label.config(text=result_text)
        
    def choice_to_emoji(self, choice):
        if choice == "rock":
            return "✊"
        elif choice == "paper":
            return "✋"
        else:  # scissors
            return "✌️"
        
def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
