from django.contrib import admin
from .models import Category,Food
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']
class FoodsAdmin(admin.ModelAdmin):
    exclude = ['created_dt','updated_dt']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Food,FoodsAdmin)