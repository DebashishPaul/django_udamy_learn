from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView
# Create your views here.
# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list
#     }
#     return HttpResponse(template.render(context, request))

#functinal views
def index(request):
    item_list = Item.objects.all()
    context ={
        'item_list' : item_list
    }
    return render(request, 'food/index.html', context)

#class based views
class IndexClassViews(ListView):
    model = Item;
    template_name='food/index.html'
    context_object_name = 'item_list'

def menu(request):
    context = {
        'item_list' : item_list
    }
    return render(request, 'base.html', context)

def foodList(request):
    return HttpResponse('<h1>this is title of<br> food list</h1>')

#functional detail views
def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/details.html', context)

#class based details views
class DetailViewClass(DetailView):
    model = Item
    template_name='food/details.html'

#create item functional view
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-forms.html', {'form':form})

#create item class view
# class CreateClassItem(CreateView):
#     model : Item
#     fields : ['item_name', 'item_desc', 'item_price', 'item_image']
#     template_name = "food/item-forms.html"
    

#     def form_valid(self, form):
#         form.instance.user_name = self.request.user

#         return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-forms.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})
