# Generated by Django 3.2.4 on 2022-01-24 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("licensing_template", "0013_alter_proposalgeometry_proposal"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="proposal",
            name="customer_status",
        ),
    ]
