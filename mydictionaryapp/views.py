from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Word
from .serializers import WordSerializer


@api_view(['GET'])
def words_list(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_word(request):
    if request.method == 'POST':
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Метод не разрешен'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_word(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return Response({'message': 'Слово не найдено'}, status=status.HTTP_404_NOT_FOUND)

    word.delete()
    return Response({'message': 'Слово успешно удалено'}, status=status.HTTP_204_NO_CONTENT)
