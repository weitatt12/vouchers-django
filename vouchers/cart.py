from decimal import Decimal
from django.conf import settings
from vouchers.models import Voucher

class Cart(object):
    def __init__(self):
        self.voucher_id = self.sessions.get('voucher_id')

    def total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        @property
        def voucher(self):
            if self.voucher_id:
                # if self.voucher_id > 4: if voucher is being used up to 3 then is not valid
                #     return 'Voucher is not valid'
                return Voucher.objects.get(id=self.voucher_id)
            return None

    def get_discount(self):
        if self.voucher:
            return (seld.voucher.discount / Decimal('100')) * self.total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.total_price() - self.get_discount()
