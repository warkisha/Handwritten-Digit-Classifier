# Handwritten-Digit-Classifier
Is an interactive app for capturing handwritten digits. It uses a convolutional neural network (CNN) trained on the MNIST dataset to predict the digits that users draw on a canvas.

## Description 
This project is a simple handwritten digit app using a neural network and a GUI. The app allows the user to draw digits on a canvas, make predictions using machine learning models, and display the results. The model is trained on the MNIST dataset and can be improved with user feedback.

## Main Features
- **Digital Drawing**: Users can draw digits on the canvas.
- **Prediction**: The model makes predictions based on the digit they draw.
- **Feedback**: Users can correct by correctly predicting the digit model and adjust the label if necessary.

## How it works **Model:**
_The model is a convolutional neural network trained on the MNIST dataset. It uses Conv2D, MaxPooling2D, Flatten, Dense, and Dropout layers._
**GUI:** _The interface is built using Tkinter. Users can draw on the canvas, and the app will process the image to make a prediction._ **Feedback:** _ If the prediction models are incorrect, the user can enter the correct label. This information is used to train the models further._ 
**Dependencies:** 
- TensorFlow
- NumPy
- Pillow
- Tkinter


______________________________________________________________________________________________________________________________________________________
## Описание

Этот проект представляет собой простое приложение для распознавания рукописных цифр, использующее нейронную сеть и графический интерфейс. Приложение позволяет пользователю рисовать цифры на холсте, делать предсказания с помощью модели машинного обучения и отображать результаты. Модель обучается на наборе данных MNIST и может улучшаться с помощью обратной связи от пользователей.

## Основные функции

- **Рисование цифр**: Пользователи могут рисовать цифры на холсте.
- **Предсказание**: Модель делает предсказание на основе нарисованной цифры.
- **Обратная связь**: Пользователи могут подтвердить, правильно ли предсказала модель цифру, и, при необходимости, скорректировать метку.

## Как это работает

**Модель:**
_Модель представляет собой сверточную нейронную сеть, обученную на наборе данных MNIST.
Она использует слои Conv2D, MaxPooling2D, Flatten, Dense и Dropout._

**Графический интерфейс:**
_Интерфейс создан с помощью Tkinter.
Пользователи могут рисовать на холсте, и приложение будет обрабатывать изображение для предсказания._

**Обратная связь:**
_Если предсказание модели неверное, пользователи могут ввести правильную метку.
Эта информация используется для дополнительного обучения модели._

**Зависимости:**
- TensorFlow
- NumPy
- Pillow
- Tkinter
