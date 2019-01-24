# Generated by Django 2.1.5 on 2019-01-18 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0013_auto_20180712_2107'),
        ('wells', '0052_merge_20190116_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitysubmission',
            old_name='driller_responsible',
            new_name='person_responsible',
        ),
        migrations.RenameField(
            model_name='well',
            old_name='driller_responsible',
            new_name='person_responsible',
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='person_responsible',
            field=models.ForeignKey(blank=True, db_column='person_responsible_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.Person', verbose_name='Person Responsible for Drilling'),
        ),
        migrations.AlterField(
            model_name='well',
            name='person_responsible',
            field=models.ForeignKey(blank=True, db_column='person_responsible_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.Person', verbose_name='Person Responsible for Drilling'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='company_of_person_responsible',
            field=models.ForeignKey(blank=True, db_column='org_of_person_responsible_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.Organization', verbose_name='Company of person responsible for drilling'),
        ),
        migrations.AddField(
            model_name='well',
            name='company_of_person_responsible',
            field=models.ForeignKey(blank=True, db_column='org_of_person_responsible_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.Organization', verbose_name='Company of person responsible for drilling'),
        ),
    ]
