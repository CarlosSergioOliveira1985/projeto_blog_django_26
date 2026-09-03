from site_setup.models import SiteSetup




def context_processor_example(request):
    return{
        'exemplo':'Exemplo veio do context rocessor'
    }


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return{
        'site_setup': setup, 
    }