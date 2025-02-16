from django.db import models

class book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    isbn = models.CharField(max_length=500)
    available = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["author"]
        unique_together = (("isbn", "title"),)
        verbose_name = "book"
        verbose_name_plural = "books"
