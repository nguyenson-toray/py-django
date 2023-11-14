from django.db import models

# Create your models here.


class GuestInfo(models.Model):
    name = models.CharField(max_length=200)
    id_card = models.CharField(max_length=12)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    pub_date = models.DateTimeField("date published")
