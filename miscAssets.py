import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))

'''Misc Game Items and Assets'''
# Game Items
coin_drop = pygame.image.load('imageAssets/MiscAssets/drop_coin.png').convert_alpha() # Single Coin
food_drop = pygame.image.load('imageAssets/MiscAssets/food_1.png').convert_alpha() # Ham Joint


'''Menu and UI Assets'''
# Font
game_font = pygame.font.Font('imageAssets/Richsten.otf', 17)

# Backgrounds and UI
backGround_main = pygame.image.load('imageAssets/Background.png').convert_alpha()
main_menu_background = pygame.image.load('imageAssets/MiscAssets/Main_Menu.png').convert_alpha()
credits_background = pygame.image.load('imageAssets/MiscAssets/Credits.png').convert_alpha()
game_over_background = pygame.image.load('imageAssets/MiscAssets/Game_Over.png').convert_alpha()
settings_background = pygame.image.load('imageAssets/MiscAssets/Settings.png').convert_alpha()
in_game_HUD = pygame.image.load('imageAssets/MiscAssets/HUD.png').convert_alpha()

mm_hover_button = pygame.image.load('imageAssets/MiscAssets/Button_hover.png').convert_alpha()
rest_hover_button = pygame.image.load('imageAssets/MiscAssets/Button_hover_credits.png').convert_alpha()

# Index and position values for menus
# Main Menu
mm_hover_position = [(352, 172), (352, 204), (352, 236), (352, 268), (352, 301)]
mm_hover_button_index = 0
# Death Menu
dm_hover_position = [(262, 276), (363, 276), (464, 276)]
dm_hover_button_index = 0
# Settings Menu
sm_hover_position = [(311, 318), (412, 318)]
sm_hover_button_index = 0