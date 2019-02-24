from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
from .models import Resume, Fieldset, Field, ImageField

class FieldInline(admin.TabularInline):
    model = Field
    fk_fieldset = 'fieldset'
    extra = 0

class ImageFieldInline(admin.TabularInline):
    model = ImageField
    fk_fieldset = 'fieldset'
    extra = 0

class FieldsetAdmin(admin.ModelAdmin):
    inlines = [FieldInline,ImageFieldInline]
    fk_resume = 'resume'

class ResumeAdmin(admin.ModelAdmin):
    model = Resume
    extra = 1
    

admin.site.register(Fieldset,FieldsetAdmin)
admin.site.register(Resume,ResumeAdmin)