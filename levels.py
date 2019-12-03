#! /usr/bin/env python
#-*- coding: utf-8 -*-



testChunk = [
"                                                       W",
"                                                        ",
"                                                       W",
"                                                        ",
"                                                       W",
"                                                        ",
"                                                       W",
"W W W W W W W W W W W W W W W W W W W W W W W W W W W W ",
]


testChunk2 = [
"                                                        ",
"                                                        ",
"                                                        ",
"                                      W                 ",
"       W                              W                W",
"                    W                                  W",
"                                                       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


init_1 = [
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"   ",
"W  ",
]


chunk_0 = [
"                                                       ",
"                                                       ",
"                                                       ",
"                                                     WW",
"                                                     WW",
"                                                     WW",
"                                               WW    WW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


chunk_1 = [
"                                     W                                                                        W",
"",
"                                                                                                       WW              W",
"              W             W         W              WW                  W    W    W    W             W W",
"                                               WW    WW                                              W  W",
"                                         WW    WW    WW     W                                       W   W                W",
"                                         WW    WW    WW     W                                      W    W     W        W",
"WWWWWWWWWWWWWWWWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWW   WW                       WWWWWW      WWWWW WWWWWWWW ",
]


chunk_2 = [
"                        W                   W           ",
"                                                        ",
"             W                         W                ",
"   W                   W                                ",
"  W               WW       WWW              W          W",
"          W                       W                   WW",
"         WW                       W      W           WWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


mini_1 = [
"          ",
"          ",
"          ",
"          ",
"          ",
"          ",
"          ",
"WWW    WWW"
]


mini_2 = [
"          ",
"          ",
"          ",
"          ",
"WWW       ",
"      WWW ",
"       W  ",
"WWWWWW W W",
]


mini_3 = [
"          ",
"          ",
"          ",
"          ",
"          ",
"          ",
" WWWWWWWW ",
"WWWWWWWWWW",
]


mini_4 = [
"WW        ",
"          ",
"          ",
"          ",
"  W       ",
"          ",
"          ",
"W       WW",
]


mini_5 = [
"        ",
"        ",
"WWWWW   ",
"W W W   ",
"W W W   ",
"        ",
"        ",
"W W WW  ",
]


mid_1 = [
"                        ",
"                        ",
"                        ",
"                        ",
"                        ",
"WWW    WWW    WWW    WWW",
" W      W      W      W ",
" W  WW  W  WW  W  WW  W ",
]


mid_2 = [
"                             ",
"                             ",
"                         WWWW",
"                    WWWW     ",
"               WWWW          ",
"          WWWW               ",
"     WWWW                    ",
"WWWW                         ",
]

flat_1 = [
"                         ",
"                         ",
"                         ",
"                         ",
"                         ",
"                         ",
"                         ",
"WWWWWWWWWWWWWWWWWWWWWWWWW",
]

flat_2 = [
"                         ",
"          W              ",
"                         ",
"                         ",
"                W        ",
"                         ",
"      W                  ",
"WWWWWWWWWWWWWWWWWWWWWWWWW",
]

flat_3 = [
"                         ",
"        W                ",
"                     W   ",
"                         ",
"                         ",
"        W                ",
"        W                ",
"WWWWWWWWWWWWWWWWWWWWWWWWW",
]

spe_1 = [
"                        ",
"    WW                  ",
"  W W                   ",
"  W W                   ",
"W W WWWWWWWWWW WWWWWW   ",
"  W                     ",
"  W                     ",
"WWWWWWWWWWWWWW WWWWWWW  ",
]

spe_2 = [
"      W               W         ",
"      W          WWW  W         ",
"      W               W         ",
"      WW              W         ",
"      W               W         ",
"                      W         ",
"                      W         ",
"     WWWWWW           W      WW ",
]


spe_3 = [
"         W                      ",
"         W                      ",
"         W            WW        ",
"                                ",
"      W                         ",
"      WWWWW                     ",
" W                              ",
"WW                              ",
]


spe_4 = [
"                                       ",
"                                       ",
"                                       ",
"                                  WWW  ",
"               WW                      ",
"                                       ",
"WWW                                    ",
"W                                 WWW  ",
]


spe_5 = [
"  W              WWW                       ",
"  WW                                       ",
"                                           ",
"             W                             ",
"            WW                             ",
"                                           ",
"                                           ",
"WWW                                       W",
]


extra_1 = [
"  W     W                                          ",
"  WW   WW                                          ",
"  W W W W    WWW   W WWW   WW WW    WWW   WWWWW    ",
"  W  W  W   W   W  WW     W  W  W  W   W     W     ",
"  W     W   W   W  W      W     W  W   W    W      ",
"  W     W   WWWW   W      W     W  W   W   W       ",
"  W     W   W      W      W     W  W   W  W        ",
"  W     W    WWWW  W      W     W   WWW   WWWWW    ",
]


niveau = []

niveau.append(init_1)

#niveau.append(testChunk)
#niveau.append(testChunk2)

#niveau.append(chunk_0)
#niveau.append(chunk_1)
#niveau.append(chunk_2)

niveau.append(mini_1)
niveau.append(mini_2)
niveau.append(mini_3)
# niveau.append(mini_4)
niveau.append(mini_5)

# niveau.append(mid_1)
niveau.append(mid_2)

#niveau.append(flat_1)
#niveau.append(flat_2)
#niveau.append(flat_3)

niveau.append(spe_1)
# niveau.append(spe_2)
niveau.append(spe_3)
# niveau.append(spe_4)
# niveau.append(spe_5)

#niveau.append(extra_1)

HAUTEUR_CHUNK = 8 # En nombre de block
NBR_CHUNK = len(niveau)
