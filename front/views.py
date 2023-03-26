from django.shortcuts import render

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