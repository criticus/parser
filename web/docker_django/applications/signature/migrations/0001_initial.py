# Generated by Django 2.0.9 on 2019-03-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('birthday', models.DateField(default=None, null=True)),
                ('phone', models.CharField(default=None, max_length=15, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Новий'), (2, 'У роботі'), (3, 'Опрацьовано'), (4, ' Відхилено')], default=1)),
                ('service_title', models.IntegerField(choices=[(1, 'Тестовий бізнес-процес')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
