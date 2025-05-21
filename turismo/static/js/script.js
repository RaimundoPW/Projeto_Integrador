// def inicioSite(request):
//     pacotes = PacoteTuristico.objects.all()

//     if request.method == 'POST':
//         nome = request.POST.get('nome')
//         email = request.POST.get('email')
//         mensagem = request.POST.get('mensagem')

//         if nome and email and mensagem:
           
//             messages.success(request, 'Mensagem enviada com sucesso! Em breve retornaremos seu contato.')
//         else:
//             messages.error(request, 'Por favor, preencha todos os campos.')

//     return render(request, 'turismo/index.html', {'pacotes': pacotes})