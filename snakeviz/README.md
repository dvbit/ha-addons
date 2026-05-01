# SnakeViz Add-on for Home Assistant

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FYOURUSERNAME%2Fha-addons)

Python cProfile visualizer running inside Home Assistant.

## Installation

1. Click the button above or manually add this repository URL in Home Assistant:
   **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
2. Install "SnakeViz" from the add-on store
3. Start the add-on
4. Place your `.prof` files in `/share/snakeviz/`
5. Click "OPEN WEB UI" to browse and visualize profiles

## What is SnakeViz?

[SnakeViz](https://jiffyclub.github.io/snakeviz/) is a browser-based graphical
viewer for the output of Python's cProfile module. It provides interactive
icicle and sunburst visualizations of profiling data.
