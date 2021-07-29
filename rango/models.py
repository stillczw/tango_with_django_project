from django.db import models

# Create models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    # fix plural typo
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    # field: one-to-many; one-to-one; many-to-many
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title