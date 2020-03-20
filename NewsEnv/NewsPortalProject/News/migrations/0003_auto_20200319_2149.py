# Generated by Django 3.0.4 on 2020-03-19 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20200319_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_description',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('Comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
