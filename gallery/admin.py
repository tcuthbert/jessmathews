from django.contrib import admin
from django.forms import ModelForm
from zipfile import ZipFile
from gallery.models import Photo, Category


# Register your models here.
def handle_uploaded_zipfile(request):
    return

class PhotoAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'image')

    def get_form(self, request, obj=None, **kwargs):
        return super(PhotoAdmin, self).get_form(request, obj, **kwargs)
        
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PhotoAdmin, self).save_model(request, obj, form, change)
admin.site.register(Photo, PhotoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
admin.site.register(Category, CategoryAdmin)
