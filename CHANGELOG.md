# Changelog

All notable changes to this project will be documented in this file.

This project follows **Semantic Versioning (SemVer)**.

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

* Improved the shooting cooldown implementation by passing the last shot timestamp to the timer function.
* Refactored gameplay systems into reusable functions for improved readability and maintainability.
* Updated project documentation to reflect the latest gameplay features.

---

## [0.4.0] - 2026-07-01

### Added

* Random asteroid spawning system.
* Randomized asteroid movement with horizontal drift.
* Real-time score display based on survival time.
* Custom timer event for spawning meteors.
* Meteor management system using dynamic lists.
* `pygame.math.Vector2` for directional asteroid movement.

### Changed

* Refactored gameplay into reusable update functions (`laser_update()`, `meteor_update()`, `laser_timer()`, and `display_score()`).
* Improved game loop organization by separating input handling, updates, and rendering.

---

## [0.3.0] - 2026-06-30

### Added

* Mouse-controlled player movement.
* Laser shooting mechanic.
* Shooting cooldown system.
* Frame-rate-independent laser movement using delta time.
* Dynamic laser management (creation, movement, and removal).
* Mouse click controls for firing lasers.

### Changed

* Refactored laser logic into reusable functions.
* Updated the README with the latest project features and controls.

---

## [0.2.0] - 2026-06-29

### Added

* Mouse-controlled player movement.
* Frame rate capped at 120 FPS.
* Custom game title rendered using a TrueType font.
* Improved game loop organization following the Input → Update → Render pattern.

### Changed

* Refined the rendering pipeline to ensure the correct draw order (background → player → UI text).
* Added project versioning.

---

## [0.1.0] - 2026-06-28

### Added

* Initial Pygame project setup.
* 1280 × 720 game window.
* Custom window title.
* Background image rendering.
* Player ship sprite rendering.
* Custom font loading and title display.
* Core game loop structure.
* Clean application shutdown.
