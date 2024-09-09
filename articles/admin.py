from django.contrib import admin
from .models import *
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'phone_number')
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'operation_type', 'clients_client_id', 'valuables_data_barcode','product_amount', 'expected_completion_date')
class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ('op_journal_operation_id', 'worker_worker_id', 'address', 'pending_delivery_date')
class FinancesAdmin(admin.ModelAdmin):
    list_display = ('finance_op_id', 'payment', 'contracts_contract_id', 'transaction_completion')
class OperationsAdmin(admin.ModelAdmin):
    list_display = ('operation_id', 'operation_type', 'contracts_contract_id', 'valuables_data_barcode', 'clients_client_id', 'worker_worker_id', 'operation_date', 'amount')
class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'payment', 'planned_work_time')
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'name', 'amount', 'zone_type', 'zone_number')
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'name', 'phone_number')
class ValuablesAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'package_type', 'value','appropriate_zones')
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_id', 'name', 'jobs_job_name', 'date_of_birth', 'passport_number', 'phone_number')
admin.site.register(clients, ClientAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contracts, ContractAdmin)
admin.site.register(Deliveries, DeliveriesAdmin)
admin.site.register(Finances, FinancesAdmin)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(OperationsJournal, OperationsAdmin)
admin.site.register(Registry, RegistryAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(ValuablesData, ValuablesAdmin)
admin.site.register(Worker, WorkerAdmin)
