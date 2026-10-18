"""
FEAT-002 stub: organizations models.

The database-builder adds fields to these models in a concurrent session.
The full field list (name, is_active for ClientOrg; name, sid, org FK for
SAPApplication) is defined in DBD-001 v0.1 § Module: organizations.
"""

from django.db import models


class ClientOrg(models.Model):
    """Represents a client organization whose SAP applications AMS supports.

    Fields are added by the database-builder in Mode B (FEAT-002).
    """

    class Meta:
        db_table = "organizations_clientorg"


class SAPApplication(models.Model):
    """Represents an SAP application belonging to one client organization.

    Fields are added by the database-builder in Mode B (FEAT-002).
    """

    class Meta:
        db_table = "organizations_sapapplication"
