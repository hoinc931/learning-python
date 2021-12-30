from rest_framework import viewsets, generics, status
from .models import Category, Courses, Lesson, Tag
from .serializers import CategorySerializer, CoursesSerializer, LessonsSerializer, LessonDetailSerializer
from .paginator import BasePagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404, JsonResponse


# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['post'], detail=False, url_path='create')
    def create_cate(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        name = request.data.get('name')
        get_category = Category.objects.filter(name=name)

        # print("this is name: " + str(len(name)))
        if len(name) <= 5:
            return Response({"message": "Category name must be more 5 characters.", "data": None}, status=status.HTTP_411_LENGTH_REQUIRED)

        if get_category.exists():
            return Response({"message": "Category was existed.", "data": None}, status=status.HTTP_400_BAD_REQUEST)
        # print("this is get: " + str(get_category.exists()))

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category was created", "data": str(get_category)}, status=status.HTTP_201_CREATED)

        return Response({"message": "Category was not created", "data": None}, status=status.HTTP_404_NOT_FOUND)


# Create Category
class CreateCategoryViewSet(viewsets.ViewSet, generics.CreateAPIView):
    model = Category
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Category was created", "data": str(serializer)}, status=status.HTTP_201_CREATED)

        return JsonResponse({"message": "Category was not created", "data": None}, status=status.HTTP_404_NOT_FOUND)


class CoursesViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = CoursesSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        courses = Courses.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            courses = courses.filter(subject__icontains=q)

        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            courses = courses.filter(category_id=category_id)

        return courses

    @action(methods=['get'], detail=True, url_path='lessons')
    def get_lessons(self, request, pk):
        # course = Courses.objects.get(pk=pk)
        # lessons = course.lessons.filter(active=True)

        lessons = self.get_object().lessons.filter(active=True)

        kw = request.query_params.get('kw')
        if kw is not None:
            lessons.filter(subject__icontains=kw)

        return Response(LessonsSerializer(lessons, many=True).data, status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonDetailSerializer

    @action(methods=['post'], detail=True, url_path="tags")
    def add_tag(self, request, pk):
        try:
            lesson = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tags = request.data.get('tags')
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    lesson.tags.add(t)

                lesson.save()
                return Response(self.serializer_class(lesson).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)
