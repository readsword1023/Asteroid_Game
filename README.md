# Asteroids

A simple Asteroids game built with Python and [pygame](https://www.pygame.org/). Fly your ship, shoot asteroids, and rack up points before one hits you.

## Features

- Ship controls with rotation, thrust and shooting
- Asteroids that split into smaller ones when shot (large -> medium -> small)
- Score system with a live score counter in the top-right corner
- 8-bit starry night sky background with twinkling stars
- Pixel-art look: the ship, asteroids and shots are drawn at low resolution and scaled up
- Game over screen showing your final score, with a quick restart

## Requirements

- Python 3.13 or newer
- Git
- pygame 2.6.1 (installed automatically by the steps below)

## Quick start

```bash
git clone https://github.com/readsword1023/Asteroid_Game.git
cd Asteroid_Game
uv run main.py
```

No uv? See the full setup steps below.

## Setup after cloning

```bash
git clone https://github.com/readsword1023/Asteroid_Game.git
cd Asteroid_Game
```

The virtual environment (`.venv`) is not stored in the repo, so you create your own below. It is built for your system and needs no cleanup.

Pick **one** of the two options below.

### Option 1: uv (recommended)

[uv](https://docs.astral.sh/uv/) reads `pyproject.toml` / `uv.lock`, installs the right Python and pygame version, and runs the game.

1. Install uv:
   - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Run the game:
   ```bash
   uv run main.py
   ```

### Option 2: plain Python and pip

1. Create and activate a virtual environment:
   - Windows (PowerShell): `py -3.13 -m venv .venv` then `.venv\Scripts\Activate.ps1`
   - Windows (cmd): `py -3.13 -m venv .venv` then `.venv\Scripts\activate.bat`
   - macOS / Linux: `python3.13 -m venv .venv` then `source .venv/bin/activate`
2. Install the dependency:
   ```bash
   pip install pygame==2.6.1
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Updating to the latest version

If you already cloned the game, run `git pull` inside the project folder to get the latest version, then run the game again.

## Controls

| Key     | Action                  |
| ------- | ----------------------- |
| `W`     | Move forward            |
| `S`     | Move backward           |
| `A`     | Rotate left             |
| `D`     | Rotate right            |
| `Space` | Shoot                   |

## Scoring

The score is shown in the top-right corner of the screen.

| Asteroid | Points                |
| -------- | --------------------- |
| Large    | 20 (when it splits)   |
| Medium   | 50 (when it splits)   |
| Small    | 100 (when destroyed)  |

The values can be changed in `constants.py`.

## Game over and restart

If an asteroid hits your ship, a **GAME OVER** screen shows your **Final Score**.

| Key          | Action                |
| ------------ | --------------------- |
| `R`          | Restart a new game    |
| `Enter`      | Exit the game         |

All other keys are ignored on this screen, so an accidental key press won't dismiss it. Closing the window also exits.

## Project layout

| File               | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| `main.py`          | Game loop, score display, game over / restart screen     |
| `player.py`        | The player's ship (movement, rotation, shooting)         |
| `asteroid.py`      | Asteroids, splitting and score values                    |
| `asteroidfield.py` | Spawns asteroids at the screen edges                     |
| `shot.py`          | Bullets fired by the ship                                |
| `background.py`    | Starry sky background                                    |
| `constants.py`     | Settings: screen size, speeds, scoring                   |
| `logger.py`        | Writes game state/events to `.jsonl` log files           |

## Customizing

- Point values: `SCORE_*` in `constants.py`
- Sky colour, star count and twinkle speed: top of `background.py`
- Ship speed, shot speed and cooldown: `constants.py`
- Pixel size (how chunky the 8-bit look is): `PIXEL_SIZE` in `constants.py` (use a number that divides 1280 and 720, such as 2, 4 or 8)

## Notes

- Running the game writes `game_state.jsonl` and `game_events.jsonl` in the project folder (see `logger.py`).
- On Windows 11 / recent Windows 10 you can also run the game inside WSL; WSLg shows the pygame window automatically.

## Troubleshooting

- **Cloned before `.venv` was removed from the repo** and getting errors like "bad interpreter" or a missing Python: delete the old `.venv` folder (`Remove-Item -Recurse -Force .venv` on Windows, `rm -rf .venv` on macOS / Linux), then follow the setup steps again.

- **`python` / `py` not found or wrong version**: install Python 3.13+ from [python.org](https://www.python.org/downloads/) and re-open your terminal.
- **PowerShell won't activate the venv** ("running scripts is disabled"): run `Set-ExecutionPolicy -Scope Process Bypass` and try again, or use Option 1.
- **`ModuleNotFoundError: No module named 'pygame'`**: the virtual environment isn't active, or pygame wasn't installed. Re-do the steps for your option.
- **No window on Linux over SSH / headless**: pygame needs a display; run it on a machine with a desktop session.
