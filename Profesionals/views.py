from django.shortcuts import render

def ProfesionalIndexView(request):
	return render(request, 'index.html', {
		'hola': "hi"
	})