from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null= True)

    def __unicode__(self):    # 2.7版本
        return self.title

    def __str__(self):     # 3.5版本
        return self.title