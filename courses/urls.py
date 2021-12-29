from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register("categories", views.CategoryViewSet, 'category')
routers.register("courses", views.CoursesViewSet, "course")
routers.register("lessons", views.LessonViewSet, "lesson")
# routers.register("category/create", views.CategoryViewSet, 'create category')

urlpatterns = [
    path('', include(routers.urls)),
]
