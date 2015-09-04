from django.contrib import admin

from .models import Category, Graph, Scategory, MetaCategory

#collapse
class GraphInline(admin.TabularInline):
    model = Graph
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    inlines = [GraphInline]

class GraphAdmin(admin.ModelAdmin):
    list_display = [
        'graph_id',
        'category',
        'seriesid',
        'geosetid',
        'geomapping',
        'votes' ,
        'notes' ,
    ]    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Graph, GraphAdmin)
admin.site.register(Scategory)
admin.site.register(MetaCategory)