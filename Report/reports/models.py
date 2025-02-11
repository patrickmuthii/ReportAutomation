from django.db import models



# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content    
# Create your models here.
