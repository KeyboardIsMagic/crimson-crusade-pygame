import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))


'''All Enemy Assets'''

''' Basic Skeleton Assets'''
# Idle
basic_skell_idle_1 = pygame.image.load('imageAssets/BasicSkell/Idle/idle-1.png').convert_alpha()
basic_skell_idle_2 = pygame.image.load('imageAssets/BasicSkell/Idle/idle-2.png').convert_alpha()
basic_skell_idle_3 = pygame.image.load('imageAssets/BasicSkell/Idle/idle-3.png').convert_alpha()
basic_skell_idle_4 = pygame.image.load('imageAssets/BasicSkell/Idle/idle-4.png').convert_alpha()
basic_skell_idle = [basic_skell_idle_1, basic_skell_idle_2, basic_skell_idle_3, basic_skell_idle_4]
basic_skell_idle_index = 0

# Attack
basic_skell_attack_1 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A1.png').convert_alpha()
basic_skell_attack_2 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A2.png').convert_alpha()
basic_skell_attack_3 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A3.png').convert_alpha()
basic_skell_attack_4 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A4.png').convert_alpha()
basic_skell_attack_5 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A5.png').convert_alpha()
basic_skell_attack_6 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A6.png').convert_alpha()
basic_skell_attack_7 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A7.png').convert_alpha()
basic_skell_attack_8 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-A8.png').convert_alpha()
basic_skell_attack = [basic_skell_attack_1, basic_skell_attack_2, basic_skell_attack_3, basic_skell_attack_4, basic_skell_attack_5, basic_skell_attack_6, basic_skell_attack_7, basic_skell_attack_8]
basic_skell_attack_index = 0

basic_skell_attack_B1 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B1.png').convert_alpha()
basic_skell_attack_B2 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B2.png').convert_alpha()
basic_skell_attack_B3 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B3.png').convert_alpha()
basic_skell_attack_B4 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B4.png').convert_alpha()
basic_skell_attack_B5 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B5.png').convert_alpha()
basic_skell_attack_B6 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B6.png').convert_alpha()
basic_skell_attack_B7 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B7.png').convert_alpha()
basic_skell_attack_B8 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B8.png').convert_alpha()
basic_skell_attack_B9 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B9.png').convert_alpha()
basic_skell_attack_B10 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B10.png').convert_alpha()
basic_skell_attack_B11 = pygame.image.load('imageAssets/BasicSkell/Attack/attack-B11.png').convert_alpha()
basic_skell_attack_B = [basic_skell_attack_B1, basic_skell_attack_B2, basic_skell_attack_B3, basic_skell_attack_B4, basic_skell_attack_B5, basic_skell_attack_B6, basic_skell_attack_B7, basic_skell_attack_B8, basic_skell_attack_B9, basic_skell_attack_B10, basic_skell_attack_B11]
basic_skell_attack_B_index = 0

# Walk
basic_skell_walk_1 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-1.png').convert_alpha()
basic_skell_walk_2 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-2.png').convert_alpha()
basic_skell_walk_3 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-3.png').convert_alpha()
basic_skell_walk_4 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-4.png').convert_alpha()
basic_skell_walk_5 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-5.png').convert_alpha()
basic_skell_walk_6 = pygame.image.load('imageAssets/BasicSkell/Walk/walk-6.png').convert_alpha()
basic_skell_walk = [basic_skell_walk_1, basic_skell_walk_2, basic_skell_walk_3, basic_skell_walk_4, basic_skell_walk_5, basic_skell_walk_6]
basic_skell_walk_index = 0

# Hit Stun
basic_skell_hitstun_1 = pygame.image.load('imageAssets/BasicSkell/HitStun/hit-1.png').convert_alpha()
basic_skell_hitstun_2 = pygame.image.load('imageAssets/BasicSkell/HitStun/hit-2.png').convert_alpha()
basic_skell_hitstun_3 = pygame.image.load('imageAssets/BasicSkell/HitStun/hit-3.png').convert_alpha()
basic_skell_hitstun = [basic_skell_hitstun_1, basic_skell_hitstun_2, basic_skell_hitstun_3]
basic_skell_hitstun_index = 0

# Death
basic_skell_death_1 = pygame.image.load('imageAssets/BasicSkell/Dead/dead-1.png').convert_alpha()
basic_skell_death_2 = pygame.image.load('imageAssets/BasicSkell/Dead/dead-2.png').convert_alpha()
basic_skell_death_3 = pygame.image.load('imageAssets/BasicSkell/Dead/dead-3.png').convert_alpha()
basic_skell_death_4 = pygame.image.load('imageAssets/BasicSkell/Dead/dead-4.png').convert_alpha()
basic_skell_death = [basic_skell_death_1, basic_skell_death_2, basic_skell_death_3, basic_skell_death_4]
basic_skell_death_index = 0

###########################################################################################################

''' Armored Skeleton Assets'''

# Idle
armored_skell_idle_1 = pygame.image.load('imageAssets/SkellWarrior/idle/idle-1.png').convert_alpha()
armored_skell_idle_2 = pygame.image.load('imageAssets/SkellWarrior/idle/idle-2.png').convert_alpha()
armored_skell_idle_3 = pygame.image.load('imageAssets/SkellWarrior/idle/idle-3.png').convert_alpha()
armored_skell_idle_4 = pygame.image.load('imageAssets/SkellWarrior/idle/idle-4.png').convert_alpha()
armored_skell_idle = [armored_skell_idle_1, armored_skell_idle_2, armored_skell_idle_3, armored_skell_idle_4]
armored_skell_idle_index = 0

# Attack
armored_skell_attack_1 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A1.png').convert_alpha()
armored_skell_attack_2 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A2.png').convert_alpha()
armored_skell_attack_3 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A3.png').convert_alpha()
armored_skell_attack_4 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A4.png').convert_alpha()
armored_skell_attack_5 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A5.png').convert_alpha()
armored_skell_attack_6 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A6.png').convert_alpha()
armored_skell_attack_7 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A7.png').convert_alpha()
armored_skell_attack_8 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A8.png').convert_alpha()
armored_skell_attack_9 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A9.png').convert_alpha()
armored_skell_attack_10 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A10.png').convert_alpha()
armored_skell_attack_11 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A11.png').convert_alpha()
armored_skell_attack_12 = pygame.image.load('imageAssets/SkellWarrior/Attack1/attack-A12.png').convert_alpha()
armored_skell_attack = [armored_skell_attack_1, armored_skell_attack_2, armored_skell_attack_3, armored_skell_attack_4, armored_skell_attack_5, armored_skell_attack_6, armored_skell_attack_7, armored_skell_attack_8, armored_skell_attack_9, armored_skell_attack_10, armored_skell_attack_11, armored_skell_attack_12]
armored_skell_attack_index = 0

armored_skell_attack_B1 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B1.png').convert_alpha()
armored_skell_attack_B2 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B2.png').convert_alpha()
armored_skell_attack_B3 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B3.png').convert_alpha()
armored_skell_attack_B4 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B4.png').convert_alpha()
armored_skell_attack_B5 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B5.png').convert_alpha()
armored_skell_attack_B6 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B6.png').convert_alpha()
armored_skell_attack_B7 = pygame.image.load('imageAssets/SkellWarrior/Attack2/attack-B7.png').convert_alpha()
armored_skell_attack_B = [armored_skell_attack_B1, armored_skell_attack_B2, armored_skell_attack_B3, armored_skell_attack_B4, armored_skell_attack_B5, armored_skell_attack_B6, armored_skell_attack_B7]
armored_skell_attack_B_index = 0

# Walk
armored_skell_walk_1 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-1.png').convert_alpha()
armored_skell_walk_2 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-2.png').convert_alpha()
armored_skell_walk_3 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-3.png').convert_alpha()
armored_skell_walk_4 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-4.png').convert_alpha()
armored_skell_walk_5 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-5.png').convert_alpha()
armored_skell_walk_6 = pygame.image.load('imageAssets/SkellWarrior/walk/walk-6.png').convert_alpha()
armored_skell_walk = [armored_skell_walk_1, armored_skell_walk_2, armored_skell_walk_3, armored_skell_walk_4, armored_skell_walk_5, armored_skell_walk_6]
armored_skell_walk_index = 0

# Hit Stun
armored_skell_hitstun_1 = pygame.image.load('imageAssets/SkellWarrior/HitStun/hit-1.png').convert_alpha()
armored_skell_hitstun_2 = pygame.image.load('imageAssets/SkellWarrior/HitStun/hit-2.png').convert_alpha()
armored_skell_hitstun_3 = pygame.image.load('imageAssets/SkellWarrior/HitStun/hit-3.png').convert_alpha()
armored_skell_hitstun = [armored_skell_hitstun_1, armored_skell_hitstun_2, armored_skell_hitstun_3]
armored_skell_hitstun_index = 0

# Death
armored_skell_death_1 = pygame.image.load('imageAssets/SkellWarrior/dead/dead-1.png').convert_alpha()
armored_skell_death_2 = pygame.image.load('imageAssets/SkellWarrior/dead/dead-2.png').convert_alpha()
armored_skell_death_3 = pygame.image.load('imageAssets/SkellWarrior/dead/dead-3.png').convert_alpha()
armored_skell_death_4 = pygame.image.load('imageAssets/SkellWarrior/dead/dead-4.png').convert_alpha()
armored_skell_death = [armored_skell_death_1, armored_skell_death_2, armored_skell_death_3, armored_skell_death_4]
armored_skell_death_index = 0

###########################################################################################################