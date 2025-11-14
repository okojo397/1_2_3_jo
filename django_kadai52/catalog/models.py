from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=40)
    summary = models.TextField(blank=True)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-published_at','-id')
    def __str__(self): return f"{self.title} / {self.author}"
