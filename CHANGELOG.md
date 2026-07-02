# Changelog

All notable changes to this project will be documented in this file.

This project follows **Semantic Versioning (SemVer).**

---

## [0.6.0] - 2026-07-02

### Added

* Refactored the project into an object-oriented architecture.
* `Ship` class derived from `pygame.sprite.Sprite`.
* `Laser` class derived from `pygame.sprite.Sprite`.
* `Meteor` class derived from `pygame.sprite.Sprite`.
* Dedicated `Score` class for rendering the score.
* Sprite Groups for automatic object management.
* Pixel-perfect collision detection using sprite masks.
* Rotating meteors.
* Random meteor scaling.
* Configurable shooting cooldown.
* Background music and sound effect integration within sprite classes.

### Changed

* Replaced manual object lists with `pygame.sprite.Group`.
* Moved gameplay logic into class methods (`update()`, `rotate()`, `laser_shoot()`, `meteor_collision()`, etc.).
* Improved project readability through object-oriented design.
* Simplified the main game loop by delegating behaviour to sprites.
* Updated project documentation.

---

## [0.5.0] - 2026-07-01

### Added

* Laser vs. asteroid collision detection.
* Player vs. asteroid collision detection.
* Shooting sound effects.
* Explosion sound effects.
* Background music.
* Game over when the player collides with an asteroid.

### Changed

* Improved the shooting cooldown implementation.
* Refactored gameplay into reusable helper functions.

---

## [0.4.0] - 2026-07-01

### Added

* Random asteroid spawning.
* Random asteroid movement.
* Real-time score display.
* Custom timer event for spawning meteors.
* Delta-time movement for meteors.
* `pygame.math.Vector2` movement.

### Changed

* Refactored gameplay into reusable functions.

---

## [0.3.0] - 2026-06-30

### Added

* Mouse-controlled player movement.
* Laser shooting mechanic.
* Shooting cooldown.
* Delta-time laser movement.
* Dynamic laser management.

### Changed

* Refactored laser logic into reusable functions.

---

## [0.2.0] - 2026-06-29

### Added

* Mouse-controlled player movement.
* Frame rate capped at 120 FPS.
* Custom game title.
* Structured game loop.

### Changed

* Improved rendering order.
* Added project versioning.

---

## [0.1.0] - 2026-06-28

### Added

* Initial Pygame project setup.
* Game window.
* Background rendering.
* Player sprite.
* Custom font.
* Main game loop.
* Clean application shutdown.
