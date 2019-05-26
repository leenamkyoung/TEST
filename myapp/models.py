from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    # model.뭐뭐무머Field(추가적 뭐뭐뭐)

    def __str__(self):
        return self.title
