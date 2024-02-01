from .models import Course , Reviews , Categories
from .serializers import CourseListSerializer , CourseDetailSerializer , ReviewsSerializer , CategoriesListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters








class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter , filters.OrderingFilter]
    #filterset_fields = ['price ', 'name'] 
    search_fields = ['name', 'price']
    ordering_fields = ['price', 'name' ,'categorie']
    def get_queryset(self):
        queryset = super().get_queryset()
        categories = self.request.query_params.getlist('categorie')
        prices = self.request.query_params.getlist('price')

        if categories:
            queryset = queryset.filter(categorie__in=categories)
            #queryset = queryset.filter(categorie__name=categories)
        
        if prices :
             queryset = queryset.filter(price__in=prices)
             

        return queryset

   




class CourseDetailAPI(generics.RetrieveAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseDetailSerializer

class CategorieListAPI(generics.ListAPIView):
      queryset = Categories.objects.all() 
      serializer_class = CategoriesListSerializer