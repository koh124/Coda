from django.db import migrations, models
from coda.models.models import *

class Migration(migrations.Migration):

  dependencies = []

  operations = [
    migrations.CreateModel(
      name='User',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=127))
      ]
    ),
    migrations.CreateModel(
      name='Article',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('title', models.CharField(max_length=50)),
        ('body', models.TextField()),
        ('is_public', models.BooleanField(default=True)),
        ('user', models.ForeignKey(on_delete=models.CASCADE, to='user.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='Module',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=255)),
        ('is_public', models.BooleanField(default=True)),
        ('is_importable', models.BooleanField(default=True)),
        ('is_executable', models.BooleanField(default=True)),
        ('user', models.ForeignKey(on_delete=models.CASCADE, to='user.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='Language',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=255)),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='File',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('language', models.ForeignKey(on_delete=models.CASCADE, to='language.id')),
        ('file_tag_name', models.CharField(max_length=255)),
        ('code', models.TextField()),
        ('file_name', models.CharField(max_length=255)),
        ('file_path', models.CharField(max_length=1023)),
        ('is_public', models.BooleanField(default=True)),
        ('is_importable', models.BooleanField(default=True)),
        ('is_executable', models.BooleanField(default=True)),
        ('user', models.ForeignKey(on_delete=models.CASCADE, to='user.id')),
        ('article', models.ForeignKey(on_delete=models.CASCADE, to='article.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='Article_Module_Dependencies',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('article', models.ForeignKey(on_delete=models.CASCADE, to='article.id')),
        ('module', models.ForeignKey(on_delete=models.CASCADE, to='module.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='Module_File_Dependencies',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('module', models.ForeignKey(on_delete=models.CASCADE, to='module.id')),
        ('file', models.ForeignKey(on_delete=models.CASCADE, to='file.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
    migrations.CreateModel(
      name='File_File_Dependencies',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('file', models.ForeignKey(on_delete=models.CASCADE, to='file.id')),
        ('dependency_file', models.ForeignKey(on_delete=models.CASCADE, to='file.id')),
        ('created_at', models.DateTimeField(auto_now_add=True)),
        ('updated_at', models.DateTimeField(auto_now=True))
      ]
    ),
  ]
