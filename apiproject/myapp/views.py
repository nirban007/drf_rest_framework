from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from myapp.serializers import ContractSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import Contract
from rest_framework import status

class ContractViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Contract.objects.all()
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contract.objects.all()
        contract = get_object_or_404(queryset, pk=pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)

    def create(self, request):
        serilizer = ContractSerializer(data = request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        contact = Contract.objects.get(pk=pk)
        serilizer = ContractSerializer(contact, data = request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
































# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.http import Http404
# from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from myapp.models import Contract
# from myapp.serializers import ContractSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.reverse import reverse

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'contract': reverse('contract-list', request=request, format=format),
#     })





# #Using generic class-based views
# class ContractList(generics.ListCreateAPIView, mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# class ContractDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# #Writing regular Django views using our Serializer
# # @csrf_exempt
# # def api_list(request):

# #     if request.method == 'GET':
# #         apivar = Contract.objects.all()
# #         serializer = ContractSerializer(apivar, many=True)
# #         return JsonResponse(serializer.data, safe=False)

# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = ContractSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data, status=201)
# #         return JsonResponse(serializer.errors, status=400)

# # @csrf_exempt
# # def api_detail(request, pk):

# #     try:
# #         dvar = Contract.objects.get(pk=pk)
# #     except Contract.DoesNotExist:
# #         return HttpResponse(status=404)

# #     if request.method == 'GET':
# #         serializer = ContractSerializer(dvar)
# #         return JsonResponse(serializer.data)

# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = ContractSerializer(dvar, data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         dvar.delete()
# #         return HttpResponse(status=204)

# #Requests and Responses
# # @api_view(['GET', 'POST'])
# # def api_list(request):

# #     if request.method == 'GET':
# #         snip = Contract.objects.all()
# #         serializer = ContractSerializer(snip, many=True)
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = ContractSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def api_detail(request, pk):

# #     try:
# #         snip = Contract.objects.get(pk=pk)
# #     except Contract.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)

# #     if request.method == 'GET':
# #         serializer = ContractSerializer(snip)
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = ContractSerializer(snip, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     elif request.method == 'DELETE':
# #         snip.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

# #Rewriting our API using class-based views
# class BlogList(APIView):

#     def get(self, request, format=None):
#         snippets = Contract.objects.all()
#         serializer = ContractSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ContractSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ApiDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Contract.objects.get(pk=pk)
#         except Contract.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ContractSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ContractSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)