import requests
import os

api_key = 'acc_23c683b3a6a6147'
api_secret = 'c45920b2b1e0885dbc39958a084ee6a4'
image_url = 'https://pixelpost.pythonanywhere.com/media/images/image_4.jpg'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

print(response.json())

# import requests
# import os

# response = requests.get("http://localhost:8000/media/images/cloud-data_r1ZNOtcI.png")