# Generated by Django 3.0.1 on 2020-11-07 23:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snack', 'snack')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.ManyToManyField(to='users.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fooditem', models.ManyToManyField(to='users.Fooditem')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
