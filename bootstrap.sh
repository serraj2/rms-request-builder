#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# ✅ Check that python3 exists
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ python3 not found. Please install it before running this script."
  exit 1
fi

# ✅ Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "🔧 Creating virtual environment..."
  python3 -m venv venv
fi

# ✅ Activate virtual environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# ✅ Upgrade pip safely (skip if not allowed)
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip --break-system-packages || echo "⚠️ Skipping pip upgrade due to system restrictions"

# ✅ Install required dependencies
echo "📦 Installing dependencies..."
python3 -m pip install --break-system-packages -r requirements.txt

# ✅ Launch the main app
echo "✅ Launching RMS Request Builder..."
python3 rmsPlaceReq.py
