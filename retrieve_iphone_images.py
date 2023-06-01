import pyicloud

# Replace with your iCloud username and password
username = 'user@example.com'
password = 'password'

# Connect to iCloud
api = pyicloud.PyiCloudService(username, password)

# Get a list of all photos in the iCloud Photo Library
photos = api.photos.all

# Select the desired photo from the list
photo = photos[0]

# Download the photo
photo.download()