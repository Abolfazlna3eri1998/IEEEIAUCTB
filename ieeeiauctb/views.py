from django.contrib.auth import authenticate, login
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from ieeeiauctb.forms import SignUpForm


#def index(request):
 #   return render(request, "base.html", {})
#def homepage(request):
 #   return render(request,"index.html")
#def register(request):
#    return render(request,"registerform.html")
#def contactus(request):
 #   return render(request,"tamasbama.html")
#def signup(request):
  #  if request.method == 'POST':
   #     form = SignUpForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      username = form.cleaned_data.get('username')
       #     raw_password = form.cleaned_data.get('password1')
        #    user = authenticate(username=username, password=raw_password)
         #   login(request, user)
          #  return redirect('home')
    #else:
     #   form = SignUpForm()
    #return render(request, 'registerform.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registerform.html', {'form': form})
