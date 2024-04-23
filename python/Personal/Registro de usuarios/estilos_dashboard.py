colores = {
        'blanco': "#ffffff",
        'azul_claro_claro': "#858CB6",
        'azul_claro': "#676f9d",
        'azul_medio': "#424769",
        'azul_oscuro': "#2d3250",
        'tomate': "#ffb17a",
    }



button_pages_toolbar = f"""
    QPushButton {{
        height: 40px;
        width: 100px;
        background-color: transparent;
        color: #d9dde7;
        border: none;
        font-size: 17px;
        font-family: Raleway;
        border-radius: 20px;
    }}

    QPushButton:hover {{
        background: rgba(240, 240, 240, 200);
        border-radius: 20px;  
        color: #000000;
    }}

    QPushButton:pressed {{
        background: rgba(200, 200, 200, 200);
        border-radius: 20px;  
        color: #000000;
    }}

    QPushButton:checked {{
        background: rgba(240, 240, 240, 200);
        border-radius: 20px;  
        color: #000000;
    }}
"""
button_pages_toolbar_selected = f"""
    QPushButton {{
        height: 40px;
        width: 100px;
        background: rgba(240, 240, 240, 200);
        color: #000000;
        font-size: 17px;
        border: none;
        font-family: Raleway;
        border-radius: 20px;
    }}
"""

social_button_toolbar = f"""
    QPushButton {{
        background-color: transparent;
        border: none;
    }}
"""

estilo_barra_busqueda = f"""
    QLineEdit {{
        background-color: transparent;
        border: none;
        padding: 10 20px;
        border-bottom: 4px solid #676f9d;
        font-size: 17px;
        font-family: Raleway;
        color: #676f9d;
    }}

    QLineEdit:focus {{
        border-bottom: 4px solid #ffb17a;
    }}
"""


estilo_search_frame  = f"""
    QFrame {{
        background-color: #2d3250;
        border: none;
    }}
"""


no_fondo = f"""
    QPushButton {{
        background-color: transparent;
        border: none;
    }}
"""

estilo_volver_search_page = f"""
    QPushButton {{
        background-color: #2d3250;
        border-radius: 25px;
        padding: 5px;
    }}
    QFrame {{
        background-color: qlineargradient(
            spread: pad, 
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #424769,
            stop: 0.5 #424769,
            stop: 0.51 #2d3250
        );
    }}
"""

estilo_resulst_search_page= f"""
    QFrame {{
        background-color: #424769
    }}
"""

estilo_volver_map_page = f"""
    QPushButton {{
        background-color: #5C5F6E;
        border-radius: 25px;
        padding: 5px;
    }}
    QFrame {{
        background-color: qlineargradient(
            spread: pad, 
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #F8F0D9,
            stop: 0.5 #F8F0D9,
            stop: 0.51 #5C5F6E
        );
    }}
"""