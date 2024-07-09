import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Making Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        scoreboard.give_point()
        snake.extend()
        food.refresh()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect Collision with tail
    for snake_part in snake.segments[1:]:
        if snake.head.distance(snake_part) < 15:
            # game_is_on = False
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
