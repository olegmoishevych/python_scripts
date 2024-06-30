import pygetwindow as gw
import psutil
import time

blocked_websites = ["youtube", "tiktok"]

while True:
  windows = gw.getAllTitles()
  for window in windows:
    if any(site in window.lower() for site in blocked_websites):
      print(f"Found blocked site in window: {window}")
      win = gw.getWindowsWithTitle(window)[0]
      win.close()
  time.sleep(1)
