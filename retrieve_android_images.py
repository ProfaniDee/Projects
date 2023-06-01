import pyadb

# Replace with the IP address or hostname of the Android device
device_address = '192.168.1.100'

# Replace with the path to the image file on the Android device
image_path = '/sdcard/DCIM/image1.jpg'

# Replace with the local path where you want to save the image file
local_path = '/path/to/local/folder/image1.jpg'

# Connect to the Android device
device = pyadb.ADB(device_address)

# Pull the image file from the device
device.pull(image_path, local_path)