

colores = {
        'blanco': "#ffffff",
        'azul_claro_claro': "#858CB6",
        'azul_claro': "#676f9d",
        'azul_medio': "#424769",
        'azul_oscuro': "#2d3250",
        'tomate': "#ffb17a",
        'brillante': '#FFC295',
        'oscuro': '#FCA668',
        'blanco_hover': "#DCDBDB",
        'blanco_clicked': "#C1C1C1",
        'rojo_fail': "#FF5C5C",
    }

estilos_sections = f"""
    QPushButton {{
        font-family: Raleway Semibold;
        font-size: 16px;
        color: {colores['azul_claro']};
        border: none;
        }}

    QPushButton:checked {{
        font-family: Raleway Semibold;
        font-size: 16px;
        color: white;
        border-bottom: 4px solid {colores['tomate']};
    }}
    
    """

estilo_bienvenido = f"""
    QLabel {{
        font-family: Raleway SemiBold;
        font-size: 30px;
        color: {colores['blanco']};
        }}
    
    """

estilos_label2 = f"""
    QLabel {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        }}
    
    """

estilos_line_edit = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: none;
        height: 50px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative;

    }}

    QLineEdit:focus {{
        border-left: 4px solid {colores['tomate']};
    }}

    QLineEdit:placeholder {{
        color: {colores['azul_claro']};
        font-size: 15px;
        top: 5px; 
        right: 15px; 
    }}

    
    """


estilos_line_edit_hide = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: none;
        height: 50px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative; 
    }}

    QLineEdit:focus {{
        border-left: 4px solid {colores['tomate']};
    }}

    QLineEdit:placeholder {{
        color: {colores['azul_claro']};
        font-size: 15px;
        top: 5px; 
        right: 15px; 
    }}


    """

estilo_boton_pass = f"""
    QPushButton {{
        background: transparent;
        border: none;
        color: {colores['azul_claro']};
    }}

    """

log_in_button = f"""
    QPushButton {{
        background-color: {colores['tomate']};
        font-family: Raleway Semibold;
        font-size: 18px;
        height: 60px;
        width: 210px;
        border-radius: 10px;
        border: 1px solid black;
    }}

     QPushButton:hover {{
        background-color: {colores['brillante']};
        border-color: {colores['brillante']}; 
    }}
    
    QPushButton:pressed {{
        background-color: {colores['oscuro']};
        border-color: {colores['oscuro']}; 
    }}
"""

estilo_remind_me = f"""
    QCheckBox {{
        font-size: 15px;
        color: {colores['blanco']};
    }}

    QCheckBox:hover {{
        font-size: 15px;
        color: {colores['blanco_hover']};
    }}
    QCheckBox::indicator:unchecked {{
        image: url(:/images/no_marcado.png);
    }}

    QCheckBox::indicator:checked {{
        image: url(:/images/marcado.png);
    }}
"""

estilos_forgot_password = f"""
    QPushButton {{
        background: transparent;
        color: {colores['azul_claro']};
        font-family: Raleway Semibold;
        font-size: 15px;
        border: none;
    }}

     QPushButton:hover {{
        color: {colores['azul_claro_claro']};
        text-decoration: underline;
    }}
    
    QPushButton:pressed {{
        color: {colores['azul_medio']};
    }}
"""

estilos_redes_sociales = f"""
    QPushButton {{
        height: 50px;
        width: 50px;
        background: transparent;
        border-radius: 10px;
    }}
    
    QPushButton:pressed {{
        color: {colores['azul_medio']};
    }}
"""

iniciar_sesion_con = f"""
    QLabel {{
        font-family: Raleway SemiBold;
        font-size: 16px;
        color: {colores['azul_claro']};
        }}
    
    """

registrarse_line_edit = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: none;
        height: 40px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative;

    }}

    QLineEdit:focus {{
        border-left: 4px solid {colores['tomate']};
    }}

    QLineEdit:placeholder {{
        color: {colores['azul_claro']};
        font-size: 15px;
        top: 5px; 
        right: 15px; 
    }}
    """


registrarse_line_edit_hide = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: none;
        height: 40px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative; 
    }}

    QLineEdit:focus {{
        border-left: 4px solid {colores['tomate']};
    }}

    QLineEdit:placeholder {{
        color: {colores['azul_claro']};
        font-size: 15px;
        top: 5px; 
        right: 15px; 
    }}
    """

registrarse_name = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: none;
        height: 40px;
        width: 155px;
        padding: 10px;
        padding-left: 20px;
        position: relative;

    }}

    QLineEdit:focus {{
        border-left: 4px solid {colores['tomate']};
    }}

    QLineEdit:placeholder {{
        color: {colores['azul_claro']};
        font-size: 15px;
        top: 5px; 
        right: 15px; 
    }}
    """

registrarse_line_edit_hide_fail = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: 1px solid {colores['rojo_fail']};
        border-radius: 3px;
        height: 40px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative; 
    }}

    """

names_registration_fail = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: 1px solid {colores['rojo_fail']};
        border-radius: 3px;
        height: 40px;
        width: 155px;
        padding: 10px;
        padding-left: 20px;
        position: relative;

    }}
    """

email_register_fail = f"""
    QLineEdit {{
        font-family: Raleway;
        font-size: 15px;
        color: {colores['blanco']};
        background-color: {colores['azul_medio']};
        border: 1px solid {colores['rojo_fail']};
        border-radius: 3px;
        height: 40px;
        width: 350px;
        padding: 10px;
        padding-left: 20px;
        position: relative;

    }}

    """