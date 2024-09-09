from django.db import models
from django.contrib.auth.models import User
from django import forms

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    def __unicode__ (self):
        return "%s: %s" % (self.author.username, self.title)
    def get_excerpt(self):
        return self.text

class clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, max_length=150)
    phone_number = models.IntegerField()

    class Meta:
        db_table = 'clients'
        
class NewClient(forms.ModelForm):
    class Meta(object):
        model = clients
        fields = ("name", "phone_number")


class Contracts(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    operation_type = models.CharField(max_length=150)
    clients_client_id = models.IntegerField(blank=True)
    suppliers_supplier_id = models.IntegerField(blank=True)
    valuables_data_barcode = models.IntegerField(blank=True)
    product_amount = models.IntegerField()
    expected_completion_date = models.DateField()

    class Meta:
        db_table = 'contracts'

class NewContract(forms.ModelForm):
    class Meta(object):
        model = Contracts
        fields = ("operation_type", "clients_client_id", "suppliers_supplier_id", "valuables_data_barcode", "product_amount", "expected_completion_date")

class Deliveries(models.Model):
    op_journal_operation_id = models.IntegerField(primary_key=True)
    worker_worker_id = models.IntegerField()
    address = models.CharField(max_length=150)
    pending_delivery_date = models.DateField()

    class Meta:
        db_table = 'deliveries'



class Finances(models.Model):
    finance_op_id = models.IntegerField(primary_key=True)
    payment = models.IntegerField()
    contracts_contract_id = models.IntegerField()
    transaction_completion = models.CharField(max_length=150)

    class Meta:
        db_table = 'finances'


class Jobs(models.Model):
    job_name = models.CharField(primary_key=True, max_length=150)
    payment = models.IntegerField()
    planned_work_time = models.IntegerField()

    class Meta:
        db_table = 'jobs'


class OperationsJournal(models.Model):
    operation_id = models.IntegerField(primary_key=True)
    operation_type = models.CharField(max_length=150)
    contracts_contract_id = models.IntegerField(unique=True)
    valuables_data_barcode = models.IntegerField(blank=True)
    clients_client_id = models.IntegerField(blank=True)
    worker_worker_id = models.IntegerField(blank=True)
    operation_date = models.DateField()
    amount = models.IntegerField()

    class Meta:
        db_table = 'operations_journal'


class Registry(models.Model):
    barcode = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=150)
    amount = models.IntegerField()
    zone_type = models.CharField(max_length=150)
    zone_number = models.IntegerField()

    class Meta:
        db_table = 'registry'


class Relation16(models.Model):
    worker_worker_id = models.IntegerField(primary_key=True)
    registry_barcode = models.IntegerField()

    class Meta:
        db_table = 'relation_16'


class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=150)
    phone_number = models.IntegerField()

    class Meta:
        db_table = 'suppliers'


class ValuablesData(models.Model):
    barcode = models.IntegerField(primary_key=True)
    package_type = models.CharField(max_length=150)
    value = models.IntegerField(blank=True, null=True) 
    appropriate_zones = models.CharField(max_length=150)

    class Meta:
        db_table = 'valuables_data'


class Worker(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    jobs_job_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    passport_number = models.IntegerField()
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'worker'
