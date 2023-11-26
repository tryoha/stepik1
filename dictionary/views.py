from django.shortcuts import render, redirect

def index(request):
    context = {}
    return render(request, 'dictionary/index.html', context)


def add_word(requst):
    context = {}
    if requst.method == 'GET':
        return render(requst, 'dictionary/add_word.html', context)
    elif requst.method == 'POST':
        print(requst.POST) 
        with open('/mnt/projects/projects/django/stepic/dictionary.txt', 'a') as f:
            f.writelines(requst.POST['word1'] + "-" + requst.POST['word2'] + "\n")
        return redirect(index)
        


def read_from_file():
    file = open("/mnt/projects/projects/django/stepic/dictionary.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2

def wordslist(request):
    words1, words2 = read_from_file() 
    context = {"words": (zip(words1, words2))}
    return render(request, 'dictionary/wordslist.html', context)
