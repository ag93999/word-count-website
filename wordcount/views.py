from django.shortcuts import render
import operator


def about(request):
    """
    This view is used to set the about page.
    """
    return render(request, 'about.html')


def homepage(request):
    """
    This view is used to set the home page where you can enter your text.
    """
    return render(request, 'home.html')


def count(request):
    """
    This view is used to set the count page which will show you the text that you entered and the occurrence of each word.
    """
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': sortedwords})
