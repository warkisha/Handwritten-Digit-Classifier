import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageOps

# Загрузка и нормализация данных
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Создание модели
model = models.Sequential([
    layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Графический интерфейс
class DigitRecognizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Digit Recognizer")

        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        self.predict_button = tk.Button(self.master, text="Predict", command=self.predict_digit)
        self.predict_button.pack(side=tk.RIGHT)

        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.last_x = None
        self.last_y = None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)

    def predict_digit(self):
        img = preprocess_image(self.image)
        pred = model.predict(img)
        digit = np.argmax(pred)
        messagebox.showinfo("Prediction", f"Predicted Digit: {digit}")

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill='black', width=8)
            self.draw.line([self.last_x, self.last_y, x, y], fill='black', width=8)
        self.last_x = x
        self.last_y = y

    def reset_last(self, event):
        self.last_x = None
        self.last_y = None

def preprocess_image(img):
    img = img.resize((28, 28))
    img = ImageOps.invert(img)
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 28, 28)
    return img

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()
