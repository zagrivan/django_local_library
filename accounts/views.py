# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponseRedirect


# class SignUpView(generic.CreateView):
#     form_class = UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
#     # initial = {'groups': Group.objects.get(id=1)}


def SignUpView(request):
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name='Library Members'))

            return HttpResponseRedirect(reverse('login') )

    else:
        form = UserCreateForm()

    return render(request, 'signup.html', {'form': form })