# Changelog

All notable changes to this project will be documented in this file.

This project follows **Semantic Versioning (SemVer)**.

---

## [0.3.0] - 2026-06-30

### Added

* Shooting mechanic — lasers fire on mouse click and travel upward from the ship.
* Automatic removal of lasers once they move off-screen.
* Delta-time-based movement for frame-rate-independent gameplay.

---

## [0.2.0] - 2026-06-29

### Added

* Mouse-controlled player movement.
* Frame rate capped at 120 FPS using `pygame.time.Clock`.
* Improved game loop organization following the Input → Update → Render pattern.

### Changed

* Refined the rendering pipeline to ensure the correct draw order (background → player → UI text).
* Updated the project documentation with a development roadmap and versioning.

---

## [0.1.0] - 2026-06-28

### Added

* Initial Pygame project setup.
* 1280 × 720 game window.
* Custom window title.
* Background image rendering.
* Player ship sprite rendering.
* Custom font loading and title display.
* Event handling for clean application shutdown.
* Core game loop structure.