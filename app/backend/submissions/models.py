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
from decimal import Decimal
import uuid
from django.utils import timezone

from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from gwells.models import AuditModel

class WellActivityCodeTypeManager(models.Manager):

    def construction(self):
        return self.get_queryset().get(code='CON')

    def legacy(self):
        return self.get_queryset().get(code='LEGACY')

    def decommission(self):
        return self.get_queryset().get(code='DEC')

    def alteration(self):
        return self.get_queryset().get(code='ALT')

    def staff_edit(self):
        return self.get_queryset().get(code='STAFF_EDIT')


class WellActivityCode(AuditModel):
    """
    Types of Well Activity.
    """
    code = models.CharField(
        primary_key=True, max_length=10,  editable=False, db_column='well_activity_type_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(timezone.datetime.max, timezone.get_default_timezone()), null=False)

    objects = models.Manager()
    types = WellActivityCodeTypeManager()

    class Meta:
        db_table = 'well_activity_code'
        ordering = ['display_order', 'description']

    def __str__(self):
        return self.description
