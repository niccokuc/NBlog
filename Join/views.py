from django.shortcuts import render
from .forms import JoinForm
from .models import Join

# how the page is viewed
def JoinView(request):
    form = JoinForm(request.POST or None)

    if form.is_valid():
        print("THANKS")
        new_join = form.save(commit=False)
        email = form.cleaned_data['varEmail']
        name = form.cleaned_data['varName']
        user = form.cleaned_data['varUser']
        print(email)
        new_join_old, created = Join.objects.get_or_create(varEmail=email, varName=name, varUser=user)
    return render(request, 'signup.html', {'form': form})

