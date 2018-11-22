from django.db import models

class Kingdoms(models.Model):
    title = models.TextField(unique=True)
    list_url = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'kingdoms'


class List(models.Model):
    id = models.BigAutoField(primary_key=True)
    kingdom = models.ForeignKey(Kingdoms, models.DO_NOTHING)
    title = models.TextField()
    page_url = models.TextField()
    type = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list'
        unique_together = (('kingdom', 'title'),)