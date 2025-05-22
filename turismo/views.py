from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import PacoteTuristico, Contato
from django.contrib import messages


def inicioSite(request):
    pacotes = PacoteTuristico.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        if nome and email and mensagem:
            # Salvar no banco
            Contato.objects.create(
                nome=nome,
                email=email,
                mensagem=mensagem
            )

            # Enviar e-mail
            send_mail(
                subject=f'Nova mensagem de {nome}',
                message=f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
                from_email='seuemail@gmail.com',  # Coloque um e-mail válido configurado no Django
                recipient_list=['raimundodasilvasudario@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('pagina_de_sucesso')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'turismo/index.html', {'pacotes': pacotes})


def pagina_de_sucesso(request):
    return render(request, 'turismo/sucesso.html')