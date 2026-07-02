# 🚀 Asteroid Shooter

**Version:** **v0.6.0**

A 2D arcade space shooter built with **Python** and **Pygame**. Control your spacecraft with the mouse, destroy incoming asteroids with lasers, avoid collisions, and survive for as long as possible while your score continuously increases.

This project is part of my software engineering portfolio as I develop practical experience in Python, object-oriented programming, game development, and software engineering while working toward becoming a Junior Full-Stack Software Developer in Ireland.

---

## ✨ Features

* 1280 × 720 game window
* Mouse-controlled player movement
* Laser shooting with cooldown
* Random asteroid spawning
* Random asteroid sizes, speeds, and movement directions
* Rotating asteroids
* Pixel-perfect collision detection using masks
* Laser vs. asteroid collisions
* Player vs. asteroid collisions (game over)
* Shooting and explosion sound effects
* Background music
* Real-time score counter
* Frame-rate-independent movement using delta time
* Object-oriented game architecture using Pygame Sprites and Sprite Groups

---

## 🛠️ Concepts Practiced

This project demonstrates the following concepts:

* Object-oriented programming (OOP)
* Classes and objects
* Inheritance with `pygame.sprite.Sprite`
* Encapsulation
* Polymorphism through `Sprite.update()`
* Sprite Groups
* Image, font, and sound loading
* Pixel-perfect collision detection using masks
* Delta-time movement
* `pygame.math.Vector2`
* Random number generation
* Event-driven programming
* Custom timer events
* Real-time game loop architecture
* Asset organization

---

## 📂 Project Structure

```text
asteroid-shooter/
│
├── assets/
│   ├── graphics/
│   │   ├── background.png
│   │   ├── laser.png
│   │   ├── meteor.png
│   │   ├── ship.png
│   │   └── subatomic.ttf
│   │
│   └── sounds/
│       ├── laser.ogg
│       ├── explosion.wav
│       └── music.wav
│
├── main.py
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.12+
* Pygame

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## 🎮 Controls

* **Move the mouse** — Control the spaceship
* **Left-click** — Fire a laser
* **Avoid meteors** — A collision ends the game

---

## 🧰 Built With

* Python
* Pygame
* Git
* GitHub

---

## 🎯 Learning Goals

This project is helping me strengthen my understanding of:

* Object-oriented programming
* Game architecture
* Sprite-based game development
* Collision detection
* Delta-time game loops
* Software design and maintainability
* Clean Python code
* Professional Git and GitHub workflows

---

## 👨‍💻 Author

**Douglas Aguiar**

Computer Science student at Dorset College Dublin and self-taught Python developer building practical projects to become a Junior Full-Stack Software Developer in Ireland.

**GitHub:** https://github.com/DouglasAguiar-Dev
