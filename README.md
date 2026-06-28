# 🚀 Asteroid Shooter

A 2D space shooter being built in Python with Pygame, where the player will pilot a ship through an asteroid field, dodging and destroying incoming asteroids to survive as long as possible.

This project is part of my personal portfolio as I work toward a Junior Software Engineer role in Dublin, Ireland.

## 🏗️ Current Status

This project is in early development. So far, the foundation is in place:

* The game window opens at a fixed resolution (1280x720).
* The main game loop runs continuously, structured around three phases: input handling, game state updates, and drawing to the screen.
* The window can be closed safely — clicking quit shuts Pygame down cleanly and exits the program.

No gameplay yet (ship, asteroids, shooting) — see **Planned Features** below.

## 🛠 Concepts Practiced So Far

* **Pygame initialization** — `pygame.init()` sets up all of Pygame's internal modules before anything else can run.
* **Display surface** — `pygame.display.set_mode()` creates the surface (window) that everything will eventually be drawn onto.
* **Event loop** — `pygame.event.get()` retrieves all input events (like the close-window click) that occurred since the last frame.
* **Game loop structure** — organizing the loop into clear phases (input → update → draw), the pattern almost every game engine is built around.
* **Clean program exit** — `pygame.quit()` and `sys.exit()` together make sure Pygame shuts down properly and the script terminates without errors.

## 🚀 Running the Project

```bash
python main.py
```

Requires:

* Python 3
* Pygame (`pip install pygame`)

## 🗺️ Planned Features

* Player ship that moves and rotates based on keyboard input.
* Asteroids that spawn and move across the screen.
* Shooting mechanic to destroy asteroids.
* Collision detection between bullets, asteroids, and the player.
* Frame-rate independent movement using delta time.
* Score tracking and a game-over state.
* Sound effects and background music.

## 🧑‍💻 Author

Douglas Aguiar — [GitHub](https://github.com/DouglasAguiar-Dev)
Self-taught Python developer working toward a Junior Software Engineer role in Dublin, Ireland.