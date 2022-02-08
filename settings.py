#game settings

WIDTH = 1024 #of the window
HEIGTH = 768 #   //
FPS = 120
BLOCKSIZE = 96 #the floor

# user interface
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80

#color
UI_BG_COLOR = 100,100,100
UI_BORDER_COLOR = 0,0,0

#day n night
DAY_DURATION = 2
NIGHT_DURATION = 10

# number of tile 26 x 25
MAP_1 = [
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','w','w','w','w','w','w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','w','w','w','w','w','w','w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','w','w','w','w','w','w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','w','w','w','w','w','w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','w','w','w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o',' ',' ',' ','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','t',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ','o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o',' ','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o'],
]
