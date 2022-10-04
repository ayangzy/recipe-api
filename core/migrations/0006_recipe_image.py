# Generated by Django 4.1.1 on 2022-10-04 12:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_recipe"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                null=True, upload_to=core.models.recipe_image_file_path
            ),
        ),
    ]
