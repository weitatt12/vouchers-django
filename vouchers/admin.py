from django.contrib import admin
from .models import Voucher

class VoucherAdmin(admin.ModelAdmin):
    form_display = ['form', 'valid_from', 'valid_to', 'discount', 'active']
    form_filter = ['active', 'valid_from', 'valid_to']
    form_search = ['form']

admin.site.register(Voucher, VoucherAdmin)
