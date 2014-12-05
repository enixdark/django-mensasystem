from django.db import models

# Create your models here.
class SystemIP(models.Model):
    start_ip = models.IPAddressField()
    end_ip = models.IPAddressField()
    class Meta:
        verbose_name_plural = 'Management IP'

