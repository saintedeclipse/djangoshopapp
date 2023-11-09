from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

course_resource = CourseResource()
category_resource = CategoryResource()

api = Api(api_name='v1')
api.register(course_resource)
api.register(category_resource)

urlpatterns =[path('', include(api.urls), name="index")

              ]