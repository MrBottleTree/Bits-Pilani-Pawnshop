# Generated by Django 5.1.6 on 2025-03-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bits', '0003_feedback_feedbackimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
