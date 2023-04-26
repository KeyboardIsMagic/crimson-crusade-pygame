import pygame
from sys import exit
from random import randint, choice
from heroAssets import *
from enemyAssets import *
from miscAssets import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        '''List of images for the player's animation'''
        self.player_idle = [player_idle_1, player_idle_2, player_idle_3, player_idle_4, player_idle_5, player_idle_6]
        self.player_idle_left = []
        for image in self.player_idle: self.player_idle_left.append(self.flip_image(image))
        self.player_idle_index = 0
        
        self.player_run_right = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8, player_run_9, player_run_10, player_run_11, player_run_12]
        self.player_run_left = []
        for image in self.player_run_right: self.player_run_left.append(self.flip_image(image))
        self.player_index = 0
        
        self.player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5, player_jump_6, player_jump_7, player_jump_8, player_jump_9, player_jump_10, player_jump_11, player_jump_12, player_jump_13, player_jump_14]
        self.player_jump_left = []
        for image in self.player_jump: self.player_jump_left.append(self.flip_image(image))
        self.player_jump_index = 0
        
        self.player_attack_1 = [player_a1_1, player_a1_2, player_a1_3, player_a1_4, player_a1_5, player_a1_6, player_a1_7]
        self.player_attack_1_left = []
        for image in self.player_attack_1: self.player_attack_1_left.append(self.flip_image(image))
        self.player_attack_1_index = 0
        
        
        '''Player's starting image, rect, gravity, hitbox, and facing direction'''
        self.image = self.player_idle[self.player_idle_index]
        self.rect = pygame.Rect(320, 16, 32, 64) # (x, y, width, height)
        self.gravity = 0
        self.player_health = 100
        
        self.facing_right = True
        
        
    def flip_image(self, image): # Flips the image to the opposite direction when needed
        return pygame.transform.flip(image, True, False)
    
    def adjust_sprite_position(self):
        if self.facing_right: self.rect.x += 32
        else: self.rect.x -= 32
    
    def player_movement(self): # Player's input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 350:
            self.gravity = -10
            
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.facing_right:
                self.facing_right = False
                self.adjust_sprite_position()
            
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if not self.facing_right:
                self.facing_right = True
                self.adjust_sprite_position()

        
    def apply_gravity(self): #Applies gravity to the player
        self.gravity += 0.7
        self.rect.y += self.gravity
        if self.rect.bottom > 352:
            self.rect.bottom = 352
            
    def animation_state(self): # Changes the player's animation state
        keys = pygame.key.get_pressed()
        moving = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]
        attacking = keys[pygame.K_c]
        
        if self.rect.bottom < 350:
            self.player_jump_index += 0.5
            if self.player_jump_index >= len(self.player_jump): self.player_jump_index = 0
            if self.facing_right:
                self.image = self.player_jump[int(self.player_jump_index)]
            else:
                self.image = self.player_jump_left[int(self.player_jump_index)]
        elif moving:
            if self.facing_right:
                self.player_index += 0.4
                if self.player_index >= len(self.player_run_right): self.player_index = 0
                self.image = self.player_run_right[int(self.player_index)]
            else:
                self.player_index += 0.4
                if self.player_index >= len(self.player_run_left): self.player_index = 0
                self.image = self.player_run_left[int(self.player_index)]
        elif attacking:
            self.player_attack_1_index += 0.3
            if self.player_attack_1_index >= len(self.player_attack_1): self.player_attack_1_index = 0
            if self.facing_right:
                self.image = self.player_attack_1[int(self.player_attack_1_index)]
            else:
                self.image = self.player_attack_1_left[int(self.player_attack_1_index)]
        else:
            if self.facing_right:
                self.player_idle_index += 0.1
                if self.player_idle_index >= len(self.player_idle): self.player_idle_index = 0
                self.image = self.player_idle[int(self.player_idle_index)]
            else:
                self.player_idle_index += 0.1
                if self.player_idle_index >= len(self.player_idle_left): self.player_idle_index = 0
                self.image = self.player_idle_left[int(self.player_idle_index)]

    def update(self, item_group): # Updates the player's position, hitbox, and animation each frame
        self.update_hitboxes()
        self.player_movement()
        self.apply_gravity()
        self.animation_state()
        self.player_position()
        self.item_collision(item_group)
        
    def player_position(self): # Keeps the player within the screen
        if self.rect.x + 80 < -5:
            self.rect.x = 790
        elif self.rect.x > 800:
            self.rect.x  = 0 - 80
        
    def update_hitboxes(self):
        keys = pygame.key.get_pressed()
        moving = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]
        attacking = keys[pygame.K_c]
        
        '''Player hitbox'''
        if self.facing_right:
            self.player_hitbox = (self.rect.x + 32, self.rect.y + 16, 32, 48)
        else:  # Player is facing left
            self.player_hitbox = (self.rect.x + 64, self.rect.y + 16, 32, 48)

        '''Attack hitbox'''
        if attacking and not moving and self.rect.bottom >= 350:
            if self.facing_right:
                self.attack_hitbox = (self.rect.x + 48, self.rect.y + 32, 48, 16)
            else:  # Player is facing left
                self.attack_hitbox = (self.rect.x + 32, self.rect.y + 32, 48, 16)
        else: # Remove attack hitbox
            self.attack_hitbox = (self.rect.x, self.rect.y, 0, 0)
            
        '''Display hitboxes visually for testing'''    
        # pygame.draw.rect(screen, 'red', self.attack_hitbox)
        # pygame.draw.rect(screen, 'pink', self.player_hitbox)
        
    def check_collision(self, enemy_group): 
        for enemy in enemy_group:
            if pygame.Rect(*self.attack_hitbox).colliderect(pygame.Rect(*enemy.enemy_hurtbox)):
                enemy.enemy_health -= 1
                enemy.hit_stun_animation()
                # print(enemy.enemy_health)
                
    def item_collision(self, item_group): # Argument is defined in the main loop within update()
        collection_hitbox = pygame.Rect(self.player_hitbox[0] + self.player_hitbox[2] //3,
                                        (self.player_hitbox[1] + 32) + self.player_hitbox[3] //3,
                                        self.player_hitbox[2] //3,
                                        self.player_hitbox[3] //3)  # Creating a smaller hitbox by reusing code from players hitbox for item collection
        
        for item in item_group:
            if pygame.Rect(collection_hitbox).colliderect(item.rect):
                if item.drop_type == 'health':
                    self.player_health += 15
                    if self.player_health > 100: self.player_health = 100 # Prevents health from going over 100
                    item.kill()
                elif item.drop_type == 'coin':
                    global coins
                    coins += randint(2, 7)
                    item.kill()
                    
        ''' Display hitbox visually for testing'''
        # pygame.draw.rect(screen, 'pink', collection_hitbox)
                
    def get_x_offset(self): # Values used to calculate the player's correct position on the screen for enemy AI
        if self.facing_right: return -10
        else: return 64




class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x = randint(0, 800)):
        super().__init__()

        '''List of images for the enemy's animation'''
        
        # Basic Skeleton
        self.basic_skell_idle = [basic_skell_idle_1, basic_skell_idle_2, basic_skell_idle_3, basic_skell_idle_4]
        self.basic_skell_idle_left = []
        for image in self.basic_skell_idle: self.basic_skell_idle_left.append(self.flip_image(image))
        self.basic_skell_idle_index = 0

        self.basic_skell_walk = [basic_skell_walk_1, basic_skell_walk_2, basic_skell_walk_3, basic_skell_walk_4]
        self.basic_skell_walk_left = []
        for image in self.basic_skell_walk: self.basic_skell_walk_left.append(self.flip_image(image))
        self.basic_skell_walk_index = 0
        
        self.basic_skell_attack = [basic_skell_attack_1, basic_skell_attack_2, basic_skell_attack_3, basic_skell_attack_4, basic_skell_attack_5, basic_skell_attack_6, basic_skell_attack_7, basic_skell_attack_8]
        self.basic_skell_attack_left = []
        for image in self.basic_skell_attack: self.basic_skell_attack_left.append(self.flip_image(image))
        self.basic_skell_attack_index = 0
        
        self.basic_skell_hitstun = [basic_skell_hitstun_1, basic_skell_hitstun_2, basic_skell_hitstun_3]
        self.basic_skell_hitstun_left = []
        for image in self.basic_skell_hitstun: self.basic_skell_hitstun_left.append(self.flip_image(image))
        self.basic_skell_hitstun_index = 0
        
        '''Enemy's starting image, rect, and facing direction'''
        self.image = self.basic_skell_idle[self.basic_skell_idle_index]
        self.rect = pygame.Rect(x, 16, 32, 64) # (x, y, width, height)
        
        self.facing_right = True
        self.player = player.sprites()[0]
        self.attack_radius = 75
        self.attack_timer = randint(180, 300)
        self.enemy_health = 60
        self.enemy_gravity = 0

    def flip_image(self, image): # Flips the image to the opposite direction when needed
        return pygame.transform.flip(image, True, False)

    def hit_stun_animation(self):
        if self.facing_right:
            self.basic_skell_hitstun_index += 0.1
            if self.basic_skell_hitstun_index >= len(self.basic_skell_hitstun): self.basic_skell_hitstun_index = 0
            self.image = self.basic_skell_hitstun[int(self.basic_skell_hitstun_index)]
            self.rect.x -= 0.5
        else:
            self.basic_skell_hitstun_index += 0.1
            if self.basic_skell_hitstun_index >= len(self.basic_skell_hitstun_left): self.basic_skell_hitstun_index = 0
            self.image = self.basic_skell_hitstun_left[int(self.basic_skell_hitstun_index)]
            self.rect.x += 0.5
            
    def update_hitboxes(self): # Updates the enemy's hurtbox and hitbox
        '''Enemy hurtbox'''
        if self.facing_right:
            self.enemy_hurtbox = (self.rect.x + 32, self.rect.y + 32, 32, 48)
        else:  # Facing left
            self.enemy_hurtbox = (self.rect.x + 64, self.rect.y + 32, 32, 48)

        '''Enemy hitbox'''
        if self.basic_skell_attack_index >= 4 and self.basic_skell_attack_index <= 5:
            if self.facing_right:
                self.enemy_hitbox = (self.rect.x + 48, self.rect.y + 48, 64, 16)
            else:  # Facing left
                self.enemy_hitbox = (self.rect.x + 32, self.rect.y + 48, 48, 16)
        else:
            self.enemy_hitbox = (0, 0, 0, 0)

        '''Display hitboxes visually for testing'''    
        #pygame.draw.rect(screen, 'pink', self.enemy_hitbox)

    def update(self): # Updates the enemy's position, hitbox, and animation each frame
        self.update_hitboxes()
        self.enemy_AI_logic()
        self.destroy()
        self.apply_gravity()

    def enemy_x_offset(self): # Value used to calculate correct attack distance
        if self.facing_right: return -32
        else: return 48

    def enemy_AI_logic(self):
        enemy_x_offset = self.enemy_x_offset() # Creates a variable for the enemy's x offset based on its facing direction
        player_x_offset = self.player.get_x_offset() # Same as above but for the player
        
        # Get the distance between the enemy and the player for attacking
        player_center_x = self.player.rect.x + player_x_offset
        enemy_center_x = self.rect.x + enemy_x_offset
        distance_to_player = player_center_x - enemy_center_x 
        
        # Move towards the player
        if abs(distance_to_player) > self.attack_radius:
            if distance_to_player > 0:
                self.rect.x += 1
                if not self.facing_right:
                    self.facing_right = True
            else:
                self.rect.x -= 1
                if self.facing_right:
                    self.facing_right = False
                    
            # Change animation state to 'Walking'
            if self.facing_right:
                self.basic_skell_walk_index += 0.1
                if self.basic_skell_walk_index >= len(self.basic_skell_walk): self.basic_skell_walk_index = 0
                self.image = self.basic_skell_walk[int(self.basic_skell_walk_index)]
            else:
                self.basic_skell_walk_index += 0.1
                if self.basic_skell_walk_index >= len(self.basic_skell_walk_left): self.basic_skell_walk_index = 0
                self.image = self.basic_skell_walk_left[int(self.basic_skell_walk_index)]

        # Attack the player if within range
        elif self.attack_timer > 0:
            if self.facing_right:
                self.basic_skell_attack_index += 0.1
                if self.basic_skell_attack_index >= len(self.basic_skell_attack): self.basic_skell_attack_index = 0
                self.image = self.basic_skell_attack[int(self.basic_skell_attack_index)]
            else:
                self.basic_skell_attack_index += 0.1
                if self.basic_skell_attack_index >= len(self.basic_skell_attack_left): self.basic_skell_attack_index = 0
                self.image = self.basic_skell_attack_left[int(self.basic_skell_attack_index)]
            
            self.attack_timer -= 1
        
        else: # Change animation state to 'Idle'
            if self.facing_right:
                self.basic_skell_idle_index += 0.1
                if self.basic_skell_idle_index >= len(self.basic_skell_idle): self.basic_skell_idle_index = 0
                self.image = self.basic_skell_idle[int(self.basic_skell_idle_index)]
            else:
                self.basic_skell_idle_index += 0.1
                if self.basic_skell_idle_index >= len(self.basic_skell_idle_left): self.basic_skell_idle_index = 0
                self.image = self.basic_skell_idle_left[int(self.basic_skell_idle_index)]   
            # Reset the attack timer       
            self.attack_timer = randint(180, 300) 
            
        
        
    def check_collision(self, player_sprite):
        player = player_sprite.sprite
        if pygame.Rect(*self.enemy_hitbox).colliderect(pygame.Rect(*player.player_hitbox)):
            player.player_health -= 0.6
            #print(f'Player health: {player.player_health:.2f}')
    
    def apply_gravity(self):
        self.enemy_gravity += 0.5
        self.rect.y += self.enemy_gravity
        if self.rect.y >= 272:
            self.rect.y = 272
            self.enemy_gravity = 0
        
    def destroy(self): # Destroys the enemy
        global enemies_killed
        if self.enemy_health <= 0:
            item_type = choice(['health', 'coin'])
            item_drop = ItemDrop(self.rect.x, item_type)
            item_group.add(item_drop)
            enemies_killed += 1
            self.kill()




class ItemDrop(pygame.sprite.Sprite):
    def __init__(self, x, item_type):
        super().__init__()
        self.drop_type = item_type
        if self.drop_type == 'health': self.image = food_drop
        if self.drop_type == 'coin': self.image = coin_drop
        self.rect = self.image.get_rect()
        self.rect.x = x + 50
        self.rect.y = 345




# Helpful Game Functions

def display_time(): #Displays the score
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surface = game_font.render(f'{current_time}', True, 'black')
    time_rect = time_surface.get_rect(center=(110, 30))
    screen.blit(time_surface, time_rect)
    return current_time
    
def display_coins(): # Displays the player's coins
    coin_surface = game_font.render(f'{coins}', True, 'black')
    coin_rect = coin_surface.get_rect(center=(110, 54))
    screen.blit(coin_surface, coin_rect)

def display_health(player_obj): # Displays the player's health
    player = player_obj.sprite
    health_surface = game_font.render(f'{player.player_health:.0f}', True, 'black')
    health_rect = health_surface.get_rect(center=(110, 76))
    screen.blit(health_surface, health_rect)

# Game
pygame.display.set_caption('Crimson Crusade')
clock = pygame.time.Clock()
main_menu = True
game_active = False
death_menu = False
setting_menu = False
credits_menu = False
start_time = 0
time = 0
temp_time = 0
coins = 0
enemies_killed = 0




# Music
background_music = pygame.mixer.Sound('musicAssets/Battle-Furious-edit.mp3')
background_music.play(loops=-1)
background_music.set_volume(0.1)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy(player))

item_group = pygame.sprite.Group()


# Timer
spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_timer, 1600)


while True:
    for event in pygame.event.get(): # Event listener 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
         
        elif main_menu:
            screen.blit(main_menu_background, (0, 0))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mm_hover_button_index -= 1
                    if mm_hover_button_index < 0: mm_hover_button_index = len(mm_hover_position) - 1
                    
                elif event.key == pygame.K_DOWN:
                    mm_hover_button_index += 1
                    if mm_hover_button_index >= len(mm_hover_position): mm_hover_button_index = 0
                    
                
                if event.type == pygame.KEYDOWN and mm_hover_button_index == 0 and event.key == pygame.K_SPACE: 
                    main_menu = False
                    game_active = True
                    mm_hover_button_index = 0
                    start_time = int(pygame.time.get_ticks() / 1000)
                    
                if event.type == pygame.KEYDOWN and mm_hover_button_index == 1 and event.key == pygame.K_SPACE: 
                    pass # Upgrades not available yet
                
                if event.type == pygame.KEYDOWN and mm_hover_button_index == 2 and event.key == pygame.K_SPACE:
                    main_menu = False
                    setting_menu = True
                    mm_hover_button_index = 0
                    
                if event.type == pygame.KEYDOWN and mm_hover_button_index == 3 and event.key == pygame.K_SPACE:
                    credits_menu = True
                    main_menu = False
                    mm_hover_button_index = 0
                
                if event.type == pygame.KEYDOWN and mm_hover_button_index == 4 and event.key == pygame.K_SPACE:
                    pygame.quit()
                    exit()
                    
            
            screen.blit(mm_hover_button, mm_hover_position[mm_hover_button_index])
            
        elif death_menu:
            screen.blit(game_over_background, (0, 0))
            
            # Drawing Scores on the death menu
            temp_time_surface = game_font.render(f'{temp_time}', True, ('black'))
            temp_time_rect = temp_time_surface.get_rect(center=(440, 162))
            screen.blit(temp_time_surface, temp_time_rect)
            
            enimies_killed_surface = game_font.render(f'{enemies_killed}', True, ('black'))
            enemies_killed_rect = enimies_killed_surface.get_rect(center=(440, 200))
            screen.blit(enimies_killed_surface, enemies_killed_rect)
            
            coins_surface = game_font.render(f'{coins}', True, ('black'))
            coins_rect = coins_surface.get_rect(center=(440, 235))
            screen.blit(coins_surface, coins_rect)
            
            # Death menu navigation
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dm_hover_button_index -= 1
                    if dm_hover_button_index < 0: dm_hover_button_index = len(dm_hover_position) - 1
                    
                elif event.key == pygame.K_RIGHT:
                    dm_hover_button_index += 1
                    if dm_hover_button_index >= len(dm_hover_position): dm_hover_button_index = 0
                    
                
                if event.type == pygame.KEYDOWN and dm_hover_button_index == 0 and event.key == pygame.K_SPACE: 
                    pass # Upgrades not developed yet
                    
                if event.type == pygame.KEYDOWN and dm_hover_button_index == 1 and event.key == pygame.K_SPACE: 
                    death_menu = False
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                    enemies_killed = 0
                    dm_hover_button_index = 0
                    
                if event.type == pygame.KEYDOWN and dm_hover_button_index == 2 and event.key == pygame.K_SPACE: 
                    death_menu = False
                    main_menu = True
                    enemies_killed = 0
                    dm_hover_button_index = 0
                    
            
            screen.blit(rest_hover_button, dm_hover_position[dm_hover_button_index])
        
        elif setting_menu:
            screen.blit(settings_background, (0, 0))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sm_hover_button_index -= 1
                    if sm_hover_button_index < 0: sm_hover_button_index = len(sm_hover_position) - 1
                    
                
                elif event.key == pygame.K_RIGHT:
                    sm_hover_button_index += 1
                    if sm_hover_button_index >= len(sm_hover_position): sm_hover_button_index = 0

                if event.type == pygame.KEYDOWN and sm_hover_button_index == 0 and event.key == pygame.K_SPACE:
                    pass #FIXME: Apply settings changes later
                
                if event.type == pygame.KEYDOWN and sm_hover_button_index == 1 and event.key == pygame.K_SPACE:
                    setting_menu = False
                    main_menu = True
                    sm_hover_button_index = 0
            
            screen.blit(rest_hover_button, sm_hover_position[sm_hover_button_index])
            
        elif credits_menu:
            screen.blit(credits_background, (0, 0))
            screen.blit(rest_hover_button, (42, 341))
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                credits_menu = False
                main_menu = True
            
            
                              
        if game_active:        
            if event.type == spawn_timer:
                enemy_group.add(Enemy(player, randint(0, 800)))
                

    ''' Game Logic'''
    if game_active:
        screen.blit(backGround_main, (0, 0))
        screen.blit(in_game_HUD, (7, 13))
        
        # Player
        player.draw(screen)
        player.update(item_group)
        

        enemy_group.draw(screen)
        enemy_group.update()
        
        item_group.draw(screen)
        
        
        # Collision
        player.sprite.check_collision(enemy_group)
        for enemy_instance in enemy_group:
            enemy_instance.check_collision(player)
            
        # In Game UI
        display_health(player)
        time = display_time()
        display_coins()
        
        
        # Game Over
        if player.sprite.player_health <= 0:
            game_active = False
            death_menu = True
            enemy_group.empty()
            player.sprite.player_health = 100
            player.sprite.rect.x = 400
            player.sprite.rect.y = 272
            start_time = 0
            temp_time = time
            item_group.empty()


    else:
        pass

    
    pygame.display.update()
    clock.tick(60)