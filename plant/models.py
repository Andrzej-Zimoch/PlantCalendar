from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Plant(models.Model):
    title = models.CharField(max_length=250, verbose_name=u"Plant's name", help_text=u"Please enter plant's name...")
    first_date= models.DateTimeField(default=datetime.now(), verbose_name=u"First water date")
    water_after= models.IntegerField(default=None, null=True, verbose_name=u"Days to next watering")
    water_ml = models.IntegerField(default=None, null=True, verbose_name=u"Water amount in ml")
    check_out = models.DateTimeField(null=True, blank=True, default=None)
    photo = models.ImageField(default=None, null=True,upload_to='gallery', verbose_name=u"Photo")
    # slug = models.SlugField(max_length=250, default='None',null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.check_out = self.first_date + timedelta(days=float(self.water_after))
        return super().save(*args, **kwargs)
   

  