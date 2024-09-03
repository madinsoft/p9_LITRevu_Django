from django.conf import settings
from django.db import models



# Create your models here.
class Review(models.Model):
    """Critique avec comme champs : title, comment"""
    title = models.fields.CharField(max_length=100)
    # score bouton selection
    comment = models.fields.CharField(max_length=600)
    def __str__(self):
        return f'{self.title}'

class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048, null=True, blank=True)
    #photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default= '2')
    #date_created = models.DateTimeField(auto_now_add=True, default=timezone.now)
    #user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #changer après avec : rajouter to=settings.AUTH_USER_MODEL et modifier on_delete=models.CASCADE
    # Après que la class User soit supprimée
    #image = models.fields.ImageField(null=True, blank=True)
    # reponse terminal : module "django.db.models.fields' has no attribute 'ImageField'. Did you mean: 'DateField'?
    #time_created = models.fields.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'



