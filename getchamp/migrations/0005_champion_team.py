# Generated by Django 4.0.2 on 2022-04-07 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getchamp', '0004_alter_champion_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='Team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='getchamp.teambuilder'),
        ),
    ]