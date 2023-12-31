# Generated by Django 4.2 on 2023-11-15 22:39

from django.db import migrations, models
import ir_server.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ir_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to=ir_server.models.save_stat_to)),
            ],
        ),
    ]
