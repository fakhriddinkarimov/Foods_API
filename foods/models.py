from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64,blank=False, null=False)
    slug = models.SlugField()
    parent = models.ForeignKey('self',related_name='father',on_delete=models.CASCADE,blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=128,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    price = models.IntegerField(blank=False,null=False)
    photo = models.ImageField(upload_to='static/img/',null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=False,null=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name