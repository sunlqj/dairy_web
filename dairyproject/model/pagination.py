from rest_framework.pagination import PageNumberPagination
  
  
class MyPageNumberPagination(PageNumberPagination):
    page_size = 10 # 每页默认展示数据的条数
    page_size_query_param = 'size' # ?page=xx&size=??
    max_page_size = 30 # 设置了每个可以展示的最大数据条数


from django.core.paginator import Paginator
def PageNumber(querysets_list=[], page=1, num=10, num_max=30):
    """
    数据分页
    :input querysets_list 数据列表
    :input page           要第几页
    :input num            每页数量
    :input num_max        最大每页数量
    """
    #输入内容
    page = int(page)
    num = min(int(num), num_max)
    #分页
    paginator = Paginator(querysets_list, num)
    
    info = {
        'all_num'      : len(querysets_list), # 总数据量
        'pages_num'    : paginator.num_pages, # 总页数
        'page'         : page,                # 当前页的页数
        'num'          : num,                 # 请求时填写的每页商品数
        #'order_number' : [],                  # 序号
        'content'      : []                   # 内容
    }
    #如果超过数量
    if page > paginator.num_pages:  # 总页数
        return info
    #获取内容
    info['content']  = list(paginator.page(number=page))

    return info

                
def PageNumber_order_number(info, order):
    """
    给分页数据加序号
    :input info  分页数据
    :input order 正序True/倒序False
    :return info 增加序号的分页数据
    """
    #基础数据
    page = info['page']
    num  = info['num']
    content_num = len(info['content'])
    all_num = info['all_num']
    
    #正序
    if order:
        start_number = (page - 1) * num
        order_number_list = [i + 1 for i in range(start_number, start_number + content_num)]
        for n in range(content_num):
            info['content'][n]['order_number'] = order_number_list[n]
    #倒序
    else:
        start_number = (page - 1) * num
        order_number_list = [all_num - i for i in range(start_number, start_number + content_num)]
        for n in range(content_num):
            info['content'][n]['order_number'] = order_number_list[n]
    return info