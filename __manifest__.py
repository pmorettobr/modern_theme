# -*- coding: utf-8 -*-
{
    'name': 'My Theme Plus',
    'version': '16.0.1.0.0',
    'summary': 'Melhorias complementares ao modern_theme',
    'description': """
        Módulo complementar ao modern_theme (pmorettobr).
        Adiciona o que está faltando sem quebrar nada:

        ✅ Fonte moderna (DM Sans)
        ✅ Scrollbar mais fina (6px)
        ✅ Hover nas linhas da list view
        ✅ Header da tabela com estilo uppercase
        ✅ Transições suaves nos botões
        ✅ Fade ao trocar de view
        ✅ Search facets modernos
        ✅ Kanban hover com elevação
        ✅ Form sheet com sombra melhorada
        ✅ Separadores de seção refinados
        ✅ Status bar melhorada
        ✅ Notificações/Toasts mais elegantes
        ✅ Dropdown com sombra profunda
        ✅ Badges de status coloridos
    """,
    'author': 'My Company',
    'category': 'Themes/Backend',
    # ← depende do modern_theme que já está instalado
    'depends': ['modern_theme'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        # CSS puro no bundle de backend — sem SCSS, sem risco de erro
        'web.assets_backend': [
            'my_theme_plus/static/src/css/enhancements.css',
        ],
    },
}
