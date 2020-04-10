# Generated by Django 3.0.3 on 2020-04-09 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200407_0211'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Food')),
            ],
        ),
    ]