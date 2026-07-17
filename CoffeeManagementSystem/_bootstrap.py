"""
CoffeeShopManagementSystem Bootstrap
This module ensures proper Python path setup for all subprocess instances
"""
import sys
import os

# Get the project root directory
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path if not already there
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Set PYTHONPATH environment variable
os.environ['PYTHONPATH'] = _project_root

# Change to the CoffeeManagementSystem directory for relative file paths
_app_dir = os.path.join(_project_root, 'CoffeeManagementSystem')
if os.path.exists(_app_dir):
    os.chdir(_app_dir)
