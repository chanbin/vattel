from django.shortcuts import render

# Create your views here.
def base_index(request):
    return render(request, 'base/index.html')
    
def base_charts(request):
    return render(request, 'base/charts.html')
    
def base_tables(request):
    return render(request, 'base/tables.html')
    
def base_forms(request):
    return render(request, 'base/forms.html')
    
def base_bootstrap_elements(request):
    return render(request, 'base/bootstrap-elements.html')
    
def base_bootstrap_grid(request):
    return render(request, 'base/bootstrap-grid.html')
    
def base_dropdown(request):
    return render(request, 'base/tables.html')
    
def base_blank_page(request):
    return render(request, 'base/blank-page.html')
    
def base_index_rtl(request):
    return render(request, 'base/index-rtl.html')