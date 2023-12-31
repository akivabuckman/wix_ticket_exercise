# Generated by Django 4.2.3 on 2023-07-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('userEmail', models.EmailField(max_length=254)),
                ('creationTime', models.DateTimeField()),
                ('labels', models.JSONField(null=True)),
            ],
        ),
    ]
