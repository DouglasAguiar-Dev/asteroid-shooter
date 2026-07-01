# 🚀 Asteroid Shooter

**Version:** **v0.4.0**

A 2D arcade space shooter built with **Python** and **Pygame**. Pilot your spacecraft through deep space, dodge incoming asteroids, destroy them with your laser, and survive for as long as possible while your score continuously increases.

This project is part of my software engineering portfolio as I develop practical experience in Python, game development, and software engineering while working toward becoming a Junior Full-Stack Software Developer in Ireland.

---

## ✨ Features

* 1280 × 720 game window
* Background and player ship rendering
* Custom font and game title
* Mouse-controlled player movement
* Shooting mechanic — click to fire lasers
* Laser cooldown system
* Random asteroid spawning
* Randomized asteroid movement
* Real-time score counter
* Frame-rate-independent movement using delta time
* Frame rate capped at 120 FPS for consistent performance
* Structured game loop (Input → Update → Render)
* Clean application shutdown

---

## 🛠️ Concepts Practiced

This project demonstrates the following concepts:

* Pygame initialization
* Display and window management
* Image and font loading
* Surface rendering with `blit()`
* Positioning objects using `pygame.Rect`
* Mouse input handling (movement and click events)
* Event-driven programming
* Custom timer events
* Delta-time-based movement
* Random number generation
* `pygame.math.Vector2` for movement
* Dynamic list management (creating, updating, and removing game objects)
* Function decomposition
* Game loop architecture
* Asset organization

---

## 📂 Project Structure

```text
asteroid-shooter/
│
├── assets/
│   └── graphics/
│       ├── background.png
│       ├── laser.png
│       ├── meteor.png
│       ├── ship.png
│       └── subatomic.ttf
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

Install Pygame:

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

---

## 🧰 Built With

* Python
* Pygame
* Git
* GitHub

---

## 🎯 Learning Goals

This project is helping me improve my understanding of:

* Game development fundamentals
* Procedural programming
* Event-driven programming
* Real-time game loops
* Delta-time movement
* Clean and maintainable Python code
* Professional Git and GitHub workflows

---

## 👨‍💻 Author

**Douglas Aguiar**

Computer Science student at Dorset College Dublin and self-taught Python developer building projects to become a Junior Full-Stack Software Developer in Ireland.

**GitHub:** https://github.com/DouglasAguiar-Dev
