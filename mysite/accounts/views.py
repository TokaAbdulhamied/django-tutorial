from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup_view (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})
