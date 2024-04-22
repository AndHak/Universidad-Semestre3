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
