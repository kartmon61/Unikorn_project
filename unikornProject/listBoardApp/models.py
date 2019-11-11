from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()

class Posting(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    content = RichTextUploadingField()
    post_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.post_hit = self.post_hit+1
        self.save()

class PostingComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    posting = models.ForeignKey(Posting,on_delete=models.CASCADE)
    author = models.CharField(max_length=200,null=True,default=1)