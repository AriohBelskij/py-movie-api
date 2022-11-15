# Generated by Django 4.1.3 on 2022-11-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=55)),
                ("description", models.TextField(blank=True)),
                ("duration", models.IntegerField()),
            ],
        ),
    ]
