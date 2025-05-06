import helpers
from django.db import models
from cloudinary.models import CloudinaryField


helpers.cloudinary_init()

class PublishStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'pub', 'Published',
    COMING_SOON = 'soon', 'Coming soon'

class AccessRequirement(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email required'

#def image upload function
def upload_image(instance, filename):
    return f"{filename}"



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    #published_date = models.DateTimeField(auto_now_add=True)
    #images = models.ImageField(upload_to=upload_image, blank=True, null=True)
    image = CloudinaryField('image', null=True, blank=True)
    access = models.CharField(max_length=5, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=5, choices=PublishStatus.choices, default=PublishStatus.DRAFT)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

