# Generated by Django 4.1.2 on 2022-12-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_post_rec_posts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[
                    ("education", "Education"),
                    ("science-and-technology", "Science and Tech"),
                    ("entertainment", "Entertainment"),
                    ("finance", "Finance"),
                    ("general", "General"),
                ],
                default="general",
                max_length=50,
            ),
        ),
    ]
