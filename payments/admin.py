from django.contrib import admin

from payments.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "user", "remote_id", "amount", "status")
    list_display_links = ("id", "order")
