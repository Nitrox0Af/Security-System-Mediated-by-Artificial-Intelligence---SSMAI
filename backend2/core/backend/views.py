from django.http import JsonResponse
from backend.models import Quest

def receber_strings(request):
    if request.method == 'POST':
        str_1 = request.POST.get('str_1')
        str_2 = request.POST.get('str_2')
        str_3 = request.POST.get('str_3')
        str_4 = request.POST.get('str_4')
        str_5 = request.POST.get('str_5')

        minha_string = Quest(str_1=str_1, str_2=str_2, str_3=str_3, str_4=str_4, str_5=str_5)
        minha_string.save()

        return JsonResponse({'message': 'Strings armazenadas com sucesso!'})

    return JsonResponse({'message': 'Método inválido.'})