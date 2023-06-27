import time
import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake game")
screen.tracer(0)

game_is_on = True
snake = Snake.Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect food collision
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.write_score()

#   detect wall collision
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # scoreboard.print_game_over()
        scoreboard.reset()
        snake.reset()


#   detect collision with the tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.print_game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()