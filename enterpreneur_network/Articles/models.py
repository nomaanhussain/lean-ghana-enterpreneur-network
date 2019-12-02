from django.db import models
from django.contrib.auth.models import User	
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
from django.conf import settings

class Author(models.Model):
    author_name = models.CharField(max_length=250)
    profile_picture = models.ImageField(blank=True, null=True, help_text='Add picture of author')
    about_author = models.CharField(max_length=1000, help_text='Add something about author')
    website = models.URLField(max_length=250, blank=True, null=True, help_text="Add URL of your website")
    linkedin = models.URLField(max_length=250, blank=True, null=True, help_text="Add URL of your linkedin account")
    facebook = models.URLField(max_length=250, blank=True, null=True, help_text="Add URL of your FB account")
    insta = models.URLField(max_length=250, blank=True, null=True, help_text="Add URL of your insta account")
    others = models.URLField(max_length=250, blank=True, null=True,  help_text="Add other URL (e.g github account etc)")

    class Meta:
        ordering = ['author_name']

    def __str__(self):
        return self.author_name


class Category(models.Model):
    category_title = models.CharField(max_length=100, help_text="Add category of article")

    class Meta:
        ordering = ['category_title']

    def __str__(self):
        return self.category_title


class Article(models.Model):
    title = models.CharField(max_length=100)
    #overview = models.TextField()
    thumbnail = models.ImageField(help_text='Add image related to your blog')
    categories = models.ManyToManyField(Category)
    content = RichTextUploadingField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    ARTICLE_STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    #featured = models.BooleanField()
    status = models.CharField(
        max_length=1,
        choices=ARTICLE_STATUS,
        default='d',
        help_text='Status of articles',
    )

    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('Articles:article-detail', kwargs = {'slug':self.slug})

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Comment')
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.user.username


