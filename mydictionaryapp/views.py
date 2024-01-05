from django.shortcuts import render, redirect
from .utils import add_to_file, read_from_file

def home(request):
    return render(request, 'mydictionaryapp/home.html')

def words_list(request):
    words = read_from_file()
    return render(request, 'mydictionaryapp/words_list.html', {'words': words})

def add_word(request):
    if request.method == 'POST':
        word1 = request.POST.get('word1')
        word2 = request.POST.get('word2')
        add_to_file(word1, word2)
        return redirect('home')
    return render(request, 'mydictionaryapp/add_word.html')
