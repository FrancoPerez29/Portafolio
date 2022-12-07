from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def Contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method == 'POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            Nombre=request.POST.get("Nombre")
            Email=request.POST.get("Email")
            Asunto=request.POST.get("Asunto")
            Mensaje=request.POST.get("Mensaje")
            
            Email=EmailMessage("Mensaje desde pagina Web",
            "El usuario con Nombre {} con la direccion de correo {} y asunto {} , escribe lo siguiente:\n\n {} ".format(Nombre,Email,Asunto,Mensaje),
            "",["hakunamatatahogar.ok@gmail.com"],reply_to=[Email])
            
            try:
                Email.send()
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
            
    
    return render(request,"contactoapp/contacto.html", {'miFormulario':formulario_contacto})