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
# =============================================================================
# CPU Auto Profiler Package
# =============================================================================
# Prerequisito: integrazione "Profiler" installata in HA
#   Impostazioni > Dispositivi e servizi > Aggiungi integrazione > Profiler
#
# Installazione:
#   1. Copia questo file in /config/packages/cpu_auto_profiler.yaml
#   2. Assicurati che configuration.yaml contenga:
#      homeassistant:
#        packages: !include_dir_named packages
#   3. Riavvia Home Assistant
#
# I file .cprof generati si trovano in /config/
# Copiali in /share/snakeviz/ per visualizzarli con l'addon SnakeViz
# =============================================================================

input_number:
  cpu_profiler_threshold:
    name: "CPU Profiler - Soglia CPU %"
    icon: mdi:speedometer
    min: 10
    max: 100
    step: 5
    initial: 80
    unit_of_measurement: "%"
    mode: slider

  cpu_profiler_duration:
    name: "CPU Profiler - Durata cattura"
    icon: mdi:timer-outline
    min: 10
    max: 300
    step: 10
    initial: 60
    unit_of_measurement: "s"
    mode: slider

  cpu_profiler_cooldown:
    name: "CPU Profiler - Cooldown tra catture"
    icon: mdi:timer-sand
    min: 60
    max: 3600
    step: 60
    initial: 300
    unit_of_measurement: "s"
    mode: slider

input_boolean:
  cpu_profiler_enabled:
    name: "CPU Profiler - Abilitato"
    icon: mdi:bug-play

automation:
  - id: cpu_auto_profiler
    alias: "CPU Auto Profiler"
    description: >-
      Avvia automaticamente il profiler HA quando l'uso CPU supera
      la soglia configurata. Genera file .cprof visualizzabili con SnakeViz.
    mode: single
    max_exceeded: silent
    triggers:
      - trigger: numeric_state
        entity_id: sensor.processor_use
        above: input_number.cpu_profiler_threshold
        for:
          seconds: 10
    conditions:
      - condition: state
        entity_id: input_boolean.cpu_profiler_enabled
        state: "on"
    actions:
      - variables:
          duration: "{{ states('input_number.cpu_profiler_duration') | int(60) }}"
          cpu_now: "{{ states('sensor.processor_use') }}"
          threshold: "{{ states('input_number.cpu_profiler_threshold') }}"
          cooldown: "{{ states('input_number.cpu_profiler_cooldown') | int(300) }}"
      - action: persistent_notification.create
        data:
          title: "⏳ Profiler avviato"
          message: >-
            CPU al {{ cpu_now }}% (soglia: {{ threshold }}%).

            Profiling in corso per {{ duration }} secondi.

            Inizio: {{ now().strftime('%H:%M:%S') }}
          notification_id: cpu_profiler_status
      - action: profiler.start
        data:
          seconds: "{{ duration }}"
      - delay:
          seconds: "{{ duration }}"
      - action: persistent_notification.create
        data:
          title: "✅ Profiler completato"
          message: >-
            Cattura completata alle {{ now().strftime('%H:%M:%S') }}.

            Durata: {{ duration }}s — CPU al momento del trigger: {{ cpu_now }}%.

            I file .cprof e callgrind sono in /config/.

            Copia i .cprof in /share/snakeviz/ per visualizzarli con SnakeViz.
          notification_id: cpu_profiler_status
      - delay:
          seconds: "{{ cooldown }}"```

Then copy generated `.cprof` file from `/config/` to `/share/snakeviz/`.
