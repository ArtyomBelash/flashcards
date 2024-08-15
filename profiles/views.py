from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.views import generic
from .forms import ProfileForm


class CreateProfileView(generic.CreateView):
    form_class = ProfileForm
    model = User
    success_url = '/'
    template_name = 'profiles/create_user.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class CustomLogoutView(generic.View):

    def get(self, request):
        if self.request.user.is_authenticated:
            logout(request)
            return redirect('card-list')
