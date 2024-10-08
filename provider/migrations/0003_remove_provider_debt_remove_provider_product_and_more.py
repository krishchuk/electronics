# Generated by Django 5.1 on 2024-08-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_alter_contact_country_alter_contact_house_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='product',
        ),
        migrations.AlterField(
            model_name='provider',
            name='type',
            field=models.CharField(choices=[('0', 'завод'), ('1', 'розничная сеть'), ('2', 'индивидуальный предприниматель')], default=0, max_length=1, verbose_name='тип'),
        ),
        migrations.AddField(
            model_name='provider',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='provider.product', verbose_name='продукты'),
        ),
    ]
