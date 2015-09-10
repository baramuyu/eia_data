from django.contrib import admin

from .models import Scategory, MetaCategory

#collapse
class ScategoryAdmin(admin.ModelAdmin):
    list_display = [
        'series_id',
        str('category1_id'),
        str('category2_id')
    ]

class MetaCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_id',
        'name'
    ]    

admin.site.register(Scategory, ScategoryAdmin)
admin.site.register(MetaCategory, MetaCategoryAdmin)