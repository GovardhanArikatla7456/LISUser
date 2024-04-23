from django.shortcuts import render, redirect

# Create your views here.
from .forms import EntryForm
from .models import User
# view for entering the user data
def form_view(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = EntryForm()
    return render(request, 'userinput/form.html', {'form': form})
# view for displaying the user data
def confirmation_view(request):
    entries = User.objects.all()
    return render(request, 'userinput/confirmation.html', {'entries': entries})
