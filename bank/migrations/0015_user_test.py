# Generated by Django 4.2 on 2023-04-08 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0014_user_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.testresult'),
        ),
    ]