# Generated by Django 3.2.4 on 2022-01-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licensing_template", "0018_auto_20220128_1420"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="aboriginal_site_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="building_required_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="clearing_vegetation_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="consistent_plan_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="consistent_purpose_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="environmentally_sensitive_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="exclusive_use_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="ground_disturbing_works_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="heritage_site_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="long_term_use_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="mining_tenement_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="native_title_consultation_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="significant_change_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="wetlands_impact_text",
            field=models.TextField(blank=True),
        ),
    ]
