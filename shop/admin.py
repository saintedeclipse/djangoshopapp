from django.contrib import admin
from .models import Course, Category


# Register your models here.

admin.site.index_title = "welcome to the rice fields"
admin.site.site_title = "djamboo"
admin.site.site_header = "adminka"

class FirstCourseAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','date_of_creation')

class CoursesInLine(admin.TabularInline):
    model = Course
    extra = 1

class FirstCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','date_of_creation')
    fieldsets = [(None, {'fields': ['title']}),
                 ('Dates', {'fields': ['date_of_creation'],
                            'classes': ['collapse']})]
    inlines = [CoursesInLine]
admin.site.register(Category, FirstCategoryAdmin)
admin.site.register(Course, FirstCourseAdmin)