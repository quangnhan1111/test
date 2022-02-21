from rest_framework import mixins, generics, status
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from company.models import Company

from company.serializers import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# class CompanyMixins(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class DetailCompanyMixins(mixins.RetrieveModelMixin,
#                           mixins.CreateModelMixin,
#                           mixins.UpdateModelMixin,
#                           mixins.DestroyModelMixin,
#                           generics.GenericAPIView
#                           ):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#     def get(self, request, *args, **kwargs):
#         # query_set_a = Company.objects.exist()
#         if True:
#             print(self.queryset.query)
#             return self.retrieve(request, *args, **kwargs)
#         else:
#             return Response(data='no data', status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
def get_list(request):
    # companies = Company.objects.first()
    return Response(data='companies', status=status.HTTP_200_OK)
