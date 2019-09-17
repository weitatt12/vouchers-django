from django.shortcuts import render
from django.utils import timezone
from .models import Voucher
from .forms import VoucherApplyForm



def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code, valid_form__lte=now, valid_to__gte=now, active=True)
            request.sessions['voucher.id'] = voucher.id
        except VoucherDoesNotExist:
            request.session['voucher.id'] = None
    return render(request, 'vouchers/voucher.html', {'form': form})
    

