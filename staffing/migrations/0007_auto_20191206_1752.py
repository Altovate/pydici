# Generated by Django 2.2.5 on 2019-12-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0006_auto_20191206_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='analytic_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffing.AnalyticCode', verbose_name='analytic code'),
        ),
    ]
