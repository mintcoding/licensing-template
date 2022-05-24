# Generated by Django 3.2.12 on 2022-02-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licensing_template", "0039_proposal_shapefile_json"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdditionalDocumentType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("enabled", models.BooleanField(default=True)),
            ],
        ),
    ]
