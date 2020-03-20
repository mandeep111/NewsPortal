from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(TimeStamp):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class SubCategory(TimeStamp):
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name

class News(TimeStamp):
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    SubCategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    news_title = models.CharField(max_length=100)
    news_content = models.TextField()
    news_image = models.ImageField(upload_to="news")
    news_author = models.CharField(max_length=100)
    views_count = models.PositiveIntegerField(default = "1")

    def __str__(self):
        return self.news_title

class Comments(TimeStamp):
    comment = models.TextField(null=True)
    Comments = models.ForeignKey(News, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment