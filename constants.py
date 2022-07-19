# Main constants
TITLE = "My Snake Game"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_SPEED_DELAY = 0.15
SNAKE_FOOD_COLLISION_DISTANCE = 15

# Snake constants
SEGMENT_START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# SEGMENT_START_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0), (-180, 0), (-200, 0), (-220, 0)]
MOVE_STEPS = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Food constants
POSITION_LOWER_BOUNDARY = -(SCREEN_WIDTH / 2 - 20)
POSITION_UPPER_BOUNDARY = SCREEN_WIDTH / 2 - 20

# ScoreBoard constants
SCORE_BOARD_POS_X = 0
SCORE_BOARD_POS_Y = SCREEN_WIDTH / 2 - 20
ALIGNMENT = "center"
SCORE_FONT = ("courier", 16, "bold")
GAME_OVER_FONT = ("courier", 30, "bold")
