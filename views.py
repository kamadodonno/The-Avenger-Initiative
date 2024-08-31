from django.shortcuts import render, redirect

def index(request):
    if request.method == "GET":
        query = request.GET.get('q', None)

        if query:
            if query.lower() == 'ironworr!or27':
                return redirect('iron')
            else:
                google_url = f"https://www.google.com/search?q={query}"
                return redirect(google_url)
        else:
            return render(request, 'index.html')

def iron(request):
    return render(request, 'iron.html')
