from django.db import models
from django.utils.text import slugify
from .managers import MyPostManager

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField('email address', unique=True)

    def __str__(self):
        return f'username: {self.username} - email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    tags = models.CharField(max_length=100)
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True)
    author_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    objects = MyPostManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post_image"

    def save(self, *args, **kwargs):
        if not self.slug:
            last_id = max([i.id for i in Post.objects.all()])
            self.slug = slugify(self.title) + str(last_id + 1)
        super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField()
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    url = models.CharField(max_length=5000, null=True, blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

