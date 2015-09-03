from django.db import models

class Graph(models.Model):
    graph_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category')
    seriesid = models.CharField(unique=False, max_length=50)
    geosetid = models.CharField(unique=False, max_length=50, null=False)
    geomapping = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    notes = models.TextField('Notes', null=False, blank=True, default='')

    def __unicode__(self):
        return str(self.seriesid)

class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.name