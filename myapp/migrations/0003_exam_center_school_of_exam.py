# Generated by Django 4.0.2 on 2022-05-29 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_admin_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('landmark', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='school_of_exam',
            fields=[
                ('exam_center_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.exam_center')),
                ('school_name', models.CharField(max_length=150)),
                ('school_created_at', models.DateTimeField(auto_now=True)),
                ('school_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('myapp.exam_center',),
        ),
    ]