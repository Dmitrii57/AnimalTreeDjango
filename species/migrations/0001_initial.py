# Generated by Django 2.1.3 on 2018-11-29 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kingdoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('list_url', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'kingdoms',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('page_url', models.TextField()),
                ('type', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='species.Kingdoms')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='species.Species')),
            ],
            options={
                'db_table': 'list',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together={('kingdom', 'title', 'type')},
        ),
    ]
