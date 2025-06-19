from django.shortcuts import render, redirect
from .forms import ProductModelForm, TestForm
from .models import Product
from django.forms import formset_factory, modelformset_factory
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form':form})

def login_view(request):
    return render(request, 'login.html', {'user': request.user})

#from .forms import TestForm

# def home(request):
#     initial_data = {
#         "some_text":"Texto inicial",
#         "boolean": True,
#         #"integer":90,
#         "float":5.5,
#         "email":"test@gmail.com"
#     }
#     form = TestForm(request.POST or None, initial=initial_data)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request, "forms.html", {"form":form})
def home(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    return render(request, "forms.html", {"form":form})

# def home(request):
#     TestFormSet = formset_factory(TestForm, extra=3)
#     formset = TestFormSet(request.POST or None)
#     for form in formset:
#         print(form.data)
#     context = {
#         "formset":formset
#     }
#     return render(request, "formset_view.html", context)
# def home(request):
#     ProductModelFormSet = modelformset_factory(Product, form=ProductModelForm)
#     formset = ProductModelFormSet(request.POST or None, queryset=Product.objects.all())

#     print("formset.data")
#     print(formset.data)

#     print("formset.errors")
#     print(formset.errors)

#     formset.clean()
#     if formset.is_valid():
#         print("modelFormset es valido")
#         formset.save()
#     context = {
#         "formset":formset
#     }
#     return render(request, "formset_view.html", context)