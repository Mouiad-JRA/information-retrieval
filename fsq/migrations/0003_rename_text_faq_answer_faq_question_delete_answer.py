# Generated by Django 4.1.2 on 2022-10-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsq', '0002_problem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='text',
            new_name='answer',
        ),
        migrations.AddField(
            model_name='faq',
            name='question',
            field=models.TextField(db_index=True, default='1'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]