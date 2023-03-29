from django import forms
from trash.models import EWaste, RWaste, HWaste, LSWaste


class OrderEwasteForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = EWaste
        fields = ["type", "height", "width", "length", "weight", "client"]


class OrderRwasteForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = RWaste
        fields = ["type", "trash_amount", "client"]


class OrderHwasteForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = HWaste
        fields = ["type", "trash_amount", "client"]


class OrderLswasteForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.HiddenInput(), required=False, queryset=None
    )

    class Meta:
        model = LSWaste
        fields = ["type", "height", "width", "length", "weight", "client"]
