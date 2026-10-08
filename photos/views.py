from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def photo_details_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-details-page.html')

def photo_add_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def photo_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')