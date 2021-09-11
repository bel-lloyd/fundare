from django.db import models

class Dares(models.Model):
    title = models.CharField(max_length=200)
    dare_description = models.TextField()
    rules = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_for_dare = models.DateTimeField()
    for_charity = models.TextField()
    charity_url = models.URLField()
    owner = models.CharField(max_length=200)

class Dollars(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField()
    dare = models.ForeignKey(
        'Dares',
        on_delete=models.CASCADE,
        related_name='dollars'
    )
    supporter = models.CharField(max_length=200)
    # created_at = models.DateTimeField()