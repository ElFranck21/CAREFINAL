from django.shortcuts import render
from .forms import ContactoForm
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def contacto(request):
    data={
        'form':ContactoForm()

    }

    if request.method=='POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save
            data["mesaje"]="contacto guardado"
        else:
            data["form"]=formulario
    return render(request,'app/contacto.html', data)
def reportes(request):
    return render(request,'app/reportes.html')


