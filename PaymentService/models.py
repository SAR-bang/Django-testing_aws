from django.db.models import *


class Permission(Model):
    title = CharField(max_length=7)
    module = CharField(max_length=15)
    description = TextField()

    class Meta:
        ordering = 'title',
        verbose_name_plural = 'Permission'
        db_table = 'permission'


class RolePermission(Model):
    permission = ForeignKey(Permission, on_delete=CASCADE)
    user = IntegerField()


