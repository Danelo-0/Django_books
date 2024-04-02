from django.shortcuts import render, redirect
import random
from django.db.models import Max
from .models import Book
from .models import Author
from .models import Profile, Language, Genre, Print
from .forms import BookForm, CustomForm, CustomAuthenticationForm, ProfileUpdate, CustomSetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def Index(request):
    check = Book.objects.all()
    if len(check) != 0:
        book = Book.objects.order_by('?').first()

        return render(request, "index.html", {"books": book, 'title': 'Рекомендуем прочитать'})

    else:
        return render(request, "index.html", {"books": None, 'title': 'Рекомендации отсутствуют'})


def AllBook(request):
    books = Book.objects.all()
    languages = Language.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    prints = Print.objects.all()

    if len(books) != 0:
        if request.method == "POST" and 'filter' in request.POST:
            if 'title' in request.POST and request.POST.get("title") != "":
                books = books.filter(title=request.POST.get("title"))
            if 'genre' in request.POST and request.POST.get("genre") != "1":
                books = books.filter(genre=request.POST.get("genre"))
            if 'publishing_house' in request.POST and request.POST.get("publishing_house") != "1":
                books = books.filter(publishing_house=request.POST.get("publishing_house"))
            if 'authors' in request.POST and request.POST.get("authors") != "1":
                books = books.filter(author=request.POST.get("authors"))
            if 'languages' in request.POST and request.POST.get("languages") != "1":
                books = books.filter(language=request.POST.get("languages"))

        return render(request, "allBoks.html", {"books": books, 'title': 'Все книги', "languages": languages,
                                                "authors": authors, "genres": genres, "prints": prints})
    else:
        return render(request, "allBoks.html", {"books": None, 'title': 'Книги отсутствуют'})


def AllAuthor(request):
    authors = Author.objects.all()
    if len(authors) != 0:
        return render(request, "allAuthor.html", {"authors": authors, 'title': 'Все авторы'})
    else:
        return render(request, "allAuthor.html", {"authors": None, 'title': 'Авторы отсутствуют'})


def OneBook(request, id):
    book = Book.objects.get(pk=id)
    languageList = book.language.all()
    authorList = book.author.all()

    authorField = ''
    languageField = ''

    for elem in authorList:
        authorField = authorField + elem.fio + '; '

    for elem in languageList:
        languageField = languageField + elem.language + '; '

    return render(request, "oneBook.html",
                  {"book": book, "title": "Подробнее о книге", "language": languageField, "author": authorField})


def OneAuthor(request, id):
    author = Author.objects.get(pk=id)
    return render(request, "oneAuthor.html", {"author": author})


def AddShow(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AllBook')
        else:
            error = 'Форма была не верной'

    form = BookForm()
    return render(request, "add.html", {'form': form})


def Delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('AllBook')


def RegisterUser(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = form.save()
            Profile.objects.create(user=user)
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return redirect('Index')
    else:
        form = CustomForm
    return render(request, "register.html", {'form': form})


def Login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Index')
    else:
        form = CustomAuthenticationForm
    return render(request, "login.html", {'form': form})


def Logout(request):
    logout(request)
    return redirect('Index')


def ProfileShow(request):
    user_profile = Profile.objects.get(user=request.user.id)
    return render(request, "profile.html", {"user_profile": user_profile})


def ProfileUpdateView(request):
    user_profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('Profile')
    else:
        form = ProfileUpdate(instance=user_profile)
    return render(request, "updateProfile.html", {"form": form})


def ProfileUpdatePassword(request):
    if request.method == 'POST':
        form = CustomSetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Profile')
    else:
        form = CustomSetPasswordForm(request.user)
    return render(request, "updatePassword.html", {"form": form})
