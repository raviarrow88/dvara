import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, SubCategory
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
