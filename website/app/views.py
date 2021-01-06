import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Category, SubCategory,Order
from django.urls import reverse
import json
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    """
    This function renders the home page
    """
    context = {}
    return render(request, "base.html", context)


def upload_data(request):
    """
    This function uploads the data from excel
    """
    try:
        if request.POST and request.FILES:
            file = request.FILES.get('file')
            print(file)
            sh1 = pd.read_excel(file, sheet_name='category')
            sh2 = pd.read_excel(file, sheet_name='subcategory')

            sh1_list = sh1.values.tolist()

            for cat in sh1_list:
                category, created = Category.objects.get_or_create(
                    cat_id=cat[0], name=cat[1])
                # category.save()

            sh2_list = sh2.values.tolist()

            for sc in sh2_list:
                sub_cat, created = SubCategory.objects.get_or_create(
                    name=sc[1],
                    category=Category.objects.get(cat_id=sc[0])
                )
            messages.success(request, 'Data Created SuccessFully.')

            return redirect(reverse('upload_data'))

        return render(request, 'upload_data.html', {})

    except Exception as e:
        messages.error(request, str(e))
        return redirect(reverse('upload_data'))






from django.views.generic import CreateView,FormView
from .forms import OrderForm
from django.urls import reverse_lazy

# Form class function to createOrder
class CreateItem(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')
    template_name = 'form.html'



# Api to filter the subcategories using category_id
def getSubCategory(request):
    id = request.GET['id']

    catgry = Category.objects.get(id=id)

    sub_catgs = catgry.subcategory_set.all()

    sub_catgs_list = []

    for s in sub_catgs:
        sub_catgs_list.append((str(s.id),s.name))

    data = {
    'sub_cats':sub_catgs_list
    }

    return JsonResponse(data)



def orderslist(request):
    orders = Order.objects.all()
    context = {'orders':orders}

    return render(request,'list.html',context)
