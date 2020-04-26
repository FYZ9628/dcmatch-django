# Generated by Django 3.0.5 on 2020-04-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.IntegerField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'user2',
                'db_table': 'user2',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
