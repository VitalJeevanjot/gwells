"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from django.contrib.gis.db import models

from gwells.models.common import AuditModelStructure
from gwells.db_comments.patch_fields import patch_fields
from wells.models import Well
from aquifers.models import Aquifer


patch_fields()


# BulkHistory does not use AuditModelStructure as that adds update_user and
# update_date columns that are not needed for a un-changeable historical record
# table.
class BulkHistory(AuditModelStructure):
    """
    A abstract class for all bulk history changes
    """
    class Meta:
        abstract = True
        ordering = ['-created_date']


class BulkWellAquiferCorrelationHistory(BulkHistory):
    """
    Keeps track of the changes to the well aquifer correlation from a bulk change
    """
    class Meta:
        db_table = 'bulk_well_aquifer_correlation_history'

    id = models.AutoField(
        db_column='bulk_well_aquifer_correlation_history_id',
        primary_key=True, verbose_name='Bulk History Id',
        db_comment=('The primary key for the bulk_history table'))
    well = models.ForeignKey(
        Well, db_column='well_tag_number', on_delete=models.PROTECT, blank=False, null=False,
        db_comment=('The file number assigned to a particular well that has it\'s aquifer correlation changed'))
    update_to_aquifer = models.ForeignKey(
        Aquifer, db_column='to_aquifer_id', on_delete=models.PROTECT, blank=False,
        null=False, verbose_name='Aquifer ID Number',
        db_comment=('The aquifer that this well is to be correlated with'))
    update_from_aquifer = models.ForeignKey(
        Aquifer, db_column='from_aquifer_id', on_delete=models.PROTECT, blank=True,
        null=True, verbose_name='Aquifer ID Number',
        db_comment=('The aquifer that this well was previously correlated with'))
