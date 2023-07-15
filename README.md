# PixelPost

PixelPost is a web application for sharing and organizing images. Users can create accounts, upload images, add labels to categorize them, and search for images based on labels. It provides a user-friendly interface to manage and explore images.

## Features

- User authentication: Users can create accounts, log in, and log out.
- Image upload: Users can upload images with titles and descriptions.
- Labeling: Users can add labels to categorize their images.
- Image search: Users can search for images based on labels.
- Download option: Authenticated users can download the uploaded images.
- User profile: Users can view and manage their uploaded images in their profile.

## Technologies Used

- Python3
- Django Web Framework
- HTML/CSS
- JavaScript
- Cloudinary (for image hosting)
- Imagaa AI ( for image labelling)
- Sqlite3 (database)
- Google Cloud Console (deployment)

## Setup Instructions

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/pixelpost.git
2. Install the required dependencies:
   
   ```shell
   pip install -r requirements.txt
3. Configure the database settings in settings.py. Update the DATABASES dictionary with your database details.
4. Configure the Cloudinary and Imagaa AI settings in forms.py. Update the CLOUDINARY dictionary with your Cloudinary credentials, and also add the ACEESS_TOKEN and ACCESS_SECRET of Imagaa AI.
5. Run the database migrations:
   ```shell
   python manage.py migrate
6. Start the development server:
   ```shell
   python manage.py runserver
7. Open your web browser and access the application at http://localhost:8000/.

## Deployment
The application can be deployed to a platform like Heroku using the provided Procfile and runtime.txt files. Refer to the platform's documentation for deployment instructions.

## Contributing
Contributions to the project are welcome. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

