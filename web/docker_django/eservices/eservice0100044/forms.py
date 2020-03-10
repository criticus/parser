from django import forms
from document.models import EServiceMeta
from document_66666666666.models import Document_66666666666

from document.models import GeoCity


class DocumentForm66666666666(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm66666666666, self).__init__(*args, **kwargs)

    comment = forms.TextInput()
    deadline = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': "form-control datepicker",

                                                                             'placeholder': "Введіть кінечну дату вхідного послуги у форматі день/місяць/рік"}))

    type_license = forms.ModelChoiceField(empty_label='Оберіть тип ліцензії', label="Тип ліцензії*:",
                                          queryset=EServiceMeta.objects.get(category_index="1.0").get_children(),
                                          required=True, widget=forms.Select(
            attrs={'class': 'form-control select_e_driver ', }))

    payment = forms.ModelChoiceField(empty_label='Оберіть тип оплати', label="Оплата*:",
                                     queryset=EServiceMeta.objects.get(category_index="2.0").get_children(),
                                     required=True, widget=forms.Select(
            attrs={'class': 'form-control select_e_driver ', }))

    region = forms.ModelChoiceField(empty_label='Оберіть область', label="Область*:",
                                    queryset=GeoCity.objects.filter(parent=None),
                                    required=True, widget=forms.Select(
            attrs={'class': 'form-control select_e_driver ', }))

    city = forms.CharField(label="Місто*:", initial="Оберіть місто", required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control width_100', 'disabled': 'disabled'}))

    file = forms.FileField(required=True, widget=forms.FileInput(attrs={'multiple': "true"}))