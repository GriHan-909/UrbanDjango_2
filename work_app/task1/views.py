from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

# Create your views here.
def sign_up_by_django(request):
    users = [buyer.name for buyer in Buyer.objects.all()]
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {}
            context = {'info': info, 'form': form}
            if password==repeat_password and age > 18 and username not in users:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request,'registration_page.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = [buyer.name for buyer in Buyer.objects.all()]
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password==repeat_password and int(age) > 18 and username not in users:
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context)


    else:
        return render(request, 'registration_page.html')


def func_basket(request):
    title = 'Корзина'
    context = {
        'title': title,
        'list_mark': ['BMW', 'CHANGAN', 'MERSEDES', 'AUDI', 'VOLVO', 'ZEEKR', 'LOTUS']
    }

    return render(request, 'basket.html', context)

def func_store(request):
    title = 'Игры'
    Games = Game.objects.all()
    context = {
        'title': title,
        'Games': Games
    }

    return render(request, 'store.html', context)
