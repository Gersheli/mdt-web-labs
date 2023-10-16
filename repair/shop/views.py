import requests
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import CartAddUslugaForm
from .forms import UslugaForm, ReviewForm
from .models import Usluga, Genre, Author, Post, Review


def usluga_list(request, usluga_genre_name=None):
    genre = None
    genres = Genre.objects.all()
    uslugas = Usluga.objects.all()
    sort_t = request.GET.get('sort')

    if (usluga_genre_name):
        genre_ = get_object_or_404(Genre, name=usluga_genre_name)
        uslugas = uslugas.filter(genre=genre_)

    if (str(sort_t) == 'ascending'):
        uslugas = uslugas.order_by('cost')
    elif (str(sort_t) == 'descending'):
        uslugas = uslugas.order_by('-cost')
    elif (str(sort_t) == 'ascendingcount'):
        uslugas = uslugas.order_by('purchase_count')
    elif (str(sort_t) == 'descendingcount'):
        uslugas = uslugas.order_by('-purchase_count')
    return render(request,
                  'shop/usluga/list.html',
                  {'genre': genre, 'genres': genres, 'uslugas': uslugas})


def usluga_detail(request, id):
    usluga = get_object_or_404(Usluga, id=id)
    cart_usluga_form = CartAddUslugaForm()

    joke = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]

    return render(request,
                  'shop/usluga/detail.html',
                  {'usluga': usluga, 'cart_usluga_form': cart_usluga_form,
                   'joke': joke['setup'] + joke['punchline']})


def usluga_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")

    print(1234567)

    form = UslugaForm()

    if request.method == "POST":
        usluga = Usluga.objects.create(title=request.POST.get('title'),
                                       author=Author.objects.get(id=request.POST.get('author')),
                                       cost=request.POST.get('cost'),
                                       genre=Genre.objects.get(id=request.POST.get('genre')),
                                       quantity=0,
                                       description=request.POST.get('description'),
                                       image=request.POST.get('image'))

        usluga.save()
    else:
        return render(request, "shop/usluga/create.html", {"form": form})
    return HttpResponseRedirect("/")


# изменение данных в бд
def usluga_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")

    try:
        usluga = Usluga.objects.get(id=id)

        form = UslugaForm(initial={'title': usluga.title, 'author': usluga.author,
                                   'cost': usluga.cost, 'genre': usluga.genre,
                                   'description': usluga.description, 'image': usluga.image})

        if request.method == "POST":
            usluga.title = request.POST.get('title')
            print(request.POST.get('title'))
            usluga.author = Author.objects.get(id=request.POST.get('author'))
            usluga.cost = request.POST.get('cost')
            usluga.genre = Genre.objects.get(id=request.POST.get('genre'))
            usluga.quantity = 0
            usluga.description = request.POST.get('description')
            usluga.image = request.FILES.get('image')
            usluga.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "shop/usluga/edit.html", {"usluga": usluga, 'form': form})
    except usluga.DoesNotExist:
        return HttpResponseNotFound("<h2>usluga not found</h2>")


# удаление данных из бд
def usluga_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")

    try:
        usluga = Usluga.objects.get(id=id)
        usluga.delete()
        return HttpResponseRedirect("/")
    except usluga.DoesNotExist:
        return HttpResponseNotFound("<h2>usluga not found</h2>")


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('shop/reviews.html')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    current_user = request.user
    return render(request, 'shop/reviews.html', {'form': form, 'reviews': reviews, 'current_user': current_user})


def news(request):
    lst = Post.objects.all()
    return render(request, 'shop/news.html', context={'news_list': lst})


def about(request):
    return render(request, 'shop/about.html')


def policy(request):
    return render(request, 'shop/policy.html')


def vacancies(request):
    return render(request, 'shop/vacancies.html')


def coupons(request):
    return render(request, 'shop/coupons.html')


def faq(request):
    return render(request, 'shop/faq.html')
