# Generated by Django 2.1.5 on 2019-02-24 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fieldset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('position', models.IntegerField()),
                ('fieldset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Fieldset')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='fieldset',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Resume'),
        ),
        migrations.AddField(
            model_name='field',
            name='fieldset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Fieldset'),
        ),
    ]
