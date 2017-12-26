# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from json import JSONEncoder
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import jdatetime
import datetime
from .models import *
from django.utils import timezone
import xlwt
from django.http import HttpResponse


from django.shortcuts import render

# Create your views here
def index(request):
    context={}
    return render(request,'index.html' , context)


def setvalue(x):
    if x =='عالی' :
        return 5
    elif x=='خوب' :
        return 4
    elif x== 'متوسط' :
        return  3
    elif x=='ضعیف' :
        return 2
    else :
        return 1

@csrf_exempt
def answer(request):
    QoProduct = 'کیفیت محصول در مقایسه با سایر محصولات مشابه'
    QoDesign = 'میزان رضایت از طراحی و کیفیت بسته بندی محصولات'
    QoResponse = 'میزان رضایت از پاسخگویی و رسیدگی به نظرات و پیشنهادات و شکایات'
    QoDelivery ='میزان رضایت از تحویل محصولات در زمان موردنظر'
    QoPersonality = 'میزان رضایت از نخوه برخورد پرسنل'
    QoDecor ='میزان رضایت از وضعیت ظاهری محیط'
    QoAmount = 'میزان رضایت از قیمت محصول در مقایسه با سایر محصولات مشابه'
    QoShape = 'میزان رضایت ازوضعیت ظاهری محصولات'
    Comment = 'لطفا نظرات و پیشنهادات تکمیلی خود را در راه ارتقا کیفیت محصولات ارائه نمایید'
    sex = 'M'
    age = 'None'

    iQoProduct = 0
    iQoDesign = 0
    iQoResponse = 0
    iQoDelivery = 0
    iQoPersonality = 0
    iQoDecor = 0
    iQoAmount = 0
    iQoShape = 0

    if 'sex' in request.POST :
        if request.POST['sex']== 'زن' :
            sex = 'F'

    if 'age' in request.POST :
        age = request.POST['age']

    string_data = request.POST['data']
    data = json.loads(string_data)

    if QoProduct in data :
        QoProduct = data[QoProduct]
        iQoProduct = setvalue(QoProduct)


    if QoDesign in data :
        QoDesign = data[QoDesign]
        iQoDesign = setvalue(QoDesign)

    if QoResponse in data :
        QoResponse = data[QoResponse]
        iQoResponse = setvalue(QoResponse)

    if QoDelivery in data :
        QoDelivery = data[QoDelivery]
        iQoDelivery = setvalue(QoDelivery)

    if QoPersonality in data :
        QoPersonality = data[QoPersonality]
        iQoPersonality = setvalue(QoPersonality)

    if QoDecor in data :
        QoDecor = data[QoDecor]
        iQoDecor = setvalue(QoDecor)

    if QoAmount in data :
        QoAmount = data[QoAmount]
        iQoAmount = setvalue(QoAmount)

    if QoShape in data :
        QoShape = data[QoShape]
        iQoShape = setvalue(QoShape)

    if Comment in data :
        Comment = data[Comment]

    ans = Answer(Date=jdatetime.date.today() , Time =timezone.now() , QoShape=iQoShape, QoAmount=iQoAmount, QoDecor=iQoDecor, QoPersonality=iQoPersonality, QoProduct=iQoProduct
                 , QoDelivery=iQoDelivery, QoResponse=iQoResponse, QoDesign=iQoDesign, Comment=Comment, Sex=sex, Age=age)
    ans.save()
    context = {}
    context['status'] = 'ok'
    return JsonResponse(context, encoder=JSONEncoder)


def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="survey.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Answers')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [ 'Year' , 'Month' , 'Day' , 'Time', 'Sex', 'Age' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    anses = Answer.objects.all()
    rows = []
    temp = []
    for ans in anses:
        temp = []
        year = ans.Date.year
        month = jdatetime.date.j_months_fa[ ans.Date.month - 1 ]
        day = ans.Date.day
        temp.append(year)
        temp.append(month)
        temp.append(day)

        time = datetime.time.strftime(ans.Time , "%H:%M")

        temp.append(time)
        temp.append(ans.Sex)
        temp.append(ans.Age)
        rows.append(temp)


    #rows = Answer.objects.all().values_list('Time', 'Sex', 'Age')
    #print(rows)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response