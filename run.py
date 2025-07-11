#!/usr/bin/env python3
"""
TrendScout Backend Runner
Run this file to start the Reddit data fetching backend
"""

import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        sys.exit(1)

def main():
    """Main runner function"""
    print("🚀 Starting TrendScout Backend...")

    # Install requirements
    install_requirements()
    
    # Start the application
    print("🔄 Starting Reddit data fetching service...")
    try:
        from app import app
        print("✅ Backend started successfully!")
        print("📊 Dashboard: http://localhost:3000")
        print("🔗 API: http://localhost:5000")
        print("📡 Fetching data from Reddit every 15 minutes...")
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n👋 Shutting down TrendScout Backend...")
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
