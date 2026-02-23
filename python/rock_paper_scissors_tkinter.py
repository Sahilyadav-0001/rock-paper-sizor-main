import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk, ImageDraw
import os

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Set theme colors
        self.bg_color = "#f0f0f0"
        self.accent_color = "#3498db"
        self.button_color = "#2980b9"
        self.hover_color = "#1c6ea4"
        self.win_color = "#2ecc71"
        self.lose_color = "#e74c3c"
        self.tie_color = "#9b59b6"
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create frames
        self.create_frames()
        
        # Show menu frame
        self.show_menu()
        
    def create_frames(self):
        # Menu Frame
        self.menu_frame = tk.Frame(self.root, bg=self.bg_color)
        self.create_menu_widgets()
        
        # Game Frame
        self.game_frame = tk.Frame(self.root, bg=self.bg_color)
        self.create_game_widgets()
        
        # Result Frame
        self.result_frame = tk.Frame(self.root, bg=self.bg_color)
        self.create_result_widgets()
    
    def create_menu_widgets(self):
        # Title
        title_label = tk.Label(
            self.menu_frame, 
            text="ROCK PAPER SCISSORS",
            font=("Arial", 36, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            pady=20
        )
        title_label.pack(pady=50)
        
        # Start Game Button
        self.start_button = tk.Button(
            self.menu_frame,
            text="Start Game",
            font=("Arial", 16),
            bg=self.button_color,
            fg="white",
            padx=20,
            pady=10,
            bd=0,
            command=self.show_game
        )
        self.start_button.pack(pady=20)
        
        # Quit Button
        self.quit_button = tk.Button(
            self.menu_frame,
            text="Quit",
            font=("Arial", 16),
            bg=self.lose_color,
            fg="white",
            padx=20,
            pady=10,
            bd=0,
            command=self.root.destroy
        )
        self.quit_button.pack(pady=20)
        
        # Add hover effects
        self.add_hover_effect(self.start_button, self.hover_color)
        self.add_hover_effect(self.quit_button, "#c0392b")
    
    def create_game_widgets(self):
        # Score Frame
        score_frame = tk.Frame(self.game_frame, bg=self.bg_color)
        score_frame.pack(pady=20, fill="x")
        
        # Player Score
        self.player_score_label = tk.Label(
            score_frame,
            text=f"Player: {self.player_score}",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.player_score_label.pack(side="left", padx=100)
        
        # Computer Score
        self.computer_score_label = tk.Label(
            score_frame,
            text=f"Computer: {self.computer_score}",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.computer_score_label.pack(side="right", padx=100)
        
        # Title
        title_label = tk.Label(
            self.game_frame, 
            text="MAKE YOUR CHOICE",
            font=("Arial", 24, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # Create and display choice images
        self.images = {}
        self.create_choice_images()
        
        # Choices Frame
        choices_frame = tk.Frame(self.game_frame, bg=self.bg_color)
        choices_frame.pack(pady=20)
        
        # Rock Button
        rock_frame = tk.Frame(choices_frame, bg=self.bg_color)
        rock_frame.pack(side="left", padx=30)
        
        rock_image_label = tk.Label(rock_frame, image=self.images["rock"], bg=self.bg_color)
        rock_image_label.pack(pady=10)
        
        self.rock_button = tk.Button(
            rock_frame,
            text="Rock",
            font=("Arial", 14),
            bg=self.button_color,
            fg="white",
            padx=15,
            pady=5,
            bd=0,
            command=lambda: self.play("rock")
        )
        self.rock_button.pack()
        
        # Paper Button
        paper_frame = tk.Frame(choices_frame, bg=self.bg_color)
        paper_frame.pack(side="left", padx=30)
        
        paper_image_label = tk.Label(paper_frame, image=self.images["paper"], bg=self.bg_color)
        paper_image_label.pack(pady=10)
        
        self.paper_button = tk.Button(
            paper_frame,
            text="Paper",
            font=("Arial", 14),
            bg=self.button_color,
            fg="white",
            padx=15,
            pady=5,
            bd=0,
            command=lambda: self.play("paper")
        )
        self.paper_button.pack()
        
        # Scissors Button
        scissors_frame = tk.Frame(choices_frame, bg=self.bg_color)
        scissors_frame.pack(side="left", padx=30)
        
        scissors_image_label = tk.Label(scissors_frame, image=self.images["scissors"], bg=self.bg_color)
        scissors_image_label.pack(pady=10)
        
        self.scissors_button = tk.Button(
            scissors_frame,
            text="Scissors",
            font=("Arial", 14),
            bg=self.button_color,
            fg="white",
            padx=15,
            pady=5,
            bd=0,
            command=lambda: self.play("scissors")
        )
        self.scissors_button.pack()
        
        # Menu Button
        self.menu_button = tk.Button(
            self.game_frame,
            text="Back to Menu",
            font=("Arial", 12),
            bg="#7f8c8d",
            fg="white",
            padx=10,
            pady=5,
            bd=0,
            command=self.reset_and_show_menu
        )
        self.menu_button.pack(pady=30)
        
        # Add hover effects
        self.add_hover_effect(self.rock_button, self.hover_color)
        self.add_hover_effect(self.paper_button, self.hover_color)
        self.add_hover_effect(self.scissors_button, self.hover_color)
        self.add_hover_effect(self.menu_button, "#616a6b")
    
    def create_result_widgets(self):
        # Result Title
        self.result_title = tk.Label(
            self.result_frame, 
            text="RESULT",
            font=("Arial", 24, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        self.result_title.pack(pady=20)
        
        # Score Frame
        score_frame = tk.Frame(self.result_frame, bg=self.bg_color)
        score_frame.pack(pady=10, fill="x")
        
        # Player Score
        self.result_player_score = tk.Label(
            score_frame,
            text=f"Player: {self.player_score}",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.result_player_score.pack(side="left", padx=100)
        
        # Computer Score
        self.result_computer_score = tk.Label(
            score_frame,
            text=f"Computer: {self.computer_score}",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.result_computer_score.pack(side="right", padx=100)
        
        # Choices Frame
        self.choices_result_frame = tk.Frame(self.result_frame, bg=self.bg_color)
        self.choices_result_frame.pack(pady=20)
        
        # Player Choice
        player_choice_frame = tk.Frame(self.choices_result_frame, bg=self.bg_color)
        player_choice_frame.pack(side="left", padx=50)
        
        self.player_choice_label = tk.Label(
            player_choice_frame,
            text="You chose:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.player_choice_label.pack()
        
        self.player_choice_image = tk.Label(player_choice_frame, bg=self.bg_color)
        self.player_choice_image.pack(pady=10)
        
        # Computer Choice
        computer_choice_frame = tk.Frame(self.choices_result_frame, bg=self.bg_color)
        computer_choice_frame.pack(side="right", padx=50)
        
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            text="Computer chose:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.computer_choice_label.pack()
        
        self.computer_choice_image = tk.Label(computer_choice_frame, bg=self.bg_color)
        self.computer_choice_image.pack(pady=10)
        
        # Result Text
        self.result_text = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 20, "bold"),
            bg=self.bg_color
        )
        self.result_text.pack(pady=20)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.result_frame, bg=self.bg_color)
        buttons_frame.pack(pady=20)
        
        # Play Again Button
        self.play_again_button = tk.Button(
            buttons_frame,
            text="Play Again",
            font=("Arial", 14),
            bg=self.win_color,
            fg="white",
            padx=15,
            pady=5,
            bd=0,
            command=self.show_game
        )
        self.play_again_button.pack(side="left", padx=20)
        
        # Menu Button
        self.result_menu_button = tk.Button(
            buttons_frame,
            text="Main Menu",
            font=("Arial", 14),
            bg=self.tie_color,
            fg="white",
            padx=15,
            pady=5,
            bd=0,
            command=self.reset_and_show_menu
        )
        self.result_menu_button.pack(side="left", padx=20)
        
        # Add hover effects
        self.add_hover_effect(self.play_again_button, "#27ae60")
        self.add_hover_effect(self.result_menu_button, "#8e44ad")
    
    def create_choice_images(self):
        # Create directory for images if it doesn't exist
        if not os.path.exists('images'):
            os.makedirs('images')
        
        # Create images if they don't exist
        self.create_rock_image()
        self.create_paper_image()
        self.create_scissors_image()
        
        # Load images
        for choice in self.choices:
            image = Image.open(f"images/{choice}.png")
            image = image.resize((100, 100), Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.ANTIALIAS)
            self.images[choice] = ImageTk.PhotoImage(image)
    
    def create_rock_image(self):
        if not os.path.exists('images/rock.png'):
            image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            
            # Draw rock (circle)
            draw.ellipse((20, 20, 180, 180), fill=(173, 216, 230))
            draw.ellipse((20, 20, 180, 180), outline=(0, 0, 0), width=3)
            
            # Save image
            image.save('images/rock.png')
    
    def create_paper_image(self):
        if not os.path.exists('images/paper.png'):
            image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            
            # Draw paper (rectangle with lines)
            draw.rectangle((20, 20, 180, 180), fill=(255, 255, 200))
            draw.rectangle((20, 20, 180, 180), outline=(0, 0, 0), width=3)
            
            # Add lines to make it look like paper
            for i in range(40, 180, 30):
                draw.line((40, i, 160, i), fill=(0, 0, 0), width=2)
            
            # Save image
            image.save('images/paper.png')
    
    def create_scissors_image(self):
        if not os.path.exists('images/scissors.png'):
            image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            
            # Draw scissors (two ellipses)
            draw.ellipse((30, 50, 170, 110), fill=(200, 255, 200))
            draw.ellipse((30, 50, 170, 110), outline=(0, 0, 0), width=3)
            
            draw.ellipse((30, 90, 170, 150), fill=(200, 255, 200))
            draw.ellipse((30, 90, 170, 150), outline=(0, 0, 0), width=3)
            
            # Add a small circle for the pivot
            draw.ellipse((90, 90, 110, 110), fill=(50, 50, 50))
            draw.ellipse((90, 90, 110, 110), outline=(0, 0, 0), width=2)
            
            # Save image
            image.save('images/scissors.png')
    
    def add_hover_effect(self, button, hover_color):
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=button["bg"]))
    
    def show_menu(self):
        self.game_frame.pack_forget()
        self.result_frame.pack_forget()
        self.menu_frame.pack(fill="both", expand=True)
    
    def show_game(self):
        self.menu_frame.pack_forget()
        self.result_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        
        # Update score labels
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
    
    def show_result(self, player_choice, computer_choice, result):
        self.menu_frame.pack_forget()
        self.game_frame.pack_forget()
        self.result_frame.pack(fill="both", expand=True)
        
        # Update score labels
        self.result_player_score.config(text=f"Player: {self.player_score}")
        self.result_computer_score.config(text=f"Computer: {self.computer_score}")
        
        # Update choice images
        self.player_choice_image.config(image=self.images[player_choice])
        self.computer_choice_image.config(image=self.images[computer_choice])
        
        # Update result text
        if result == "win":
            self.result_text.config(text="You Win!", fg=self.win_color)
        elif result == "lose":
            self.result_text.config(text="Computer Wins!", fg=self.lose_color)
        else:
            self.result_text.config(text="It's a Tie!", fg=self.tie_color)
    
    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.show_result(player_choice, computer_choice, result)
    
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_score += 1
            return "win"
        else:
            self.computer_score += 1
            return "lose"
    
    def reset_and_show_menu(self):
        self.player_score = 0
        self.computer_score = 0
        self.show_menu()

if __name__ == "__main__":
    try:
        # Try to import PIL
        from PIL import Image, ImageTk, ImageDraw
    except ImportError:
        # If PIL is not installed, show an error message
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", "This game requires the Pillow library. Please install it using:\npip install pillow")
        root.destroy()
        import sys
        sys.exit(1)
    
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
