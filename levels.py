#! /usr/bin/env python
#-*- coding: utf-8 -*-


# #################################
# SET OF LEVELS MADE FOR SPEEDRUNS
# #################################

# ##################
# Name : First Land
# ##################

init_1 = [
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"W  ",
]


chunk_1 = [
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"            ",
"WWWWWWWWWWWE"
]

chunk_2 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"          W    W     ",
"WWWWWWWWWWWWWWWWWWWWE"
]


chunk_3 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"          W          ",
"          W          ",
"          W          ",
"          W          ",
"WWWWWWWWWWWWWWWWWWWWE"
]

chunk_4 = [
"                      ",
"                      ",
"                      ",
"                      ",
"        WWWWWWWWWWWWW ",
"        W           WW",
"        W             ",
"        W             ",
"        W    WWWWWWWW ",
"        W           W ",
"        W           W ",
"        W           W ",
"        WWWWWWWWW   W ",
"                    W ",
"                    W ",
"WWWWWWWWWWWWWWWWWWWWWE"
]

chunk_5 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"        WWWWWWWWWWWWW",
"                     ",
"                     ",
"         WWWWWWWWWWWW",
"                    W",
"                    W",
"WWWWWWWWWWWWWWWWWWWWE"
]

chunk_6 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"    W        WWWWWWWW",
"    W    WWWWW      W",
"    W               W",
"    W               W",
"    WWWWWWWWWWWWW   W",
"                    W",
"                    W",
"WWWWWWWWWWWWWWWWWWWWE"
]

chunk_7 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"WWWWWWWWWW      WWWWE"
]

chunk_8 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"WWWW    WWWW     WWWE"
]

chunk_9 = [
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"        WWWW         ",
"                     ",
"                     ",
"WWWW             WWWE"
]

chunk_10 = [
"                WWWWWW",
"                      ",
"                      ",
"       W              ",
"       W            W ",
"       W            W ",
"       WW           W ",
"       W          WWW ",
"       W            W ",
"       W            W ",
"       WWW          W ",
"       W          WWW ",
"       W            W ",
"                    W ",
"                    W ",
"WWWWWWWWWWWW    WWWWWE"
]


chunk_11 = [
"                       ",
"                       ",
"                       ",
"               W       ",
"               W       ",
"               W       ",
"               W       ",
"        WW     W     WW",
"         W     W      W",
"         W     WW     W",
"         W     W      W",
"    WWW  W     W      W",
"         W     W     WW",
"         W            W",
"         W            W",
"  WWWWW  WW   WWWWWWWWE"
]


chunk_12 = [
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"       WWW    WWW    WWE",
"        W      W      W ",
"   WWW  W  WW  W  WW  W ",
]

chunk_13 = [
"              ",
"              ",
"              ",
"              ",
"              ",
"              ",
"              ",
"              ",
"    WW        ",
"              ",
"              ",
"              ",
"      W       ",
"              ",
"              ",
"WWWWW       WE",
]



chunk_14 = [
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                             ",
"                         WWWE",
"                    WWWW     ",
"               WWWW          ",
"          WWWW               ",
"     WWWW                    ",
"WWWW                         ",
]




level = []

# level.append(init_1)


level.append(chunk_1)
level.append(chunk_2)
level.append(chunk_3)
level.append(chunk_4)
level.append(chunk_5)
level.append(chunk_6)
level.append(chunk_7)
level.append(chunk_8)
level.append(chunk_9)
level.append(chunk_10) 
level.append(chunk_11)
level.append(chunk_12)
level.append(chunk_13)
level.append(chunk_14) # 24.406, 24.184, 23.253



CHUNK_HEIGHT = 16 # in amount of blocks
NB_CHUNK = len(level)
