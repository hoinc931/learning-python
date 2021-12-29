from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Courses, Lesson, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CoursesSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        return request.build_absolute_uri(path)

    class Meta:
        model = Courses
        fields = ["id", "subject", "created_date", 'image', "category"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "subject", "image", "created_date", "updated_date", "course"]


class LessonDetailSerializer(LessonsSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonsSerializer.Meta.model
        fields = LessonsSerializer.Meta.fields + ["content", "tags"]
