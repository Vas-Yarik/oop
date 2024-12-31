import tkinter as tk
import threading
import time
import random

class MovingObject:
    def __init__(self, canvas, color, size, speed):
        self.canvas = canvas
        self.color = color
        self.size = size
        self.speed = speed
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 300)
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed
        self.object_id = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

    def move(self):
        while True:
            self.x += self.dx
            self.y += self.dy

            if self.x < 0 or self.x + self.size > 400:
                self.dx *= -1
            if self.y < 0 or self.y + self.size > 300:
                self.dy *= -1

            self.canvas.move(self.object_id, self.dx, self.dy)
            time.sleep(0.02)

def start_moving_object(canvas, color, size, speed):
    obj = MovingObject(canvas, color, size, speed)
    thread = threading.Thread(target=obj.move)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Движущиеся объекты")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    start_moving_object(canvas, "red", 20, 2)
    start_moving_object(canvas, "blue", 30, 3)
    start_moving_object(canvas, "green", 25, 4)

    root.mainloop()

