#!/usr/bin/env python3
"""
Coffee Shop Management System Launcher
Properly initializes the Python path and runs the application
"""
import sys
import os
import subprocess
import platform

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Set PYTHONPATH environment variable for any child processes
os.environ['PYTHONPATH'] = project_root

# Change to the CoffeeManagementSystem directory so relative paths work
app_dir = os.path.join(project_root, 'CoffeeManagementSystem')
os.chdir(app_dir)

# Import bootstrap to set up paths in this process
from CoffeeManagementSystem import _bootstrap

# Patch os.system to properly handle Python subprocess calls with PYTHONPATH
original_system = os.system

def patched_system(cmd):
    """Wrapper around os.system that preserves PYTHONPATH for child processes"""
    if cmd.strip().startswith('python'):
        try:
            env = os.environ.copy()
            env['PYTHONPATH'] = project_root
            
            # On Windows, use CREATE_NEW_CONSOLE to detach the process
            if platform.system() == 'Windows':
                subprocess.Popen(cmd, shell=True, env=env, 
                               creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(cmd, shell=True, env=env, preexec_fn=os.setsid)
            return 0
        except Exception as e:
            print(f"Error executing command: {e}")
            return 1
    return original_system(cmd)

os.system = patched_system

# Import and run the AccountSystem directly (skip splash screen)
from CoffeeManagementSystem import AccountSystem
from tkinter import Tk

root = Tk()
root.title('COFFEE SHOP MANAGEMENT SYSTEM')
app = AccountSystem.AccountPage(root)
root.mainloop()
