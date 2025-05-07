from cloudinary.models import CloudinaryField
from django.db import models
from django.utils.text import slugify
import uuid
import helpers

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


def get_public_id_prefix(instance, *args, **kwargs):
    title = instance.title
    if title:
        slug = slugify(title)
        unique_id = str(uuid.uuid4()).replace("-", "")[:5]
        return f"courses/{slug}-{unique_id}"
    if instance.id:
        return f"courses/{instance.id}"
    return "courses"


def get_public_display_name(instance, *args, **kwargs):
    title = instance.title
    if title:
        return title
    return "Course Upload"

# course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    #published_date = models.DateTimeField(auto_now_add=True)
    #images = models.ImageField(upload_to=upload_image, blank=True, null=True)
    image = CloudinaryField('image', null=True, blank=True, public_id_prefix=get_public_id_prefix,
                            display_name=get_public_display_name, tags=["course", "thumbnail", ])
    access = models.CharField(max_length=5, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=5, choices=PublishStatus.choices, default=PublishStatus.DRAFT)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

    @property
    def image_admin_url(self):
        if not self.image:
            return ""

        image_options = {
            'width': 150,
        }
        url = self.image.build_url(**image_options)
        return url

    def get_image_thumbnail(self, is_html=False, width=500):
        if not self.image:
            return ""

        image_options = {
            'width': width,
        }
        if is_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url

# Lesson model
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    thumbnail = CloudinaryField('image', null=True, blank=True)
    video = CloudinaryField('video', null=True, blank=True, resource_type="video")
    order = models.IntegerField(default=0)
    preview = models.BooleanField(default=False, help_text="if user doesn't have access to course, can they see this ?")
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.PUBLISHED)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-updated']
