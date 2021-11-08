# Generated by Django 3.2.5 on 2021-11-08 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dollars',
            name='dares',
        ),
        migrations.AddField(
            model_name='dollars',
            name='dare',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dollars', to='dares.dares'),
        ),
        migrations.AlterField(
            model_name='dares',
            name='dare_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='dares',
            name='rules',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='dollars',
            name='supporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supporter_dollars', to=settings.AUTH_USER_MODEL),
        ),
    ]