import requests

api_key = 'acc_23c683b3a6a6147'
api_secret = 'c45920b2b1e0885dbc39958a084ee6a4'
image_url = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

print(response.json())
