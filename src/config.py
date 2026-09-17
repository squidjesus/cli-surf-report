from pathlib import Path

# Database path
PROJECT_ROOT = Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / "data" / "surf_spots.db"

# Demo spots CSV path
DEMO_PATH = PROJECT_ROOT / "data" / "demo_surf_spots.csv"

# Surf Spot Fields
FIELDS = ['name', 'location', 'type', 'lat', 'long', 'facing', 'notes']