from django.shortcuts import render


def issue_view(request):
    if request.method == 'GET':
        issue_id = request.GET.get("issue_id", "")
    elif request.method == 'POST':
        pass
