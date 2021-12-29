from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class MyModelBase(models.Model):
    subject = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

    class Meta:
        abstract = True


class Courses(MyModelBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ["-id"]

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Lesson(MyModelBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Courses, related_name="lessons", on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag', related_name="lessons", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)