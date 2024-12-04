from django.db import models
from django.utils import timezone

class Contact(models.Model):

    # models.someField() define qual o tipo do campo/atributo
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # blank = True informa que o campo é opcional.
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
