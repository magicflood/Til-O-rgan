from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Card
from .forms import CardForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForm
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = 'HomePage/index.html'

class AboutView(TemplateView):
    template_name = 'About/index.html'

def lessons_list(request):
    lessons = Card.objects.all()
    data = {
        'lessons': lessons,
    }
    return render(request, 'Learn/index.html', context=data)

def card_detail(request, pk):
    card = Card.objects.filter(id=pk).first()
    data = {
        'card': card
    }
    return render(request, 'Detail/detail.html', context=data)



def admin_login_page(request):
    return render(request, 'Admin/admin_login.html')

def check_admin_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == '1111':
            request.session['is_admin'] = True 
            return redirect('adminka')
        else:
            return render(request, 'Admin/admin_login.html', {'error': 'Неверный пароль!'})
    return redirect('admin_login')

def adminka(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    cards = Card.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminka')
    else:
        form = CardForm()

    user_count = users.count()

    return render(request, 'Admin/adminka.html', {
        'cards': cards,
        'form': form,
        'user_count': user_count,
        'users': users
    })

def delete_card(request, pk):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('adminka')

def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        user.delete()
    return redirect('adminka')