# Generated by Django 4.1 on 2022-09-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=128, verbose_name="Заголовок")),
                ("author", models.CharField(max_length=256, verbose_name="Автор")),
                ("publication_date", models.DateField()),
                (
                    "annotation",
                    models.TextField(max_length=1024, verbose_name="Аннотация"),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "ordering": ("id",),
            },
        ),
    ]
