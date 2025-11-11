import tkinter as tk
import pygame
import turtle
import threading
import time

class MultiDemo:
    def __init__(self):
        self.running = True

    def tkinter_demo(self):
        """Tkinter демонстрация"""
        root = tk.Tk()
        root.title("Tkinter in Docker VNC")
        root.geometry("400x300")

        label = tk.Label(root, text="Hello from Tkinter!", font=("Arial", 16))
        label.pack(pady=20)

        button = tk.Button(root, text="Click me!",
                          command=lambda: label.config(text="Button clicked!"))
        button.pack(pady=10)

        # График
        canvas = tk.Canvas(root, width=300, height=150, bg="white")
        canvas.pack(pady=10)

        # Рисуем простой график
        points = []
        for x in range(0, 300, 5):
            y = 75 + 50 * math.sin(x/20)
            points.append(x)
            points.append(y)

        canvas.create_line(points, fill="blue", width=2)

        root.mainloop()

    def pygame_demo(self):
        """Pygame демонстрация"""
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Pygame Demo")
        clock = pygame.time.Clock()

        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        circles = []

        for i in range(5):
            circles.append({
                'pos': [i*100+50, 200],
                'radius': 30,
                'color': colors[i % len(colors)],
                'speed': [random.uniform(-3, 3), random.uniform(-3, 3)]
            })

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))

            # Обновление и отрисовка кругов
            for circle in circles:
                circle['pos'][0] += circle['speed'][0]
                circle['pos'][1] += circle['speed'][1]

                # Отскок от границ
                if circle['pos'][0] <= circle['radius'] or circle['pos'][0] >= 600 - circle['radius']:
                    circle['speed'][0] *= -1
                if circle['pos'][1] <= circle['radius'] or circle['pos'][1] >= 400 - circle['radius']:
                    circle['speed'][1] *= -1

                pygame.draw.circle(screen, circle['color'],
                                 [int(circle['pos'][0]), int(circle['pos'][1])],
                                 circle['radius'])

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def turtle_demo(self):
        """Turtle демонстрация"""
        screen = turtle.Screen()
        screen.setup(800, 600)
        screen.bgcolor("black")
        screen.title("Turtle Graphics")

        # Создаем несколько черепашек
        turtles = []
        colors = ["red", "green", "blue", "yellow", "purple"]

        for i, color in enumerate(colors):
            t = turtle.Turtle()
            t.speed(0)
            t.color(color)
            t.penup()
            t.goto(-300 + i*150, 0)
            t.pendown()
            turtles.append(t)

        # Анимация
        for angle in range(0, 360, 5):
            for i, t in enumerate(turtles):
                t.clear()
                t.setheading(angle + i*72)
                t.forward(100)
                t.backward(100)

            time.sleep(0.1)

            if not self.running:
                break

        screen.bye()

    def run_all(self):
        """Запуск всех демо в разных потоках"""
        threads = []

        # Tkinter в главном потоке
        tk_thread = threading.Thread(target=self.tkinter_demo)
        tk_thread.daemon = True
        threads.append(tk_thread)

        # Pygame в отдельном потоке
        pygame_thread = threading.Thread(target=self.pygame_demo)
        pygame_thread.daemon = True
        threads.append(pygame_thread)

        # Turtle в отдельном потоке
        turtle_thread = threading.Thread(target=self.turtle_demo)
        turtle_thread.daemon = True
        threads.append(turtle_thread)

        # Запуск всех потоков
        for thread in threads:
            thread.start()

        # Ожидание завершения
        try:
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            self.running = False
            print("Shutting down...")

if __name__ == "__main__":
    demo = MultiDemo()
    demo.run_all()
