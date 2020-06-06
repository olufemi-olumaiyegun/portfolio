from django.shortcuts import render, get_object_or_404
from .models import Project	
	
# Create your views here.


def homepage(request):
	projects = Project.objects.all()

	return render(request, 'projects.html', {'projects':projects})
	
def detail(request, project_id):
	project_detail = get_object_or_404(Project, pk=project_id)
	return render (request, 'detail.html', {'project':project_detail})
