import uuid

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(db_column='Id', primary_key=True, default=uuid.uuid4)
