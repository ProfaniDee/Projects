import webbrowser
import time

# Set the desired total duration in seconds
total_duration = 360  # 6 minutes

# Set the interval between browser openings in seconds
interval = 30

# Calculate the number of iterations based on the total duration and interval
iterations = total_duration // interval

# Loop for the specified number of iterations
for _ in range(iterations):
    # Open the browser with the desired URL
    webbrowser.open('http://www.google.com')  # Replace with the URL you want to open

    # Wait for the specified interval
    time.sleep(interval)

# Wait for the remaining duration before exiting the program
time.sleep(total_duration % interval)