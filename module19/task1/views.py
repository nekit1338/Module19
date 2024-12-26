from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import *

#  data = {
#      'games': [
#          game.title for game in Game.objects.all()
#      ],
#      'descriptions': [
#          game.description for game in Game.objects.all()
#      ],
#      'costs': [
#          game.cost for game in Game.objects.all()
#      ],
#  }

data = {
        'games': Game.objects.all()
    }


def show_platform(request):
    return render(request, 'platform.html')


def show_shop(request):
    return render(request, 'shop.html', data)


def show_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})


def add_to_cart(request):
    if request.method == 'POST':
        try:
            game_name = request.POST.get('game')
            try:
                game = Game.objects.get(title=game_name)
                cart = request.session.get('cart', {})
                cart[game.title] = cart.get(game.title, 0) + 1
                request.session['cart'] = cart
                return redirect('cart')
            except Game.DoesNotExist:
                return HttpResponse("Игра не найдена")
        except (ValueError, TypeError):
            return HttpResponse("Некорректный запрос")
    return HttpResponse("Неверный метод запроса")


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    return redirect('cart')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            Buyer.objects.create(name=username, balance=1000, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if len(username) > 30:
            errors.append('Имя пользователя не должно превышать 30 символов')
        if Buyer.objects.filter(name=username).exists():
            errors.append('Пользователь уже существует')
        if password != repeat_password:
            errors.append('Пароли не совпадают')
        if not age.isdigit() or int(age) < 18:
            errors.append('Вам меньше 18 лет')
        if len(age) > 3:
            errors.append('Возраст не может содержать более 3 цифр')
        if int(age) > 120:
            errors.append('Возраст не может быть больше 120')
        if len(password) < 8:
            errors.append('Пароль должен быть не менее 8 символов')
        if errors:
            info['errors'] = errors
            info['username'] = username
            info['password'] = password
            info['repeat_password'] = repeat_password
            info['age'] = age
        else:
            Buyer.objects.create(name=username, balance=1000, age=age)
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', {'info': info})
