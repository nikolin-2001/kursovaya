from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Discipline
from .serializers import DisciplineSerializer
from rest_framework.decorators import api_view

from django.shortcuts import render


def index(request):
    products = Discipline.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'tutorials/index.html', context)


@api_view(['GET', 'POST', 'DELETE'])
def discipline_list(request):
    if request.method == 'GET':
        disciplins = Discipline.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            disciplins = disciplins.filter(title__icontains=title)

        disciplins_serializer = DisciplineSerializer(disciplins, many=True)
        return JsonResponse(disciplins_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        discipline_data = JSONParser().parse(request)
        discipline_serializer = DisciplineSerializer(data=discipline_data)
        if discipline_serializer.is_valid():
            discipline_serializer.save()
            return JsonResponse(discipline_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(discipline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Discipline.objects.all().delete()
        return JsonResponse({'message': '{} Disciplins were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def discipline_detail(request, pk):
    try:
        discipline = Discipline.objects.get(pk=pk)
    except Discipline.DoesNotExist:
        return JsonResponse({'message': 'The discipline does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        discipline_serializer = DisciplineSerializer(discipline)
        return JsonResponse(discipline_serializer.data)

    elif request.method == 'PUT':
        discipline_data = JSONParser().parse(request)
        discipline_serializer = DisciplineSerializer(discipline, data=discipline_data)
        if discipline_serializer.is_valid():
            discipline_serializer.save()
            return JsonResponse(discipline_serializer.data)
        return JsonResponse(discipline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        discipline.delete()
        return JsonResponse({'message': 'Discipline was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def discipline_list_published(request):
    disciplins = Discipline.objects.filter(published=True)

    if request.method == 'GET':
        disciplins_serializer = DisciplineSerializer(disciplins, many=True)
        return JsonResponse(disciplins_serializer.data, safe=False)

