from django.db import models

class Scategory(models.Model):
    series_id = models.CharField(primary_key=True, max_length=100)
    category1 = models.ForeignKey('MetaCategory', related_name='category1', null=True)
    category2 = models.ForeignKey('MetaCategory', related_name='category2', null=True)
    category3 = models.ForeignKey('MetaCategory', related_name='category3', null=True)
    category4 = models.ForeignKey('MetaCategory', related_name='category4', null=True)
    category5 = models.ForeignKey('MetaCategory', related_name='category5', null=True)
    category6 = models.ForeignKey('MetaCategory', related_name='category6', null=True)
    category7 = models.ForeignKey('MetaCategory', related_name='category7', null=True)
    category8 = models.ForeignKey('MetaCategory', related_name='category8', null=True)
    category9 = models.ForeignKey('MetaCategory', related_name='category9', null=True)
    geoset_id = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.series_id

class MetaCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
