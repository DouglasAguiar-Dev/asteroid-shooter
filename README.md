# 🚀 Asteroid Shooter

**Version:** **v0.5.0**

A 2D arcade space shooter built with **Python** and **Pygame**. Pilot your spacecraft through deep space, destroy incoming asteroids with your laser, avoid collisions, and survive for as long as possible while your score increases over time.

This project is part of my software engineering portfolio as I develop practical experience in Python, game development, and software engineering while working toward becoming a Junior Full-Stack Software Developer in Ireland.

---

## ✨ Features

* 1280 × 720 game window
* Mouse-controlled player movement
* Laser shooting mechanic
* Shooting cooldown system
* Random asteroid spawning
* Randomized asteroid movement
* Laser vs. asteroid collision detection
* Player vs. asteroid collision detection
* Sound effects for shooting and explosions
* Background music
* Real-time score counter
* Frame-rate-independent movement using delta time
* Frame rate capped at 120 FPS
* Structured game loop (Input → Update → Render)
* Clean application shutdown

---

## 🛠️ Concepts Practiced

This project demonstrates the following concepts:

* Pygame initialization
* Display and window management
* Image, font, and audio loading
* Surface rendering with `blit()`
* Positioning objects using `pygame.Rect`
* Rectangle-based collision detection
* Mouse input handling
* Event-driven programming
* Custom timer events
* Delta-time movement
* Random number generation
* `pygame.math.Vector2`
* Dynamic list management
* Function decomposition
* Game loop architecture
* Basic game state management
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
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.12+
* Pygame

Install the dependency:

```bash
pip install pygame
```

Run the project:

```bash
python main.py
```

---

## 🎮 Controls

* **Move the mouse** — Control the ship
* **Left-click** — Fire a laser
* **Avoid asteroids** — A collision ends the game

---

## 🧰 Built With

* Python
* Pygame
* Git
* GitHub

---

## 🎯 Learning Goals

This project is helping me strengthen my understanding of:

* Game development fundamentals
* Procedural programming
* Event-driven programming
* Collision detection
* Delta-time game loops
* Audio integration
* Clean and maintainable Python code
* Professional Git and GitHub workflows

---

## 👨‍💻 Author

**Douglas Aguiar**

Computer Science student at Dorset College Dublin and self-taught Python developer building practical projects to become a Junior Full-Stack Software Developer in Ireland.

**GitHub:** https://github.com/DouglasAguiar-Dev
