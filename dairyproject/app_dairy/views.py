from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from model import m_dairy
from .models import *
from app_dairy import utils

def api_csss(request):
    #try:
    if 1:
        print('ok')
        return JsonResponse('Hello World',safe=False)
    # except:
    #     return JsonResponse({'result':False, 'info':'wrong'},safe=False)
    return JsonResponse({'result':False, 'info':'wrong'},safe=False)

def api_getdairy(request):
    if 1:
        if request.POST:
            #获取用户填入数据
            data = request.POST.dict()
            print(data)
            page = int(data['page'])
            num  = min(int(data['num']) ,30)
            group_id = data['group_id']
            info = m_dairy.get_dairy_list(page,num,group_id)

            return JsonResponse({'result':True, 'info':info},safe=False)
        return JsonResponse({'result':False, 'info':'wrong'},safe=False)
    
def api_create_dairy(request):
    if 1:
        if request.POST:
            data = request.POST.dict()
            #print(data)
            title = data['title']
            data['pickdate'] = utils.toshanghai(data['pickdate'])
            pickdate  = data['pickdate'][:data['pickdate'].find(' ')]
            content = data['content']
            the_datatime = utils.get_time()

            #存储数据库数据
            data_dict1 = {
                "date"     : the_datatime,      #生成时间
                "user_id"  : "lqjyyds",         #用户id
                "pickdate" : pickdate,          #用户填写的时间
                "title"    : title,             #标题
            }

            listinfo=db_DairyList.objects.create(**data_dict1)
            listinfo.save()

            contentinfo=db_DairyContent(DairyDetail=listinfo,content=content)
            contentinfo.save()
            
            return JsonResponse({'result':True, 'info':''},safe=False)
        
        return JsonResponse({'result':False, 'info':'NOT PSOT'},safe=False)  
    
def api_get_dairy(request):
    if 1:
        if request.POST:
            #获取用户填入数据
            data = request.POST.dict()
            print(data)
            id = data["id"]
            info = m_dairy.get_dairydetail(id)
            return JsonResponse({'result':True, 'info':info},safe=False)
        return JsonResponse({'result':False, 'info':'wrong'},safe=False)