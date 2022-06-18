from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    createdDate=models.DateTimeField(null=True)
    publishedDate=models.DateTimeField(null=True)

    def __str__(self) -> str:
        return super().__str__()