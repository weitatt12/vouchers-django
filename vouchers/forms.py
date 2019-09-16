from django import forms


class VoucherApplyForm(forms.Form):
    apply_form = forms.CharField()