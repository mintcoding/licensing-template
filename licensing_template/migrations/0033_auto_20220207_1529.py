# Generated by Django 3.2.4 on 2022-02-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "licensing_template",
            "0032_rename_question_proposalassessmentanswer_checklist_question",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="proposalassessmentanswer",
            old_name="text_answer",
            new_name="answer_text",
        ),
        migrations.RenameField(
            model_name="proposalassessmentanswer",
            old_name="answer",
            new_name="answer_yes_no",
        ),
    ]
