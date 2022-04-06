# Generated by Django 4.0.3 on 2022-04-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrenInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Common')], default='M', max_length=1)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
    ]
