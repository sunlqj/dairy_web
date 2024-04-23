from app_dairy.models import *
from . import pagination

def get_dairy(querysets_list):
    results = []
    for one in querysets_list:#.object_list:
        the_one = one.__dict__
        del the_one['_state']
        results.append(the_one)
        print(the_one)
    return results

def get_dairy_list(page,num,group_id):       
    querysets_list = db_DairyList.objects.all().order_by('-date')
    info = pagination.PageNumber(querysets_list=querysets_list, page=page, num=num)
    #获取本页数据
    info['content'] = get_dairy(querysets_list = list(info['content']))
    info = pagination.PageNumber_order_number(info, False)
    return info

def get_dairydetail(id):
    info = {}
    querysets_list_first = db_DairyContent.objects.filter(DairyDetail = id).first()
    info['content'] = querysets_list_first.content
    return info