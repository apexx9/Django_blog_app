from django.conf import settings
from django.db import models
from django.utils import timezone


#creating objects, methods and actions
class Post(models.Model):
    #author described as a foreign key linking to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #title having a max length for its characters.
    title = models.CharField(max_length=200)
    # Text Field with no max-length
    text = models.TextField()
    #using the date model to handle date checking for the app.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #this handles the publishing date and saving of the app
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title