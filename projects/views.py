from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
        {
            'id':'1',
            'title':'Ecommerce website',
            'description':'Ecommerce website'
        },
        {
            'id':'2',
            'title':'Ecommerce website 2',
            'description':'Ecommerce website 2'
        },
        {
            'id':'3',
            'title':'Ecommerce website 3',
            'description':'Ecommerce website 3 '
        },
]

# Create your views here.
def projects(request):
    page = 'projects'
    number = 9
    context = {'page':page,'number':number,'projects':projectsList}
    return render(request,'projects/projects.html', context)#msg if u wanna pass anything dynamic to the page

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i

    return render(request,'projects/single-project.html',{'project':projectObj})