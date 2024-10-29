from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #사용자 인증
            login(request, user) # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form}) 

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})

def page_not_found500(request):
    try:
        return render(request, 'common/500.html', status=500)
    except Exception as e:
        print(f"Error rendering 500 page: {e}")  # 로그에 출력
        return HttpResponse("Internal Server Error", status=500)

# Create your views here.
