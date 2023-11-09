from django.urls import path
from . import views # точка означает что папка та же что и у urls(этого файла)

app_name = "shop"
urlpatterns = [
    path("", views.index, name= "index"),
    path("asd/", views.index, name= "testpage"),
    path("course/<int:course_id>", views.single_course, name="single_course"),
]
#В этом файле был создан первый маршрут в приложении shop
#К нему привязали функцию вида views.index, указали название маршрута index