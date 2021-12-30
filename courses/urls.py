from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
# routers.register("create", views.CreateCategoryViewSet, 'created')
routers.register("categories", views.CategoryViewSet, 'category')
routers.register("courses", views.CoursesViewSet, "course")
routers.register("lessons", views.LessonViewSet, "lesson")

urlpatterns = [
    path('', include(routers.urls)),
]
