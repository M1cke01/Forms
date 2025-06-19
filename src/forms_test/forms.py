from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

MY_CHOICES = [
    ("db-value1", "Opción 1"),
    ("o2", "Opción 2"),
    ("o3", "Opción 3"),
]

YEARS = [x for x in range(1900, 2030)]

class ProductModelForm(forms.ModelForm):
    labels = {
        "title":"Mi etiqueta para el titulo",
        "slug":"Mi etiqueta para el slug",
        "price":"Mi etiqueta para el precio",
    }

    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "price"
        ]
        exclude = []

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) <= 10:
            raise forms.ValidationError("El texto debe contener más de 10 caracteres")
        return title
    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get("slug")
        if "misupermarca" not in slug:
            raise forms.ValidationError("El slug debe tener 'misupermarca'")
        return slug

class TestForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label="Ingresa un texto", widget=forms.Textarea(attrs={"rows":4, "cols":20}))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=80)
    float = forms.FloatField()
    email = forms.EmailField()
    opciones = forms.CharField(label="Selecciona 1 opción", widget=forms.Select(choices=MY_CHOICES))
    opciones_radio = forms.CharField(label="Selecciona 1 opción", widget=forms.RadioSelect(choices=MY_CHOICES))
    opciones_checkbox = forms.CharField(label="Selecciona 1 opción", widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))


#     def clean_integer(self, *args, **kwargs):
#         integer = self.cleaned_data.get("integer")
#         if integer >= 100:
#             raise forms.ValidationError("El número debe ser menor o igual a 100")
#         return integer
    
#     def clean_some_text(self, *args, **kwargs):
#         some_text = self.cleaned_data.get("some_text")
#         if len(some_text) < 10:
#             raise forms.ValidationError("El texto debe contener más de 10 caracteres")
#         return some_text