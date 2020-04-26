# Generated by Django 3.0.5 on 2020-04-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200424_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test3',
            fields=[
                ('id', models.IntegerField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'test3',
                'db_table': 'test3',
            },
        ),
        migrations.DeleteModel(
            name='User2',
        ),
    ]