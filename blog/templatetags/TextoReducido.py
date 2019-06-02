from django import template
register = template.Library()

@register.simple_tag

def TextoReducido(b):
    t0=b.find("<p")
    t00=b.find(">",t0)
    t1=b.find("</p>")
    TF=b[t00+1:t1]
    TF2=TF
    return TF
