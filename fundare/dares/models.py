from django.db import models
from django.contrib.auth import get_user_model

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
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_dares'
        )

    @property
    def show_all_charities(self):
        all_charities = self.charity_set.all()
        charity_names = []
        for charity in all_charities:
            charity_names.append(charity.charity)
        return charity_names

class Charity(models.Model):
    name = models.CharField(max_length=200, default='')
    dares = models.ManyToManyField(Dares)

class Dollars(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField()
    dares = models.ForeignKey(
        'Dares',
        on_delete=models.CASCADE,
        related_name='dollars'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_dollars'
    )