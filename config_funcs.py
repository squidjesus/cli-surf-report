import os
import json
import click

APP_NAME = "cli-surf-report"
CONFIG_DIR = click.get_app_dir(APP_NAME)
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)