from django.contrib import admin
from .models import AcessoMedico, TiposExames, PedidosExames, SolicitacaoExame

admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
admin.site.register(AcessoMedico)
