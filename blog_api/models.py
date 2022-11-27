from django.db import models

# Create your models here.
class Countries(models.TextChoices):
    AFG = "AFG", 'Afghanistan'
    ALB = 'ALB', 'Albania'
    DZA = 'DZA', 'Algeria'
    FIN = 'FIN', 'Finland'
    FRA = 'FRA', 'France'
    DEU = 'DEU', 'Germany'
    IND = 'IND', 'India'
    ITA = 'ITA', 'Italy'
    MEX = 'MEX', 'Mexico'
    UZB = 'UZB', 'Uzbekistan'
    USA = 'USA', 'United States of America'

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100, choices=Countries.choices, )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'author',
        verbose_name_plural = 'authors'

class PublisherModel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=125, choices=Countries.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'publisher',
        verbose_name_plural = 'publishers'

class PostModel(models.Model):
    author =models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    published_by = models.ForeignKey(PublisherModel, on_delete=models.CASCADE, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post',
        verbose_name_plural = 'posts'


