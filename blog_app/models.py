from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_status = models.BooleanField(default=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='post_img/', default='post_img/post.png', blank=True, null=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name="blog_tag")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False, null=False)
    short_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
