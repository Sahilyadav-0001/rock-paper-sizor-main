import pygame
import sys
import random
from pygame import mixer

# Initialize pygame
pygame.init()
mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Fonts
title_font = pygame.font.SysFont("Arial", 60, bold=True)
button_font = pygame.font.SysFont("Arial", 30)
score_font = pygame.font.SysFont("Arial", 36)
result_font = pygame.font.SysFont("Arial", 48, bold=True)

# Game variables
player_score = 0
computer_score = 0
result_text = ""
result_color = BLACK
game_state = "menu"  # menu, game, result

# Button class for interactive elements
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surface = button_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click

# Create buttons
rock_btn = Button(150, 350, 120, 60, "Rock", LIGHT_BLUE, DARK_BLUE)
paper_btn = Button(340, 350, 120, 60, "Paper", LIGHT_BLUE, DARK_BLUE)
scissors_btn = Button(530, 350, 120, 60, "Scissors", LIGHT_BLUE, DARK_BLUE)
play_again_btn = Button(300, 450, 200, 60, "Play Again", GREEN, (0, 200, 0))
menu_btn = Button(300, 520, 200, 60, "Main Menu", PURPLE, (100, 0, 100))
start_btn = Button(300, 350, 200, 60, "Start Game", GREEN, (0, 200, 0))
quit_btn = Button(300, 450, 200, 60, "Quit", RED, (200, 0, 0))

# Load images
def load_images():
    rock_img = pygame.image.load("rock.png") if pygame.image.get_extended() else None
    paper_img = pygame.image.load("paper.png") if pygame.image.get_extended() else None
    scissors_img = pygame.image.load("scissors.png") if pygame.image.get_extended() else None
    
    # If images couldn't be loaded, create placeholder images
    if not rock_img or not paper_img or not scissors_img:
        # Create placeholder images
        rock_img = create_placeholder_image("Rock")
        paper_img = create_placeholder_image("Paper")
        scissors_img = create_placeholder_image("Scissors")
    
    return rock_img, paper_img, scissors_img

def create_placeholder_image(text):
    # Create a surface with text as placeholder
    surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.rect(surface, LIGHT_BLUE, (0, 0, 100, 100), border_radius=10)
    pygame.draw.rect(surface, BLACK, (0, 0, 100, 100), 2, border_radius=10)
    
    text_surface = button_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(50, 50))
    surface.blit(text_surface, text_rect)
    
    return surface

# Try to load images, or create placeholders
try:
    rock_img, paper_img, scissors_img = load_images()
except:
    rock_img = create_placeholder_image("Rock")
    paper_img = create_placeholder_image("Paper")
    scissors_img = create_placeholder_image("Scissors")

# Scale images
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

# Game functions
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score, result_text, result_color
    
    if player_choice == computer_choice:
        result_text = "It's a tie!"
        result_color = PURPLE
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_text = "You win!"
        result_color = GREEN
        player_score += 1
    else:
        result_text = "Computer wins!"
        result_color = RED
        computer_score += 1

def draw_menu():
    screen.fill(WHITE)
    
    # Title
    title = title_font.render("ROCK PAPER SCISSORS", True, DARK_BLUE)
    title_rect = title.get_rect(center=(WIDTH // 2, 150))
    screen.blit(title, title_rect)
    
    # Draw buttons
    start_btn.draw(screen)
    quit_btn.draw(screen)

def draw_game():
    screen.fill(WHITE)
    
    # Title
    title = title_font.render("MAKE YOUR CHOICE", True, DARK_BLUE)
    title_rect = title.get_rect(center=(WIDTH // 2, 100))
    screen.blit(title, title_rect)
    
    # Score
    score_text = score_font.render(f"Player: {player_score}   Computer: {computer_score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 200))
    screen.blit(score_text, score_rect)
    
    # Draw buttons
    rock_btn.draw(screen)
    paper_btn.draw(screen)
    scissors_btn.draw(screen)
    
    # Draw button images
    screen.blit(rock_img, (rock_btn.rect.centerx - 50, rock_btn.rect.y - 120))
    screen.blit(paper_img, (paper_btn.rect.centerx - 50, paper_btn.rect.y - 120))
    screen.blit(scissors_img, (scissors_btn.rect.centerx - 50, scissors_btn.rect.y - 120))

def draw_result(player_choice, computer_choice):
    screen.fill(WHITE)
    
    # Title
    title = title_font.render("RESULT", True, DARK_BLUE)
    title_rect = title.get_rect(center=(WIDTH // 2, 80))
    screen.blit(title, title_rect)
    
    # Score
    score_text = score_font.render(f"Player: {player_score}   Computer: {computer_score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 150))
    screen.blit(score_text, score_rect)
    
    # Choices
    player_choice_text = score_font.render(f"You chose: {player_choice.capitalize()}", True, BLACK)
    player_rect = player_choice_text.get_rect(center=(WIDTH // 2, 220))
    screen.blit(player_choice_text, player_rect)
    
    computer_choice_text = score_font.render(f"Computer chose: {computer_choice.capitalize()}", True, BLACK)
    computer_rect = computer_choice_text.get_rect(center=(WIDTH // 2, 270))
    screen.blit(computer_choice_text, computer_rect)
    
    # Result
    result = result_font.render(result_text, True, result_color)
    result_rect = result.get_rect(center=(WIDTH // 2, 350))
    screen.blit(result, result_rect)
    
    # Draw buttons
    play_again_btn.draw(screen)
    menu_btn.draw(screen)
    
    # Draw choice images
    player_img = None
    computer_img = None
    
    if player_choice == "rock":
        player_img = rock_img
    elif player_choice == "paper":
        player_img = paper_img
    else:
        player_img = scissors_img
        
    if computer_choice == "rock":
        computer_img = rock_img
    elif computer_choice == "paper":
        computer_img = paper_img
    else:
        computer_img = scissors_img
    
    screen.blit(player_img, (150, 220))
    screen.blit(computer_img, (550, 220))

# Main game loop
def main():
    global game_state, player_score, computer_score
    
    player_choice = ""
    computer_choice = ""
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True
        
        if game_state == "menu":
            # Check button hover
            start_btn.check_hover(mouse_pos)
            quit_btn.check_hover(mouse_pos)
            
            # Check button clicks
            if start_btn.is_clicked(mouse_pos, mouse_clicked):
                game_state = "game"
            if quit_btn.is_clicked(mouse_pos, mouse_clicked):
                running = False
            
            # Draw menu
            draw_menu()
            
        elif game_state == "game":
            # Check button hover
            rock_btn.check_hover(mouse_pos)
            paper_btn.check_hover(mouse_pos)
            scissors_btn.check_hover(mouse_pos)
            
            # Check button clicks
            if rock_btn.is_clicked(mouse_pos, mouse_clicked):
                player_choice = "rock"
                computer_choice = get_computer_choice()
                determine_winner(player_choice, computer_choice)
                game_state = "result"
            if paper_btn.is_clicked(mouse_pos, mouse_clicked):
                player_choice = "paper"
                computer_choice = get_computer_choice()
                determine_winner(player_choice, computer_choice)
                game_state = "result"
            if scissors_btn.is_clicked(mouse_pos, mouse_clicked):
                player_choice = "scissors"
                computer_choice = get_computer_choice()
                determine_winner(player_choice, computer_choice)
                game_state = "result"
            
            # Draw game
            draw_game()
            
        elif game_state == "result":
            # Check button hover
            play_again_btn.check_hover(mouse_pos)
            menu_btn.check_hover(mouse_pos)
            
            # Check button clicks
            if play_again_btn.is_clicked(mouse_pos, mouse_clicked):
                game_state = "game"
            if menu_btn.is_clicked(mouse_pos, mouse_clicked):
                game_state = "menu"
                player_score = 0
                computer_score = 0
            
            # Draw result
            draw_result(player_choice, computer_choice)
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
