from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth import login, logout, update_session_auth_hash
from itertools import chain
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sendCart(request):
    if request.method == 'POST':
        data_dict = json.loads(request.body)
        print(data_dict)
        return JsonResponse({"success": "Done"})
    else:
        return JsonResponse({"error": "Rong"})


def index(request):
    slats = Slats.objects.filter(
        available=True, category__name='Ордена России')[:6]

    context = {
        'slats': slats,
    }
    return render(request, 'plankiHomePage/index.html', context=context)


def contacts(request):
    return render(request, 'plankiHomePage/contacts.html')


def privacy(request):
    return render(request, 'plankiHomePage/privacy.html')


def terms(request):
    return render(request, 'plankiHomePage/terms.html')


@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Отправлено!')
        else:
            messages.error(request, 'Не отправлено')
    else:
        form = FeedbackForm()

    context = {
        'form': form,
    }
    return render(request, 'plankiHomePage/feedback.html', context=context)


# Authorization
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('plankiHomePage:index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'plankiHomePage/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы вошли!')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('plankiHomePage:index')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'plankiHomePage/login.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('plankiHomePage:login')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль был успешно изменён')
            redirect('plankiHomePage:settings')
        else:
            messages.error(request, 'Исправьте ошибки ниже')
    else:
        form = CustomPasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'plankiHomePage/change_password.html', context=context)


# Settings
@login_required
def settings(request):
    if request.method == 'POST':
        form = CustomSettingsUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные изменены!')
            return redirect('plankiHomePage:settings')
    else:
        form = CustomSettingsUserForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'plankiHomePage/profile_settings.html', context=context)


# Search
def search(request):
    q = request.GET.get('q')

    if q == None:
        q = 'Орден'
    elif q == "":
        q = 'Орден'
    slats = Slats.objects.filter(Q(name__icontains=q) | Q(
        description__icontains=q), Q(available=True))

    # products = sorted(chain(slats, sashes, jettons),
    #                   key=lambda instance: instance.name)

    products = slats
    paginator = Paginator(products, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'q': q,
        'page_obj': page_obj
    }
    return render(request, 'plankiHomePage/search.html', context=context)


# Products
def slats(request, slug_id):
    categories = CategorySlats.objects.annotate(cnt=Count('slats', filter=F('slats__available'))).filter(
        cnt__gt=0).order_by('time_create')
    products = Slats.objects.filter(
        category__slug=slug_id, available=True).order_by('-time_create')
    current_category = CategorySlats.objects.get(slug=slug_id).name
    paginator = Paginator(products, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'titleForCatalogue': 'Каталог Орденских Планок',
        'categories': categories,
        'page_obj': page_obj,
        'current_category': current_category,
    }
    return render(request, 'plankiHomePage/products.html', context=context)


def sashes(request):
    products = Sashes.objects.filter(available=True).order_by('-time_create')
    paginator = Paginator(products, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'titleForCatalogue': 'Ленты',
        'page_obj': page_obj,
    }
    return render(request, 'plankiHomePage/products.html', context=context)


def jettons(request):
    products = Jettons.objects.filter(available=True).order_by('-time_create')
    paginator = Paginator(products, 15)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'titleForCatalogue': 'Жетонны',
        'page_obj': page_obj
    }
    return render(request, 'plankiHomePage/products.html', context=context)


# Detail
def detail_slats(request, slug_id):
    product = get_object_or_404(Slats, slug=slug_id, available=True)

    context = {
        'product': product,
    }
    return render(request, 'plankiHomePage/detail.html', context=context)


def detail_sashes(request, slug_id):
    product = get_object_or_404(Sashes, slug=slug_id, available=True)

    context = {
        'product': product
    }
    return render(request, 'plankiHomePage/detail.html', context=context)


def detail_jettons(request, slug_id):
    product = get_object_or_404(Jettons, slug=slug_id, available=True)

    context = {
        'product': product
    }
    return render(request, 'plankiHomePage/detail.html', context=context)


# Cart
def cart(request):
    cart = None

    context = {
        'cart': cart,
    }
    return render(request, 'plankiHomePage/cart.html', context=context)
