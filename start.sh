#!/bin/bash
set -e  # stop on any error

# --- RUN THE MAIN PROGRAM ---
echo "Running program..."
python3 -u dqr.py | tee logs.txt

