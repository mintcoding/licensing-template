# Generated by Django 3.2.4 on 2022-02-01 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("licensing_template", "0021_remove_referral_referral_group"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="proposalassessment",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="proposalassessment",
            name="referral_group",
        ),
    ]
