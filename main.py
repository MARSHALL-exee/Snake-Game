from turtle import Screen
from snake import Snake
from food import Food
from scorebord import Scorebord
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#70B26E")
screen.title("Snake xenziya")
screen.tracer(0)

snake = Snake()
food = Food()
scorebord = Scorebord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





# MOVE SNAKE BODY AUTOMATIC
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebord.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scorebord.game_over()

    for segment in snake.segments[-1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorebord.game_over()

screen.exitonclick()
