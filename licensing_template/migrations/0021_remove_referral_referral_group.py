# Generated by Django 3.2.4 on 2022-02-01 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("licensing_template", "0020_auto_20220201_0856"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="referral",
            name="referral_group",
        ),
    ]
