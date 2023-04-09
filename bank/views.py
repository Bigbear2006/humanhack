from django.urls import reverse_lazy
from django.shortcuts import redirect
import django.views.generic as gnr
from .models import TrainingWay, Test, Answer, TestResult, Form, User
from utils import get_ip


class HomePageView(gnr.ListView):
    model = TrainingWay
    template_name = 'index.html'
    context_object_name = 'train_ways'


class TestDetailView(gnr.DetailView):
    model = Test
    template_name = 'ios.html'
    context_object_name = 'test'

    def post(self, request, *args, **kwargs):
        questions = self.get_object().questions.all()
        if any(request.POST[f'question{q.id}'].strip().lower() in ['', ' ', None] for q in questions):
            return redirect(reverse_lazy('home'))  # if input is empty
        test = TestResult.objects.create()
        ip = get_ip(request)
        user, is_create = User.objects.get_or_create(ip=ip)
        user.test = test
        user.save()
        for q in questions:
            text = request.POST[f'question{q.id}'].strip().lower()
            right = q.variants.filter(is_right=True)[0].variant
            if text == right:
                is_right = True
            else:
                is_right = False
            Answer.objects.create(question=q, test=test, text=text, is_right=is_right)
        return redirect(reverse_lazy('home'))  # if input is valid


class TrainingWayDetailView(gnr.DetailView):
    model = TrainingWay
    template_name = 'train_way_detail.html'
    context_object_name = 'train_way'


class TestListView(gnr.ListView):
    model = Test
    template_name = 'tests.html'
    context_object_name = 'tests'


class FormCreateView(gnr.CreateView):
    model = Form
    template_name = 'form1.html'
    fields = ('user', 'training_way', 'name', 'surname', 'patronymic', 'birthday',
              'birthday_place', 'number', 'email', 'start_practice', 'end_practice')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        ip = get_ip(self.request)
        user, is_created = User.objects.get_or_create(ip=ip)
        form.instance.user = user
        return super().form_valid(form)
