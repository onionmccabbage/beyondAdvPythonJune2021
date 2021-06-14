import turtle # may need to pip install turtle

def main():
    turtle.setup(500, 500) # size in pixels
    # we need a window
    window = turtle.Screen()
    window.title('Move and rotate using arrow keys')
    window.bgcolor('lightblue')
    Gordon = turtle.Turtle()

    def moveForward():
        Gordon.forward(50)
    # def moveBackward():
    #     Gordon.backward(50)
    def turnLeft():
        Gordon.left(30) # degrees
    def turnRight():
        Gordon.right(30)

    def start():
        window.onkey(moveForward, 'Up')
        window.onkey(turnLeft, 'Left')
        window.onkey(turnRight, 'Right')
        # start listening for events
        window.listen()
        # we need a run loop
        window.mainloop()

    start()

if __name__ == '__main__':
    main()
