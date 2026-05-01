# SnakeViz for Home Assistant

## About

SnakeViz is a browser-based graphical viewer for Python's cProfile output.
This add-on runs SnakeViz as a web server inside Home Assistant, allowing you
to visualize and analyze Python profiling data directly from the HA interface.

## Installation

1. Add this repository to Home Assistant add-on store
2. Install "SnakeViz"
3. Start the add-on
4. Click "OPEN WEB UI"

## Usage

1. Generate a cProfile output file from your Python code:
   ```python
   import cProfile
   cProfile.run('your_function()', '/share/snakeviz/output.prof')
   ```
2. Place `.prof` files in `/share/snakeviz/` on your Home Assistant host
3. Open the SnakeViz web UI and browse to your profile files

## Configuration

No configuration is required. The add-on serves profiles from `/share/snakeviz/`.

## Network

The add-on exposes port **8080** by default. You can change the host port
in the add-on network configuration.

## Support

- [SnakeViz documentation](https://jiffyclub.github.io/snakeviz/)
- [Python cProfile documentation](https://docs.python.org/3/library/profile.html)
