from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from . models import Outils
from . models import Media
    
def listview(request):
    return render(request,'outils/main.html')

def outil_render_pdf_view(request, *args, **kwargs):
    id = kwargs.get('id')
    outil = get_object_or_404(Outils, id=id)
    template_path = 'outils/generate_pdf.html'
    context = {'outil': outil}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # to directly download the pdf we need attachment 
    # response['Content-Disposition'] = 'attachment; filename="export.pdf"'

    # to view on browser we can remove attachment 
    response['Content-Disposition'] = 'filename="export.pdf'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response