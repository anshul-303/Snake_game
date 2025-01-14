# 🐍 Snake Game

Welcome to the **Snake Game**! A classic game built using Python's `turtle` module, where you control a snake that grows longer each time it eats food, but watch out – avoid hitting walls or your own tail!

---

## 🎮 **How to Play**

- Use the **arrow keys** to control the snake (up, down, left, right).
- **Eat the food** (represented as a small square) to grow the snake.
- **Avoid walls** and your own tail. If you collide, the game is over!
- The goal is to eat as much food as possible and grow the snake to a long length!

---

## 🚀 **Features**

- **Smooth gameplay** with responsive controls.
- **Growing snake**: Each time the snake eats, it grows longer.
- **Increasing difficulty**: As the snake gets longer, it becomes harder to avoid collisions.
- **Simple UI** with a classic game design.

---

## 🔧 **Installation Instructions**

Follow these steps to get the Snake Game running on your local machine:

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
Navigate to the project directory:

bash
Copy code
cd snake-game
Run the game using Python:

bash
Copy code
python snake_game.py
🖼️ Screenshots
Here are some screenshots to give you a glimpse of the game in action:

Image 1: The Snake Game in action!

## 🛠️ **Technologies Used**

This project uses the following technologies:

- **Python**: A powerful programming language used to build the game.
- **turtle Module**: A simple and easy-to-use Python library for creating graphics and animations.
- **OOP Concepts**: Object-Oriented Programming principles used to structure the game components.

---

## 🖥️ **How the `turtle` Module is Used**

The `turtle` module is central to this game, providing the drawing and animation capabilities. Here’s how it’s used:

1. **Creating the Snake🐍**: 
   - The snake is represented as a collection of **turtle objects**, each one acting as a segment of the snake’s body.
   - The **turtle’s shape** and **movement** are controlled through the module’s API, allowing smooth animations as the snake moves.
   
2. **Game Window🖥️**: 
   - The game window, background, and other graphical elements are drawn using **turtle’s window setup** and **screen properties**.
   - The `screen.bgcolor()` method is used to set the background color for the game on a display screen of 600x600 pixels.

3. **Food🍉**:
   - The food is another **turtle object** that appears at random locations on the screen.
   - The `turtle` is used to move and place the food, and collision detection is handled to grow the snake when it eats the 
     food.

4. **Controls🎮**:
   - The arrow keys are captured using **turtle’s `onscreenclick()`** or **keyboard event handlers** for player input.

---

## 💡 **How OOP Concepts are Used**

**Object-Oriented Programming** (OOP) is used to structure the game into manageable and reusable components. Here’s how OOP is implemented:

### 1. **Snake Class**

- **Purpose**: Manages the snake, its body, movement, and growth.
- **Attributes**:
  - `segments`: A list of turtle objects that represent the snake’s body.
  - `head`: A reference to the first turtle object (the head of the snake).
- **Methods**:
  - `move()`: Moves the entire snake, updating the position of each segment.
  - `grow()`: Adds a new segment to the snake’s body when it eats food.

### 2. **Food Class**

- **Purpose**: Represents the food that the snake eats to grow.
- **Attributes**:
  - `food`: A turtle object representing the food on the screen.
  - `position`: A basic pair of x and y coordinates according to the pixel settings for display.
- **Methods**:
  - `create_food()`: Creates a new food item at a random location.
  - `move_food()`: Moves the food to a new random location after being eaten by the snake.

### 3. **Game Class**

- **Purpose**: Manages the entire game, including setup, score tracking, and controlling the game flow. It basically
  corresponds to the main file which is the primary file importing the different components of the game from other files.
- **Attributes**:
  - `score`: The current score of the game.
  - `screen`: The game screen where play is visible is created using the turtle module.
  - `snake`: An instance of the Snake class to manage the snake.
  - `food`: An instance of the Food class to generate and manage food.
- **Main file  key code elements**:
  - A simple **while** loop which relies on whether the game is running or not based on a boolean value is the crux of 
    program.
  - The score which is display on the top is updated in real time when snake eats its food.
  - `game_over()`: It ends the game while still displaying the user score and also display a Game Over text to let player
   know. 

---


📜 License:
- This project is licensed under the MIT License – see the LICENSE file for details.

🙏 Acknowledgments:
- Inspired by the classic Snake Game that many of us have played on early mobile phones and gaming systems.

GitHub: anshul303

Thank You! 🐳
