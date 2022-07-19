from turtle import Screen
import time

from constants import TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SPEED_DELAY, SNAKE_FOOD_COLLISION_DISTANCE, POSITION_UPPER_BOUNDARY, POSITION_LOWER_BOUNDARY
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title(TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SNAKE_SPEED_DELAY)
    snake.move()

    # Detect collision with food
    if snake.get_head().distance(food) < SNAKE_FOOD_COLLISION_DISTANCE:
        food.set_random_position()
        scoreboard.increment_score()
        snake.increment_length()

    # Detect Collision with wall
    if snake.get_head().xcor() > POSITION_UPPER_BOUNDARY or snake.get_head().xcor() < POSITION_LOWER_BOUNDARY or snake.get_head().ycor() > POSITION_UPPER_BOUNDARY or snake.get_head().ycor() < POSITION_LOWER_BOUNDARY:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail - if head collides with any other segment in the snake
    if snake.has_collided_with_itself():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
