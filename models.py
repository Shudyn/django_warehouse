# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticlesArticle(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField()
    author = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'articles_article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clients(models.Model):
    client_id = models.IntegerField()
    name = models.CharField(blank=True, null=True)
    phone_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clients'


class Contracts(models.Model):
    contract_id = models.IntegerField()
    operation_type = models.CharField()
    clients_client_id = models.IntegerField(blank=True, null=True)
    suppliers_supplier_id = models.IntegerField(blank=True, null=True)
    valuables_data_barcode = models.IntegerField(blank=True, null=True)
    product_amount = models.IntegerField()
    expected_completion_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'contracts'


class Deliveries(models.Model):
    op_journal_operation_id = models.IntegerField(unique=True)
    worker_worker_id = models.IntegerField(unique=True)
    address = models.CharField()
    pending_delivery_date = models.DateField()
    worker_worker_id1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deliveries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Finances(models.Model):
    finance_op_id = models.IntegerField()
    payment = models.IntegerField()
    contracts_contract_id = models.IntegerField(unique=True)
    transaction_completion = models.CharField()

    class Meta:
        managed = False
        db_table = 'finances'


class Jobs(models.Model):
    job_name = models.CharField()
    payment = models.IntegerField()
    planned_work_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class OperationsJournal(models.Model):
    operation_id = models.IntegerField()
    operation_type = models.CharField()
    contracts_contract_id = models.IntegerField(unique=True)
    valuables_data_barcode = models.IntegerField(blank=True, null=True)
    clients_client_id = models.IntegerField(blank=True, null=True)
    worker_worker_id = models.IntegerField(blank=True, null=True)
    operation_date = models.DateField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operations_journal'


class Registry(models.Model):
    barcode = models.IntegerField()
    name = models.CharField(blank=True, null=True)
    amount = models.IntegerField()
    zone_type = models.CharField()
    zone_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registry'


class Relation16(models.Model):
    worker_worker_id = models.IntegerField()
    registry_barcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relation_16'


class Suppliers(models.Model):
    supplier_id = models.IntegerField()
    name = models.CharField(blank=True, null=True)
    phone_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'suppliers'


class ValuablesData(models.Model):
    barcode = models.IntegerField()
    package_type = models.CharField()
    value = models.TextField(blank=True, null=True)  # This field type is a guess.
    appropriate_zones = models.CharField()

    class Meta:
        managed = False
        db_table = 'valuables_data'


class Worker(models.Model):
    worker_id = models.IntegerField()
    name = models.CharField()
    jobs_job_name = models.CharField()
    date_of_birth = models.DateField(blank=True, null=True)
    passport_number = models.IntegerField()
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker'
