from collections import OrderedDict

from django.db import connection

def dictfetchall(cursor):
    desc = cursor.description
    return  [
        dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
    ]
def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))



def list_foods(request):
    if request.GET.get('user'):
        user = request.GET.get('user')
    sql =  """
    select * from foods_food
    ORDER BY created_dt DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return OrderedDict([
        ("items",data)
    ])
def one_food(request,pk):
    if request.GET.get('user'):
        user = request.GET.get('user')
    sql =  f"""
    select * from foods_food
    where id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql,[pk])
        data = dictfetchone(cursor)
    return OrderedDict([
        ("item",data)
    ])