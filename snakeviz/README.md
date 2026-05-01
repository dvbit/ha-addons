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

## CPU Auto Profiler Package

Automate profiling of Home Assistant based on CPU usage. This package starts 
the Profiler integration when CPU exceeds a configurable threshold.

### Setup

1. Ensure the **Profiler** integration is installed:
   **Settings → Devices & Services → Create Integration → Profiler**

2. Download `cpu_auto_profiler.yaml` from the repository

3. Copy to: `config/packages/cpu_auto_profiler.yaml`

4. Ensure `configuration.yaml` contains:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```

5. Restart Home Assistant

### Configuration

Three input_number sliders become available:

- **CPU Profiler - Soglia CPU %** (default: 80%) — Trigger threshold
- **CPU Profiler - Durata cattura** (default: 60s) — Profile duration
- **CPU Profiler - Cooldown tra catture** (default: 300s) — Minimum time between captures

Enable via: **input_boolean.cpu_profiler_enabled**

### Workflow

1. When CPU exceeds threshold for 10+ seconds, profiling starts automatically
2. Persistent notification shows capture status
3. Profile file (`.cprof`) is saved to `/config/` after capture completes
4. Copy the `.cprof` file to `/share/snakeviz/` to visualize with this add-on
5. Open SnakeViz web UI and browse your profile

### Example

```yaml
# Manually trigger profiler via service
service: profiler.start
data:
  seconds: 60
```

Then copy generated `.cprof` file from `/config/` to `/share/snakeviz/`.
