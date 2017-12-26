from controlcenter import Dashboard, widgets
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from .models import Answer

class ModelItemList(widgets.ItemList):
    model = Answer
    list_display = ('id' , 'Date', 'Time' , 'Age' , 'Sex' , 'QoProduct' , 'QoDesign' , 'QoShape' , 'QoResponse' , 'QoDelivery' ,
                    'QoPersonality' , 'QoDecor' , 'QoAmount' , 'Comment' )
    list_display_links = ('id')
    sortable = True
    title = 'لیست همه ی نظرات'
    limit_to = 200
    changelist_url = '/export'
    width = widgets.FULL



class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )