# Generated by Django 2.2.5 on 2019-09-07 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartInv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='catergory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items2', to='smartInv.Catergory'),
        ),
    ]
