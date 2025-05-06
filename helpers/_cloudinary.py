import cloudinary
from decouple import config

# Configuration
def cloudinary_init():
    cloudinary.config(
        cloud_name = config('CLOUDINARY_CLOUD_NAME'),
        api_key = config('CLOUDINARY_API_KEY'),
        api_secret = config('CLOUDINARY_API_SECRET'),
        secure=True
    )
