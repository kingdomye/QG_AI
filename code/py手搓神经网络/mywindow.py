# import tkinter as tk
#
# import numpy as np
# from PIL import Image, ImageDraw, ImageTk
#
# import img
# import main
#
#
# class MyWindow:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("手绘输入")
#
#         canvas_width, canvas_height = 128, 128
#         self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
#         self.canvas.pack()
#
#         self.image = Image.new("RGB", (canvas_width, canvas_height), "white")
#         self.tk_image = ImageTk.PhotoImage(self.image)
#         self.draw = ImageDraw.Draw(self.image)
#
#         self.drawing = False
#         self.last_x, self.last_y = None, None
#
#         self.input_area = tk.Entry(self.root)
#         self.input_area.pack()
#
#     def start_draw(self, event):
#         self.drawing = True
#         self.last_x, self.last_y = event.x, event.y
#
#     def draw_line(self, event):
#         if self.drawing:
#             x, y = event.x, event.y
#             if self.last_x is not None and self.last_y is not None:
#                 self.draw.line((self.last_x, self.last_y, x, y), fill=0, width=5)
#                 self.last_x, self.last_y = x, y
#                 self.tk_image = ImageTk.PhotoImage(self.image)
#                 self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
#                 self.canvas.image = self.tk_image
#
#     def stop_draw(self, event):
#         self.drawing = False
#
#     def clear_canvas(self):
#         self.image = Image.new("RGB", (128, 128), "white")
#         self.draw = ImageDraw.Draw(self.image)
#         self.tk_image = ImageTk.PhotoImage(self.image)
#         self.canvas.delete("all")
#         self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
#         self.canvas.image = self.tk_image
#
#     def save_image(self):
#         file_name = "input.jpg"
#         self.image.save(file_name)
#
#         answer = self.input_area.get()
#         except_outputs = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#         except_outputs[int(answer)] = 1
#
#         inputs = img.read_img("input.jpg")
#
#         nn = main.create_network_from_json()
#         nn = main.train(nn, inputs, except_outputs)
#         print(nn.get_output())
#
#     def run(self):
#         save_button = tk.Button(self.root, text="保存", command=self.save_image)
#         save_button.pack()
#
#         clear_button = tk.Button(self.root, text="清除", command=self.clear_canvas)
#         clear_button.pack()
#
#         self.canvas.bind('<B1-Motion>', self.draw_line)
#         self.canvas.bind('<Button-1>', self.start_draw)
#         self.canvas.bind('<ButtonRelease-1>', self.stop_draw)
#
#         self.root.mainloop()
#
#
# if __name__ == "__main__":
#     app = MyWindow()
#     app.run()
