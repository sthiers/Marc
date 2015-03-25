from django.shortcuts import render
from story1.models import Compound
from story1.forms import Story1Form
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return render(request, 'story1/index.html',{})
    

def compound_list(request):
    if request.method == 'POST':
        form = Story1Form(request.POST)

        if form.is_valid():
        
####    with open(os.path.join(MEDIA_ROOT, 'drugbase.csv'), newline='\n') as csvfile:
####        reader = csv.reader(csvfile, delimiter=';')
####        for row in spamreader:
####            print(', '.join(row))
            compound_list = Compound.objects.all()
            return render(request, 'story1/compound_list.html', {'compound_list': compound_list})
    else:
        raise Http404
        
