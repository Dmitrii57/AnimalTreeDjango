from django.db import models

class Kingdoms(models.Model):
    title = models.TextField(unique=True)
    list_url = models.TextField(unique=True)

    class Meta:
        app_label='species'
        managed = True
        db_table = 'kingdoms'