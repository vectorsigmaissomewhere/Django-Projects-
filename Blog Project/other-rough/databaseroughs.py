from django.db import models
from django.contrib.auth.models import User  # Or your custom user model
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    heading_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    first_paragraph = models.TextField()
    second_paragraph_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    second_paragraph = models.TextField()
    third_paragraph_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    third_paragraph = models.TextField()
    fourth_paragraph_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    fourth_paragraph = models.TextField()
    fifth_paragraph_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    fifth_paragraph = models.TextField()
    sixth_paragraph_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    sixth_paragraph = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog_post.title}'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Reply by {self.user.username} on {self.comment.id}'

class BlogPostLike(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on {self.blog_post.title}'

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on comment {self.comment.id}'

class ReplyLike(models.Model):
    reply = models.ForeignKey(Reply, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on reply {self.reply.id}'






python manage.py makemigrations
python manage.py migrate




from django.contrib import admin
from .models import BlogPost, Comment, Reply, BlogPostLike, CommentLike, ReplyLike

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(BlogPostLike)
admin.site.register(CommentLike)
admin.site.register(ReplyLike)

