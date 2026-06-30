# 🚀 Asteroid Shooter
Version: v0.3.0

A 2D arcade space shooter built with Python and Pygame. Pilot your spacecraft through deep space, dodge incoming asteroids, and eventually destroy them to survive for as long as possible.

This project is part of my software engineering portfolio as I develop practical experience in Python, game development, and software engineering while working toward a Junior Full-Stack Software Developer role in Ireland.

## ✨ Features

* 1280 × 720 game window
* Background and player ship rendering
* Custom font and game title
* Mouse-controlled player movement
* Shooting mechanic — click to fire lasers that travel upward and are automatically removed once off-screen
* Frame-rate-independent movement using delta time
* Frame rate capped at 120 FPS for consistent performance
* Structured game loop (Input → Update → Render)
* Clean application shutdown

## 🛠️ Concepts Practiced

This project demonstrates the following concepts:

* Pygame initialization
* Display and window management
* Image and font loading
* Surface rendering with `blit()`
* Positioning objects using `pygame.Rect`
* Mouse input handling (movement and click events)
* Event-driven programming
* Delta-time-based movement for frame-rate independence
* Frame-rate control using `pygame.time.Clock`
* Dynamic list management (spawning and removing objects during gameplay)
* Game loop architecture
* Asset organization

## 📂 Project Structure

```
asteroid-shooter/
│
├── assets/
│   └── graphics/
│       ├── background.png
│       ├── laser.png
│       ├── ship.png
│       └── subatomic.ttf
│
├── main.py
├── README.md
├── CHANGELOG.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

* Python 3.12+
* Pygame

Install Pygame:

```
pip install pygame
```

Run the project:

```
python main.py
```

## 🎮 Controls

* **Move your mouse** — steer the ship
* **Left-click** — fire a laser

## 🧰 Built With

* Python
* Pygame
* Git
* GitHub

## 🎯 Learning Goals

This project is helping me improve my understanding of:

* Game development fundamentals
* Object-oriented programming
* Event-driven programming
* Real-time game loops
* Clean and maintainable Python code
* Professional Git and GitHub workflows

## 👨‍💻 Author

Douglas Aguiar
Computer Science student at Dorset College Dublin and self-taught Python developer building projects to become a Junior Full-Stack Software Developer in Ireland.
GitHub: https://github.com/DouglasAguiar-Dev