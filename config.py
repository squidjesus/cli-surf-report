from pathlib import Path
from importlib.resources import files

# Database path
PROJECT_ROOT = Path(__file__).parent.parent

DB_DIR = Path.home() / ".local" / "share" / "cli-surf-report"
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "surf_spots.db"

# Demo spots CSV path
DEMO_PATH = Path(__file__).parent / "data" / "demo_surf_spots.csv"

# Surf Spot Fields
FIELDS = ['name', 'location', 'type', 'lat', 'long', 'facing', 'notes']