from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .service import GenerateShortURL
from .forms import UserLoginForm, UserRegisterForms
from .models import URLModels


def register_view(request):
    form = UserRegisterForms()

    if request.method == "POST":
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
        else:
            messages.error(request, 'Unsuccessful registered. The entered data is incorrect.')

    context = {
        'form': form,
    }
    return render(request, 'urlshortener/register.html', context)


def login_view(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shortener')
            else:
                messages.error(request, 'The entered data is incorrect.')

    context = {
        'form': form,
    }
    return render(request, 'urlshortener/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def shortener_view(request):
    if request.method == "POST":
        req_url = request.POST['origin_url']
        user = request.user

        if not URLModels.objects.filter(Q(origin_url=req_url) & Q(user=user)):
            url = URLModels(origin_url=req_url, short_id=GenerateShortURL.generate_id(), user=user)
            url.save()

        obj = URLModels.objects.get(Q(origin_url=req_url) & Q(user=user))
        host_url = request.get_host()
        messages.success(request, 'Take your short link:')

        context = {
            'obj': obj,
            'host_url': host_url,
        }
        return render(request, 'urlshortener/shortener.html', context)
    return render(request, 'urlshortener/shortener.html')


@login_required
def redirect_to_origin_url_view(request, pk):
    obj = get_object_or_404(URLModels, pk=pk)
    return redirect(obj.origin_url)


@login_required
def links_list_view(request):
    qs_links = URLModels.objects.all().order_by('-pub_date').filter(user=request.user)
    host_url = request.get_host()

    context = {
        'links': qs_links,
        'host_url': host_url,
    }
    return render(request, 'urlshortener/links_list.html', context)
