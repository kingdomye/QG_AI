import tkinter as tk
import homework_two
import numpy as np
from PIL import Image, ImageDraw, ImageTk


class MyWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("手绘输入")

        canvas_width, canvas_height = 128, 128
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        self.image = Image.new("L", (canvas_width, canvas_height), "black")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.draw = ImageDraw.Draw(self.image)

        self.drawing = False
        self.last_x, self.last_y = None, None

        self.output_area = tk.Text(self.root, height=15, width=20)
        self.output_area.pack()

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw_line(self, event):
        if self.drawing:
            x, y = event.x, event.y
            if self.last_x is not None and self.last_y is not None:
                self.draw.line((self.last_x, self.last_y, x, y), fill=255, width=7)
                self.last_x, self.last_y = x, y
                self.tk_image = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
                self.canvas.image = self.tk_image

    def stop_draw(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.image = Image.new("L", (128, 128), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
        self.canvas.image = self.tk_image

    def recognize_image(self):
        file_name = "input.jpg"
        self.image = self.image.resize((28, 28))
        self.image.save(file_name)

        nn = homework_two.Network()
        nn.create_from_memory()
        result = (nn.forward(homework_two.read_img(file_name))*100).tolist()
        max_index = result.index(max(result))
        res = ""
        for i in range(len(result)):
            res += f'{i}:{round(result[i], 3)}%\n'

        res += "最终识别结果：" + str(max_index)
        self.output_area.delete('1.0', tk.END)
        self.output_area.insert(tk.END, res)

    def run(self):
        save_button = tk.Button(self.root, text="识别", command=self.recognize_image)
        save_button.pack()

        clear_button = tk.Button(self.root, text="清除", command=self.clear_canvas)
        clear_button.pack()

        self.canvas.bind('<B1-Motion>', self.draw_line)
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<ButtonRelease-1>', self.stop_draw)

        self.root.mainloop()


if __name__ == "__main__":
    app = MyWindow()
    app.run()
