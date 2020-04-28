# Generated by Django 3.0.5 on 2020-04-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('createdBy', models.CharField(max_length=50)),
            ],
        ),
    ]
