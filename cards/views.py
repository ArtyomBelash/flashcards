from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import CardCheckForm
from .models import Card
import random


class CardListView(generic.ListView):
    model = Card
    template_name = 'cards/cards_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Card.objects.filter(owner=self.request.user).order_by('box', '-date_created')
            return queryset


class CardCreateView(generic.CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = 'cards/create_card.html'
    success_url = reverse_lazy("card-create")

    def form_valid(self, form):
        card = form.save(commit=False)
        card.owner = self.request.user
        card.save()
        return super().form_valid(form)


class CardUpdateView(CardCreateView, generic.UpdateView):
    success_url = reverse_lazy("card-list")


class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm
    context_object_name = 'boxes'

    def get_queryset(self):
        owner = self.request.user
        return Card.objects.filter(box=self.kwargs["box_num"], owner=owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))
