# Generated by Django 4.2 on 2023-04-09 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0015_user_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='birthday',
            field=models.DateField(null=True, verbose_name='дата рождения'),
        ),
        migrations.AddField(
            model_name='form',
            name='birthday_place',
            field=models.CharField(max_length=255, null=True, verbose_name='место рождения'),
        ),
        migrations.AddField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='почта'),
        ),
        migrations.AddField(
            model_name='form',
            name='end_practice',
            field=models.DateField(null=True, verbose_name='дата конца пркатики'),
        ),
        migrations.AddField(
            model_name='form',
            name='number',
            field=models.PositiveBigIntegerField(max_length=11, null=True, verbose_name='номер телефона'),
        ),
        migrations.AddField(
            model_name='form',
            name='patronymic',
            field=models.CharField(max_length=255, null=True, verbose_name='отчество'),
        ),
        migrations.AddField(
            model_name='form',
            name='start_practice',
            field=models.DateField(null=True, verbose_name='дата начала практики'),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=255, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='form',
            name='surname',
            field=models.CharField(max_length=255, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='form',
            name='training_way',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.trainingway', verbose_name='направление'),
        ),
        migrations.AlterField(
            model_name='form',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.user', verbose_name='пользователь'),
        ),
    ]
