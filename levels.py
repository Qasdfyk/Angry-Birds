from object_classes import Level, Pig, ObstacleHorizonal, ObstacleVertical

# obstacles not used
ob_vert_not_used = ObstacleVertical(10000, 10000)
ob_hor_not_used = ObstacleVertical(20000, 10000)

# LEVEL 0
pig0_1 = Pig(1200, 670)
level_0 = Level([pig0_1], [ob_vert_not_used], [ob_hor_not_used], 0)

# LEVEL 1
pig1_1 = Pig(800, 420)
ob_hor1_1 = ObstacleHorizonal(700, 460)
level_1 = Level([pig1_1], [ob_vert_not_used], [ob_hor1_1], 1)

# LEVEL 2
pig2_1 = Pig(1000, 470)
pig2_2 = Pig(1100, 270)
ob_hor2_1 = ObstacleHorizonal(900, 510)
ob_hor2_2 = ObstacleHorizonal(1000, 310)
level_2 = Level([pig2_1, pig2_2], [ob_vert_not_used],
                [ob_hor2_1, ob_hor2_2], 2)

# LEVEL 3
pig3_1 = Pig(800, 340)
pig3_2 = Pig(1200, 670)
ob_vert3_1 = ObstacleVertical(800, 460)
ob_vert3_2 = ObstacleVertical(800, 0)
ob_vert3_3 = ObstacleVertical(920, 130)
ob_hor3_1 = ObstacleHorizonal(700, 380)
level_3 = Level([pig3_1, pig3_2], [ob_vert3_1, ob_vert3_2, ob_vert3_3],
                [ob_hor3_1], 3)


# LEVEL 4
pig4_1 = Pig(1100, 670)
pig4_2 = Pig(900, 500)
pig4_3 = Pig(450, 160)
ob_vert4_1 = ObstacleVertical(600, 460)
ob_vert4_2 = ObstacleVertical(600, 0)
ob_hor4_1 = ObstacleHorizonal(800, 540)
ob_hor4_2 = ObstacleHorizonal(350, 200)
level_4 = Level([pig4_1, pig4_2, pig4_3], [ob_vert4_1, ob_vert4_2],
                [ob_hor4_1, ob_hor4_2], 4)

levels = [level_0, level_1, level_2, level_3, level_4]
