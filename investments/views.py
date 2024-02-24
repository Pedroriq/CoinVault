from django.shortcuts import render, redirect, get_object_or_404

from investments.models import Investment
from investments.forms import InvestmentForm


def create_investment(request):
    context = {}

    # add the dictionary during initialization
    form = InvestmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list_investment")

    context['form'] = form
    return render(request, "investments/create.html", context)


def list_investment(request):
    context = {'dataset': Investment.objects.all()}

    return render(request, "investments/list.html", context=context)


def update_investment(request, pk):
    context = {}

    obj = get_object_or_404(Investment, id=pk)

    form = InvestmentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("list_investment")

    context["form"] = form
    return render(request, "investments/create.html", context)


def delete_investment(request, pk):
    obj = get_object_or_404(Investment, id=pk)
    obj.delete()
    return redirect("list_investment")
