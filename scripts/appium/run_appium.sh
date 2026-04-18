#!/bin/bash

export ANDROID_HOME=~/Library/Android/sdk
export PATH=$ANDROID_HOME/emulator/:$PATH
export PATH=$ANDROID_HOME/platform-tools/:$PATH
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin/:$PATH

PORT=4723
ADDRESS="127.0.0.1"

echo "--- Appium Server Manager ---"
echo "Checking if port $PORT is busy..."


PID=$(lsof -t -i:$PORT)

if [ -n "$PID" ]; then
    echo "Killing existing Appium process ($PID) on port $PORT..."
    kill -9 $PID
    sleep 2
fi

echo "Starting Appium Server on $ADDRESS:$PORT..."
echo "Note: Running in ATTACHED mode. Use Ctrl+C to stop the server."
echo "------------------------------------------------------------"


appium --address $ADDRESS --port $PORT --base-path /wd/hub --allow-insecure=uiautomator2:chromedriver_autodownload
