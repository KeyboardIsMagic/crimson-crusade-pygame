import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))


'''Hero animations'''

# Idle
player_idle_1 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-1.png').convert_alpha()
player_idle_2 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-2.png').convert_alpha()
player_idle_3 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-3.png').convert_alpha()
player_idle_4 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-4.png').convert_alpha()
player_idle_5 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-5.png').convert_alpha()
player_idle_6 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-6.png').convert_alpha()
player_idle = [player_idle_1, player_idle_2, player_idle_3, player_idle_4, player_idle_5, player_idle_6]
player_idle_index = 0

player_wep_idle_1 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-1.png').convert_alpha()
player_wep_idle_2 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-2.png').convert_alpha()
player_wep_idle_3 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-3.png').convert_alpha()
player_wep_idle_4 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-4.png').convert_alpha()
player_wep_idle_5 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-5.png').convert_alpha()
player_wep_idle_6 = pygame.image.load('imageAssets/Hero/HeroIdle/idle-with-weapon-6.png').convert_alpha()
player_wep_idle = [player_wep_idle_1, player_wep_idle_2, player_wep_idle_3, player_wep_idle_4, player_wep_idle_5, player_wep_idle_6]
player_wep_idle_index = 0

# Walking with weapon
player_walk_1 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-1.png').convert_alpha()
player_walk_2 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-2.png').convert_alpha()
player_walk_3 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-3.png').convert_alpha()
player_walk_4 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-4.png').convert_alpha()
player_walk_5 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-5.png').convert_alpha()
player_walk_6 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-6.png').convert_alpha()
player_walk_7 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-7.png').convert_alpha()
player_walk_8 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-8.png').convert_alpha()
player_walk_9 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-9.png').convert_alpha()
player_walk_10 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-10.png').convert_alpha()
player_walk_11 = pygame.image.load('imageAssets/Hero/HeroWalking/walk-with-weapon-11.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7, player_walk_8, player_walk_9, player_walk_10, player_walk_11]
player_walk_index = 0

# Running
player_run_1 = pygame.image.load('imageAssets/Hero/HeroRun/run-1.png').convert_alpha()
player_run_2 = pygame.image.load('imageAssets/Hero/HeroRun/run-2.png').convert_alpha()
player_run_3 = pygame.image.load('imageAssets/Hero/HeroRun/run-3.png').convert_alpha()
player_run_4 = pygame.image.load('imageAssets/Hero/HeroRun/run-4.png').convert_alpha()
player_run_5 = pygame.image.load('imageAssets/Hero/HeroRun/run-5.png').convert_alpha()
player_run_6 = pygame.image.load('imageAssets/Hero/HeroRun/run-6.png').convert_alpha()
player_run_7 = pygame.image.load('imageAssets/Hero/HeroRun/run-7.png').convert_alpha()
player_run_8 = pygame.image.load('imageAssets/Hero/HeroRun/run-8.png').convert_alpha()
player_run_9 = pygame.image.load('imageAssets/Hero/HeroRun/run-9.png').convert_alpha()
player_run_10 = pygame.image.load('imageAssets/Hero/HeroRun/run-10.png').convert_alpha()
player_run_11 = pygame.image.load('imageAssets/Hero/HeroRun/run-11.png').convert_alpha()
player_run_12 = pygame.image.load('imageAssets/Hero/HeroRun/run-12.png').convert_alpha()
player_run = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6, player_run_7, player_run_8, player_run_9, player_run_10, player_run_11, player_run_12]
player_index = 0

# Jumping
player_jump_1 = pygame.image.load('imageAssets/Hero/HeroJump/jump-1.png').convert_alpha()
player_jump_2 = pygame.image.load('imageAssets/Hero/HeroJump/jump-2.png').convert_alpha()
player_jump_3 = pygame.image.load('imageAssets/Hero/HeroJump/jump-3.png').convert_alpha()
player_jump_4 = pygame.image.load('imageAssets/Hero/HeroJump/jump-4.png').convert_alpha()
player_jump_5 = pygame.image.load('imageAssets/Hero/HeroJump/jump-5.png').convert_alpha()
player_jump_6 = pygame.image.load('imageAssets/Hero/HeroJump/jump-6.png').convert_alpha()
player_jump_7 = pygame.image.load('imageAssets/Hero/HeroJump/jump-7.png').convert_alpha()
player_jump_8 = pygame.image.load('imageAssets/Hero/HeroJump/jump-8.png').convert_alpha()
player_jump_9 = pygame.image.load('imageAssets/Hero/HeroJump/jump-9.png').convert_alpha()
player_jump_10 = pygame.image.load('imageAssets/Hero/HeroJump/jump-10.png').convert_alpha()
player_jump_11 = pygame.image.load('imageAssets/Hero/HeroJump/jump-11.png').convert_alpha()
player_jump_12 = pygame.image.load('imageAssets/Hero/HeroJump/jump-12.png').convert_alpha()
player_jump_13 = pygame.image.load('imageAssets/Hero/HeroJump/jump-13.png').convert_alpha()
player_jump_14 = pygame.image.load('imageAssets/Hero/HeroJump/jump-14.png').convert_alpha()
player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4, player_jump_5, player_jump_6, player_jump_7, player_jump_8, player_jump_9, player_jump_10, player_jump_11, player_jump_12, player_jump_13, player_jump_14]
player_jump_index = 0

# Attacking
player_a1_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A1.png').convert_alpha()
player_a1_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A2.png').convert_alpha()
player_a1_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A3.png').convert_alpha()
player_a1_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A4.png').convert_alpha()
player_a1_5 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A5.png').convert_alpha()
player_a1_6 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A6.png').convert_alpha()
player_a1_7 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-A7.png').convert_alpha()
player_attack_1 = [player_a1_1, player_a1_2, player_a1_3, player_a1_4, player_a1_5, player_a1_6, player_a1_7]
player_attack_index = 0

player_b1_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B1.png').convert_alpha()
player_b1_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B2.png').convert_alpha()
player_b1_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B3.png').convert_alpha()
player_b1_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B4.png').convert_alpha()
player_b1_5 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B5.png').convert_alpha()
player_b1_6 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-B6.png').convert_alpha()
player_attack_2 = [player_b1_1, player_b1_2, player_b1_3, player_b1_4, player_b1_5, player_b1_6]
player_attack_2_index = 0

player_c1_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C1.png').convert_alpha()
player_c1_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C2.png').convert_alpha()
player_c1_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C3.png').convert_alpha()
player_c1_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C4.png').convert_alpha()
player_c1_5 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C5.png').convert_alpha()
player_c1_6 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C6.png').convert_alpha()
player_c1_7 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-C7.png').convert_alpha()
player_attack_3 = [player_c1_1, player_c1_2, player_c1_3, player_c1_4, player_c1_5, player_c1_6, player_c1_7]
player_attack_3_index = 0

player_d1_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D1.png').convert_alpha()
player_d1_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D2.png').convert_alpha()
player_d1_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D3.png').convert_alpha()
player_d1_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D4.png').convert_alpha()
player_d1_5 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D5.png').convert_alpha()
player_d1_6 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D6.png').convert_alpha()
player_d1_7 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D7.png').convert_alpha()
player_d1_8 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D8.png').convert_alpha()
player_d1_9 = pygame.image.load('imageAssets/Hero/HeroAttacks/attack-D9.png').convert_alpha()
player_attack_4 = [player_d1_1, player_d1_2, player_d1_3, player_d1_4, player_d1_5, player_d1_6, player_d1_7, player_d1_8, player_d1_9]
player_attack_4_index = 0

player_jump_attack_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/jump-attack-1.png').convert_alpha()
player_jump_attack_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/jump-attack-2.png').convert_alpha()
player_jump_attack_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/jump-attack-3.png').convert_alpha()
player_jump_attack_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/jump-attack-4.png').convert_alpha()
player_jump_attack_5 = pygame.image.load('imageAssets/Hero/HeroAttacks/jump-attack-5.png').convert_alpha()
player_jump_attack = [player_jump_attack_1, player_jump_attack_2, player_jump_attack_3, player_jump_attack_4, player_jump_attack_5]
player_jump_attack_index = 0

player_kick_attack_1 = pygame.image.load('imageAssets/Hero/HeroAttacks/kick-1.png').convert_alpha()
player_kick_attack_2 = pygame.image.load('imageAssets/Hero/HeroAttacks/kick-2.png').convert_alpha()
player_kick_attack_3 = pygame.image.load('imageAssets/Hero/HeroAttacks/kick-3.png').convert_alpha()
player_kick_attack_4 = pygame.image.load('imageAssets/Hero/HeroAttacks/kick-4.png').convert_alpha()
player_kick_attack = [player_kick_attack_1, player_kick_attack_2, player_kick_attack_3, player_kick_attack_4]
player_kick_attack_index = 0

# Blocking
player_block_pull_1 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-activ-1.png').convert_alpha()
player_block_pull_2 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-activ-2.png').convert_alpha()

player_block_center_1 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-center-1.png').convert_alpha()
player_block_center_2 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-center-2.png').convert_alpha()

player_block_up_1 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-up-1.png').convert_alpha()
player_block_up_2 = pygame.image.load('imageAssets/Hero/HeroBlock/shield-block-up-2.png').convert_alpha()

# Rolling
player_roll_1 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-1.png').convert_alpha()
player_roll_2 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-2.png').convert_alpha()
player_roll_3 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-3.png').convert_alpha()
player_roll_4 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-4.png').convert_alpha()
player_roll_5 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-5.png').convert_alpha()
player_roll_6 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-6.png').convert_alpha()
player_roll_7 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-7.png').convert_alpha()
player_roll_8 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-8.png').convert_alpha()
player_roll_9 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-9.png').convert_alpha()
player_roll_10 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-10.png').convert_alpha()
player_roll_11 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-11.png').convert_alpha()
player_roll_12 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-12.png').convert_alpha()
player_roll_13 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-13.png').convert_alpha()
player_roll_14 = pygame.image.load('imageAssets/Hero/HeroRoll/roll-14.png').convert_alpha()
player_roll = [player_roll_1, player_roll_2, player_roll_3, player_roll_4, player_roll_5, player_roll_6, player_roll_7, player_roll_8, player_roll_9, player_roll_10, player_roll_11, player_roll_12, player_roll_13, player_roll_14]
player_roll_index = 0

# Hit Stun
player_idle_hit_stun_1 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-A1.png').convert_alpha()
player_idle_hit_stun_2 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-A2.png').convert_alpha()
player_idle_hit_stun_3 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-A3.png').convert_alpha()
player_idle_hit_stun_4 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-A4.png').convert_alpha()

player_idle_hit_stun_B1 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-B1.png').convert_alpha()
player_idle_hit_stun_B2 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-B2.png').convert_alpha()
player_idle_hit_stun_B3 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-B3.png').convert_alpha()
player_idle_hit_stun_B4 = pygame.image.load('imageAssets/Hero/HeroHit/hit-idle-B4.png').convert_alpha()

player_wep_hit_stun_1 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-A1.png').convert_alpha()
player_wep_hit_stun_2 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-A2.png').convert_alpha()
player_wep_hit_stun_3 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-A3.png').convert_alpha()
player_wep_hit_stun_1 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-A4.png').convert_alpha()

player_wep_hit_stun_B1 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-B1.png').convert_alpha()
player_wep_hit_stun_B2 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-B2.png').convert_alpha()
player_wep_hit_stun_B3 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-B3.png').convert_alpha()
player_wep_hit_stun_B4 = pygame.image.load('imageAssets/Hero/HeroHit/hit-with-weapon-B4.png').convert_alpha()

# Dead
player_dead_1 = pygame.image.load('imageAssets/Hero/HeroDead/dead-1.png').convert_alpha()
player_dead_2 = pygame.image.load('imageAssets/Hero/HeroDead/dead-2.png').convert_alpha()
player_dead_3 = pygame.image.load('imageAssets/Hero/HeroDead/dead-3.png').convert_alpha()
player_dead_4 = pygame.image.load('imageAssets/Hero/HeroDead/dead-4.png').convert_alpha()
player_dead_5 = pygame.image.load('imageAssets/Hero/HeroDead/dead-5.png').convert_alpha()
player_dead_6 = pygame.image.load('imageAssets/Hero/HeroDead/dead-6.png').convert_alpha()
player_dead = [player_dead_1, player_dead_2, player_dead_3, player_dead_4, player_dead_5, player_dead_6]
player_dead_index = 0