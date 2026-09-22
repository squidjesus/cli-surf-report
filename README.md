# CLI Surf Report

A command-line surf conditions report app that retrieves current marine and weather
conditions for saved surf spots using the Open-Meteo API.

## Requirements

- Python 3.13 or newer
- Internet access for weather and marine reports

## Installation

Install directly from GitHub with `pip`:

```bash
python3 -m pip install "git+https://github.com/squidjesus/cli-surf-report.git"
```
Or with `uv`:

```bash
uv tool install "git+https://github.com/squidjesus/cli-surf-report.git"
```
For development, clone the repository and install in editable mode:

```bash
git clone https://github.com/YOUR_USERNAME/cli-surf-report.git
cd cli-surf-report
uv venv
source .venv/bin/activate
uv pip install -e .
```

## First Run

The app creates it's SQLite database automatically on first run, followed by a prompt to add the included demo surf spots (or add your own).

On first run, you can load and view the conditions report for all demo spots with:
```bash
surf report
> 1
```

Demo spots can also be loaded at any time with:
```bash
surf demo-spots
```

The database is stored at:
`~/.local/share/cli-surf-report/surf_spots.db`

## Usage

`surf --help`

`surf report` - Gets and displays the conditions report for all spots in the database.

`surf report Pipeline Mavericks` - Gets the report for given spots, matching on [name].

`surf list` - List all saved spots.

`surf list --detail` - List saved spots with all details.

`surf add` - Add a surf spot via the subsequent prompts.

`surf remove Pipeline` - Removes [name] spot from the database.

`surf demo-spots` - Add the included demo spots to the database

## Color Coding

Some weather data values are color coded to indicate 'ideal', 'good', 'mid', or 'poor' conditions for that value based on the optimal conditions for a given surf spot.

Ideal swell direction (as a general rule) is opposite to the direction a surf spot is facing. Swell direction is displayed as the direction the swell is 'coming from'.

Example: **SE** facing surf spot = ideal swell direction of **SE**.

Ideal wind conditions are the opposite, originating from the direction the surf spot is facing and moving towards the ocean, aka **Offshore**.

Example: **SE** facing surf spot = ideal wind direction of **NW**

The wind condition color rating is also affected by the magnitude of wind present, as strong winds can have a negative impact regardless of a 'good' direction, and vice-versa.

Example output:
<img width="1238" height="152" alt="Screenshot 2026-09-22 084737" src="https://github.com/user-attachments/assets/791b347a-bed8-4718-b211-b74827f56047" />



## Data Sources

Weather and Marine data provided by the [Open-Meteo API](https://open-meteo.com/).

## Features on my list to add:

- Hourly forecast report.
- Overall 'condition rating' for a set of conditions at a given spot.
- Tide information (all sources of Tide data I found required API keys, wanted to keep it simple for now.)
- Bulk-import of surf spots.
- Secondary/tertiary swell data.
- "Favoriting" or grouping spots.
