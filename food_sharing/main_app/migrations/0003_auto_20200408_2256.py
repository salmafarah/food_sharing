# Generated by Django 3.0.3 on 2020-04-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200407_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='contact_name',
            field=models.CharField(max_length=100, verbose_name='Contact person'),
        ),
        migrations.AlterField(
            model_name='food',
            name='count',
            field=models.CharField(max_length=10, verbose_name='How much is available'),
        ),
        migrations.AlterField(
            model_name='food',
            name='exp',
            field=models.CharField(max_length=10, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='food',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Pick-up location'),
        ),
        migrations.AlterField(
            model_name='food',
            name='tele',
            field=models.CharField(max_length=100, verbose_name='Contact number'),
        ),
    ]