# Asteroids

A small Asteroids clone built with [pygame](https://www.pygame.org/), written as the
capstone project for the [Boot.dev](https://www.boot.dev) "Build Asteroids in Python" course.

Fly a triangular ship around the screen, shoot the drifting asteroids, and watch the big
ones break apart into smaller, faster fragments. Touch one and the run is over.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Running the game

With `uv`:

```bash
uv run main.py
```

With pip and a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install pygame==2.6.1
python main.py
```

## Controls

| Key     | Action        |
| ------- | ------------- |
| `W`     | Thrust forward |
| `S`     | Thrust backward |
| `A`     | Rotate left   |
| `D`     | Rotate right  |
| `Space` | Shoot         |
| `Esc` / window close | Quit |

## How it works

The game is a plain pygame loop with no external game engine. Every frame it polls input,
updates every object by the elapsed frame time (`dt`), resolves collisions, and redraws.

| File | Responsibility |
| ---- | -------------- |
| `main.py` | Sets up the window, sprite groups, and the game loop |
| `circleshape.py` | `CircleShape` base class: position, velocity, radius, circle collision |
| `player.py` | The ship: rotation, thrust, and cooldown-limited shooting |
| `shot.py` | Bullets fired by the player |
| `asteroid.py` | Asteroids, including the logic that splits them when hit |
| `asteroidfield.py` | Spawns new asteroids off-screen at a steady rate |
| `constants.py` | Tunable values (speeds, sizes, spawn rate) in one place |
| `logger.py` | Optional JSONL logging of game state and events, used for debugging |

### Sprite groups

Rather than tracking objects in lists by hand, each class declares a `containers` tuple of
pygame sprite groups. `CircleShape.__init__` adds every new instance to those groups
automatically, so the loop can just iterate `updatable`, `drawable`, `asteroids`, and
`shots` without any bookkeeping.

### Asteroid splitting

An asteroid hit by a shot calls `split()`. If it is already at the minimum radius it simply
disappears; otherwise it spawns two smaller asteroids that inherit its velocity, rotated by
a random angle in either direction and scaled up slightly, so debris fans outward and moves
faster than the parent.

## Debug logging

`logger.py` writes `game_state.jsonl` (a snapshot roughly once per second for the first
16 seconds) and `game_events.jsonl` (hits, splits, and deaths). Both files are gitignored
and are safe to delete.

## License

[MIT](LICENSE)
