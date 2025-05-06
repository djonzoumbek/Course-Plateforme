from django.db import models



class PublishStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'pub', 'Published',
    COMING_SOON = 'soon', 'Coming soon'

class AccessRequirement(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email required'


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # images
    access = models.CharField(max_length=25, choices=AccessRequirement.choices, default=AccessRequirement.ANYONE)
    status = models.CharField(max_length=25, choices=PublishStatus.choices, default=PublishStatus.DRAFT)

