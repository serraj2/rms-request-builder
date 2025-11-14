#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# ✅ Check if python3 is available
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ python3 is not installed or not found in PATH."
  exit 1
fi

# ✅ Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "🔧 Creating virtual environment with python3..."
  python3 -m venv venv
fi

# ✅ Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# ✅ Upgrade pip
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip --break-system-packages || echo "⚠️ Skipping pip upgrade due to system restrictions"

# ✅ Install required dependencies
echo "📦 Installing dependencies from requirements.txt..."
python3 -m pip install --break-system-packages -r requirements.txt

# ✅ Launch the main application
echo "✅ Launching RMS Request Builder..."
python3 rmsPlaceReq.py

