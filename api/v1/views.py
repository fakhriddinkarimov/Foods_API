from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from  rest_framework.generics import GenericAPIView
from .serializers import FoodsSerializer
from .services import list_foods,one_food
from foods.models import Food
class FoodwView(GenericAPIView):
    serializer_class = FoodsSerializer
    queryset = Food.objects.all()
    def get_object(self,*args,**kwargs):
        try:
            if "pk" in kwargs and kwargs["pk"]:
                food = Food.objects.get(pk=kwargs["pk"])
        except Exception as e:
            raise  NotFound("NOT FOUND FOODS")
        return food

    def get(self,request,*args,**kwargs):
        if "pk" in kwargs and kwargs["pk"]:
            result = one_food(request,kwargs["pk"])
        else:
            result = list_foods(request)
        return Response(result,status=status.HTTP_200_OK,content_type='application/json')
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        result = one_food(request,pk=data.id)
        return  Response(result,status=status.HTTP_200_OK,content_type='applications.json')
    def put(self,request,*args,**kwargs):
        data = self.get_object(*args,**kwargs)
        serializer = self.get_serializer(data=request.data,instance=data,partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()                                                             
        result = one_food(request,pk=data.id)
        return  Response(result,status=status.HTTP_200_OK,content_type='applications.json')
    def delete(self,request,*args,**kwargs):
        data = Food.objects.get(pk=kwargs["pk"])
        data.delete()
        data.save()
        return  Response(None,status=status.HTTP_204_NO_CONTENT,content_type='applications.json')