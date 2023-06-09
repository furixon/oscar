from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.


def index(request):
    template = 'oscar/index.html'
    context = {}
    return render(request, template, context)


def detox_capsule(request):
    template = 'oscar/detox_capsule.html'
    context = {}
    return render(request, template, context)


def detox_mimi(request):
    template = 'oscar/detox_mimi.html'
    context = {}
    return render(request, template, context)


def policy_personal(request):
    template = 'oscar/policy_personal.html'
    context = {}
    return render(request, template, context)


def policy_agree(request):
    template = 'oscar/policy_agree.html'
    context = {}
    return render(request, template, context)


def introduce(request):
    template = 'oscar/introduce.html'
    context = {}
    return render(request, template, context)


def lohacell_system(request):
    template = 'oscar/lohacell_system.html'
    context = {}
    return render(request, template, context)


def research(request):
    template = 'oscar/research.html'
    context = {}
    return render(request, template, context)


def medicine(request):
    template = 'oscar/medicine.html'
    context = {}
    return render(request, template, context)


def notice(request):
    notices = Notice.objects.all().order_by('-reg_date')
    paginator = Paginator(notices, 2)
    page = request.GET.get('page')
    notices_page = paginator.get_page(page)
    template = 'oscar/notice.html'
    context = {'notices': notices_page}
    return render(request, template, context)


def payment(request):
    template = 'oscar/payment.html'
    context = {}
    return render(request, template, context)


def basicprocessor(request):
    template = 'oscar/basicprocessor.html'
    context = {}
    return render(request, template, context)