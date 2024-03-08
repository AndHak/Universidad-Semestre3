import traceback
import unittest
from test_builder import TestBuilder9
from corrección import VehiculoPasajeros, EmpresaTransporte


class TestEmpresaTransporte(TestBuilder9):
    # Es posible desactivar cualquiera de las pruebas colocando el valor de
    # cero a cualquiera de ellas en el siguiente diccionario:
    dict_pruebas = {"presentar": 10, "vincular": 10, "posicionar": 10,
                    "despachar": 10, "marca": 10, "desvincular": 10}

    # Configuración de las Pruebas: Vinculación de 5 vehículos de pasajeros a
    # la empresa de transporte "Trans Python" de NIT 159-7895480 y con un
    # número máximo de vehículos en su flota de 10
    def setUp(self):
        self.emp_trans = EmpresaTransporte("159-7895480", "Trans Python", 10)
        vhp_1 = VehiculoPasajeros("123-6", "mazda", 11)
        vhp_2 = VehiculoPasajeros("234-9", "renault", 12)
        vhp_3 = VehiculoPasajeros("345-2", "chevrolet", 13)
        vhp_4 = VehiculoPasajeros("456-5", "nissan", 14)
        vhp_5 = VehiculoPasajeros("567-8", "hyundai", 15)

        lista_vehiculos = [vhp_1, vhp_2, vhp_3, vhp_4, vhp_5]

        for vhp in lista_vehiculos:
            self.emp_trans.vincular_VP(vhp)

    def test_0(self):
        self.presentación("Test Empresa de Transporte")

    # Prueba de verificación de la cadena generada por un objeto de tipo
    # EmpresaTransporte.
    # Calificación Máxima = 0.2
    def test_1_presentación_empresa_transporte(self):
        iTest = 1
        sTitle = "Presentación de la Empresa de Transporte"
        fMax_nota = 0.20
        Nt1_1 = fMax_nota * 1.0
        if self.dict_pruebas.get("presentar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """

            # Poner maxDiff a None para aceptar cadenas muy muy largas.
            self.maxDiff = None
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("Empresa:Trans Python/NIT:159-7895480\n"
                                    "Máx Vehículos:<10>",
                                    str, [self.emp_trans], Nt1_1, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST ##############
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Prueba de vinculación de nuevos vehículos de pasajeros a la
    # empresa de transporte, validando su número de registro único.
    # Calificación Máxima = 1.0
    def test_2_vincular_VP(self):
        iTest = 2
        sTitle = "Vinculación de nuevos Vehículos"
        fMax_nota = 1.0
        Nt2_1 = fMax_nota * 0.1 / 4  # len
        Nt2_2 = fMax_nota * 0.7 / 9  # vincular_VP
        Nt2_3 = fMax_nota * 0.2  # la_flota
        if self.dict_pruebas.get("vincular"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """
            # Poner maxDiff a None para aceptar cadenas muy muy largas.
            self.maxDiff = None

            # Cálculo del número de vehículos actualmente registrados en la
            # empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(5, len, [self.emp_trans], Nt2_1, le)

            # Intentamos agregar un vehículo cuyo número de registro único es
            # INCORRECTO
            vhp_6e = VehiculoPasajeros("678-0", "aik", 0)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.vincular_VP,
                                    [vhp_6e], Nt2_2, le)

            # Agregamos un nuevo vehículo de pasajeros de forma satisfactoria
            vhp_6 = VehiculoPasajeros("678-1", "kia", 16)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.vincular_VP,
                                    [vhp_6], Nt2_2, le)

            # Cálculo del número de vehículos actualmente registrados en la
            # empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(6, len, [self.emp_trans], Nt2_1, le)

            # Agregamos un nuevo vehículo de pasajeros de forma satisfactoria
            vhp_7 = VehiculoPasajeros("789-4", "daewoo", 17)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.vincular_VP,
                                    [vhp_7], Nt2_2, le)

            # Intentamos agrgar un vehículo que ya existe, con el mismo número
            # único de registro
            vhp_5e = VehiculoPasajeros("567-8", "hyundai", 15)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.vincular_VP,
                                    [vhp_5e], Nt2_2, le)

            # Agregamos un nuevo vehículo de pasajeros de forma satisfactoria
            vhp_8 = VehiculoPasajeros("890-7", "mitsubishi", 18)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.vincular_VP,
                                    [vhp_8], Nt2_2, le)

            # Agregamos un nuevo vehículo de pasajeros de forma satisfactoria
            vhp_9 = VehiculoPasajeros("901-0", "toyota", 19)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.vincular_VP,
                                    [vhp_9], Nt2_2, le)

            # Agregamos un nuevo vehículo de pasajeros de forma satisfactoria
            vhp_10 = VehiculoPasajeros("101-2", "ford", 20)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.vincular_VP,
                                    [vhp_10], Nt2_2, le)

            # Cálculo del número de vehículos actualmente registrados en la
            # empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.emp_trans], Nt2_1, le)

            # Intentamos agregar un nuevo vehículo de pasajeros cuando el
            # límite máximo de vehículos de la la flota ya ha llegado al tope
            vhp_11 = VehiculoPasajeros("202-4", "renault", 21)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.vincular_VP,
                                    [vhp_11], Nt2_2, le)

            # Intentamos agregar un nuevo vehículo de pasajeros cuando el
            # límite máximo de vehículos de la la flota ya ha llegado al tope
            vhp_12 = VehiculoPasajeros("303-6", "toyota", 22)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.vincular_VP,
                                    [vhp_12], Nt2_2, le)

            # Cálculo del número de vehículos actualmente registrados en la
            # empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.emp_trans], Nt2_1, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{[123-6:mazda:11:0] -> "
                                    "[234-9:renault:12:0] -> "
                                    "[345-2:chevrolet:13:0] -> "
                                    "[456-5:nissan:14:0] -> "
                                    "[567-8:hyundai:15:0] -> "
                                    "[678-1:kia:16:0] -> "
                                    "[789-4:daewoo:17:0] -> "
                                    "[890-7:mitsubishi:18:0] -> "
                                    "[901-0:toyota:19:0] -> "
                                    "[101-2:ford:20:0]}",
                                    self.emp_trans.la_flota, [], Nt2_3, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST ##############
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Prueba de vinculación de nuevos vehículos, en una determinada posición,
    # en la flota de vehículos de la empresa de transporte.
    # Calificación Máxima = 1.2
    def test_3_posicionar_VP(self):
        iTest = 3
        sTitle = "Nuevos vehículos a registrar en una posición" \
            " determinada en la flota de la Empresa de Transporte"
        fMax_nota = 1.2
        Nt3_1 = fMax_nota * 0.65 / 14  # posicionar_VP
        Nt2_2 = fMax_nota * 0.05 / 2  # len
        Nt3_3 = fMax_nota * 0.30 / 3  # la_flota
        if self.dict_pruebas.get("posicionar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """

            self.emp_trans = EmpresaTransporte("000-0000000",
                                               "Empresa Transporte", 10)

            # Intento por Insertar un vehículo en una posición INCORRECTA
            vhp_1 = VehiculoPasajeros("123-6", "mazda", 11)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.posicionar_VP,
                                    [vhp_1, 1], Nt3_1, le)

            # Intento por Insertar un vehículo en una posición INCORRECTA
            vhp_2 = VehiculoPasajeros("234-9", "renault", 12)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.posicionar_VP,
                                    [vhp_2, -1], Nt3_1, le)

            # Cálculo del número de vehículos de la empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [self.emp_trans], Nt2_2, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{}", self.emp_trans.la_flota,
                                    [], Nt3_3, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_5 = VehiculoPasajeros("567-8", "hyundai", 15)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_5, 0], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_2, 0], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_3 = VehiculoPasajeros("345-2", "chevrolet", 13)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_3, 1], Nt3_1, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{[234-9:renault:12:0] -> "
                                    "[345-2:chevrolet:13:0] -> "
                                    "[567-8:hyundai:15:0]}",
                                    self.emp_trans.la_flota, [], Nt3_3, le)

            # Intento por Insertar un vehículo en una posición INCORRECTA
            vhp_8 = VehiculoPasajeros("890-7", "mitsubishi", 18)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.posicionar_VP,
                                    [vhp_8, 4], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_7 = VehiculoPasajeros("789-4", "daewoo", 17)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_7, 3], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_10 = VehiculoPasajeros("101-2", "ford", 20)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_10, 4], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_4 = VehiculoPasajeros("456-5", "nissan", 14)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_4, 2], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_1, 0], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_6 = VehiculoPasajeros("678-1", "kia", 16)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_6, 5], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_8, 7], Nt3_1, le)

            # Agregamos un nuevo vehículo de pasajeros en una posición CORRECTA
            vhp_9 = VehiculoPasajeros("901-0", "toyota", 19)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, self.emp_trans.posicionar_VP,
                                    [vhp_9, 8], Nt3_1, le)

            # Intento de agregar un nuevo vehículo de pasajeros cuando el cupo
            # de la flota ya excede su número máximo
            vhp_11 = VehiculoPasajeros("561-2", "chevrolet", 7)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False, self.emp_trans.posicionar_VP,
                                    [vhp_11, 8], Nt3_1, le)

            # Cálculo del número de vehículos de la empresa de transporte
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.emp_trans], Nt2_2, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{[123-6:mazda:11:0] -> "
                                    "[234-9:renault:12:0] -> "
                                    "[345-2:chevrolet:13:0] -> "
                                    "[456-5:nissan:14:0] -> "
                                    "[567-8:hyundai:15:0] -> "
                                    "[678-1:kia:16:0] -> "
                                    "[789-4:daewoo:17:0] -> "
                                    "[890-7:mitsubishi:18:0] -> "
                                    "[901-0:toyota:19:0] -> "
                                    "[101-2:ford:20:0]}",
                                    self.emp_trans.la_flota, [], Nt3_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # # Prueba de evaluación del despacho de un vehículo de pasajeros,
    # # modificando su número de viajes.
    # # Calificación Máxima = 0.8
    def test_4_despachar_VP(self):
        iTest = 4
        sTitle = "Despachar un Vehículo"
        fMax_nota = 0.8
        Nt4_1 = fMax_nota * 0.375 / 3  # str
        Nt4_2 = fMax_nota * 0.5 / 4  # despachar_VP
        Nt4_3 = fMax_nota * 0.125  # la_flota
        if self.dict_pruebas.get("despachar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """
            # Despacho del vehículo de pasajeros ("456-5", "nissan", 14) 4x
            vhp_4 = VehiculoPasajeros("456-5", "nissan", 14)
            for _ in range(3):
                self.emp_trans.despachar_VP(vhp_4)
            vhp_mod_4 = self.emp_trans.despachar_VP(vhp_4)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("[456-5:nissan:14:4]",
                                    str, [vhp_mod_4], Nt4_1, le)

            # Despacho del vehículo de pasajeros ("456-5", "nissan", 14) 5x
            vhp_5 = VehiculoPasajeros("567-8", "hyundai", 15)
            for _ in range(4):
                self.emp_trans.despachar_VP(vhp_5)
            vhp_mod_5 = self.emp_trans.despachar_VP(vhp_5)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("[567-8:hyundai:15:5]",
                                    str, [vhp_mod_5], Nt4_1, le)

            # Despacho de vehículos de pasajeros que NO EXISTEN
            vhp_2_e = VehiculoPasajeros("234-99", "renault", 12)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(None,
                                    self.emp_trans.despachar_VP, [vhp_2_e],
                                    Nt4_2, le)
            vhp_3_e = VehiculoPasajeros("345-2", "Chevrolet", 13)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(None,
                                    self.emp_trans.despachar_VP, [vhp_3_e],
                                    Nt4_2, le)
            vhp_1_e = VehiculoPasajeros("123-6", "mazda", 111)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(None,
                                    self.emp_trans.despachar_VP, [vhp_1_e],
                                    Nt4_2, le)
            vhp_e = VehiculoPasajeros("696", "marca", 0)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(None,
                                    self.emp_trans.despachar_VP, [vhp_e],
                                    Nt4_2, le)

            # Despacho del vehículo de pasajeros ("123-6", "mazda", 11) 10x
            vhp_1 = VehiculoPasajeros("123-6", "mazda", 11)
            for _ in range(9):
                self.emp_trans.despachar_VP(vhp_1)
            vhp_mod_1 = self.emp_trans.despachar_VP(vhp_1)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("[123-6:mazda:11:10]",
                                    str, [vhp_mod_1], Nt4_1, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{[123-6:mazda:11:10] -> "
                                    "[234-9:renault:12:0] -> "
                                    "[345-2:chevrolet:13:0] -> "
                                    "[456-5:nissan:14:4] -> "
                                    "[567-8:hyundai:15:5]}",
                                    self.emp_trans.la_flota, [], Nt4_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Prueba en la que se busca los vehículos que tengan una determinada marca.
    # Calificación Máxima = 0.8
    def test_5_mini_flota_marca(self):
        iTest = 5
        sTitle = "Listado de vehículos por marca"
        fMax_nota = 0.8
        Nt5_1 = fMax_nota * 0.3 / 6  # len
        Nt5_2 = fMax_nota * 0.7 / 5  # veh in lst_m_renault
        if self.dict_pruebas.get("marca"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """
            # Se realiza la modificación del número máximo de vehículos de la
            # flota
            self.emp_trans.num_max = 12

            vhp_1 = VehiculoPasajeros("123-6", "mazda", 11)
            vhp_2 = VehiculoPasajeros("234-9", "renault", 12)
            vhp_3 = VehiculoPasajeros("345-2", "chevrolet", 13)
            vhp_4 = VehiculoPasajeros("456-5", "nissan", 14)
            vhp_5 = VehiculoPasajeros("567-8", "hyundai", 15)

            vhp_6 = VehiculoPasajeros("678-1", "chevrolet", 16)
            vhp_7 = VehiculoPasajeros("789-4", "nissan", 17)
            vhp_8 = VehiculoPasajeros("890-7", "chevrolet", 18)
            vhp_9 = VehiculoPasajeros("901-0", "renault", 19)
            vhp_10 = VehiculoPasajeros("101-2", "renault", 20)
            vhp_11 = VehiculoPasajeros("202-4", "renault", 21)
            vhp_12 = VehiculoPasajeros("303-6", "mazda", 22)

            # Adicionamos 7 vehículos más a la flota original de 5 vehículos
            # de la empresa de trasnporte
            lista_vehiculos = [vhp_6, vhp_7, vhp_8,
                               vhp_9, vhp_10, vhp_11, vhp_12]

            for vhp in lista_vehiculos:
                self.emp_trans.vincular_VP(vhp)

            # Generamos un listado con todos los vehículos de marca "mazda"
            lst_m_mazda = self.emp_trans.mini_flota_marca("mazda")
            lst_m_mazda_OK = [vhp_1, vhp_12]

            # Número de vehículos con la marca "mazda"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_mazda_OK),
                                    len, [lst_m_mazda], Nt5_1, le)

            # Comparación de la lista obtenida con la lista esperada OK
            for veh in lst_m_mazda_OK:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True,
                                       veh in lst_m_mazda,
                                       f"Vehículo //{veh}// sea de marca 'mazda'",
                                       Nt5_2/len(lst_m_mazda_OK), le)

            # Generamos un listado con todos los vehículos de marca "renault"
            lst_m_renault = self.emp_trans.mini_flota_marca("renault")
            lst_m_renault_OK = [vhp_2, vhp_9, vhp_10, vhp_11]

            # Número de vehículos con la marca "renault"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_renault_OK),
                                    len, [lst_m_renault], Nt5_1, le)

            # Comparación de la lista obtenida con la lista esperada OK
            for veh in lst_m_renault_OK:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True,
                                       veh in lst_m_renault,
                                       f"Vehículo //{veh}// sea de marca 'renault'",
                                       Nt5_2/len(lst_m_renault_OK), le)

            # Generamos un listado con todos los vehículos de marca "chevrolet"
            lst_m_chevrolet = self.emp_trans.mini_flota_marca("chevrolet")
            lst_m_chevrolet_OK = [vhp_3, vhp_6, vhp_8]

            # Número de vehículos con la marca "chevrolet"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_chevrolet_OK),
                                    len, [lst_m_chevrolet], Nt5_1, le)

            # Comparación de la lista obtenida con la lista esperada OK
            for veh in lst_m_chevrolet_OK:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True,
                                       veh in lst_m_chevrolet,
                                       f"Vehículo //{veh}// sea de marca 'chevrolet'",
                                       Nt5_2/len(lst_m_chevrolet_OK), le)

            # Generamos un listado con todos los vehículos de marca "nissan"
            lst_m_nissan = self.emp_trans.mini_flota_marca("nissan")
            lst_m_nissan_OK = [vhp_4, vhp_7]

            # Número de vehículos con la marca "nissan"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_nissan_OK),
                                    len, [lst_m_nissan], Nt5_1, le)

            # Comparación de la lista obtenida con la lista esperada OK
            for veh in lst_m_nissan_OK:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True,
                                       veh in lst_m_nissan,
                                       f"Vehículo //{veh}// sea de marca 'nissan'",
                                       Nt5_2/len(lst_m_nissan_OK), le)

            # Generamos un listado con todos los vehículos de marca "hyundai"
            lst_m_hyundai = self.emp_trans.mini_flota_marca("hyundai")
            lst_m_hyundai_OK = [vhp_5]

            # Número de vehículos con la marca "hyundai"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_hyundai_OK),
                                    len, [lst_m_hyundai], Nt5_1, le)

            # Comparación de la lista obtenida con la lista esperada OK
            for veh in lst_m_hyundai_OK:
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True,
                                       veh in lst_m_hyundai,
                                       f"Vehículo //{veh}// sea de marca 'hyundai'",
                                       Nt5_2/len(lst_m_hyundai_OK), le)

            # Intentamos generar un listado con los vehículos de marca
            # "ferrari" la cual NO EXISTE
            lst_m_ferrari = self.emp_trans.mini_flota_marca("ferrari")
            lst_m_ferrari_OK = []

            # Número de vehículos con la marca  "ferrari"
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(len(lst_m_ferrari_OK),
                                    len, [lst_m_ferrari], Nt5_1, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    # Prueba en la que se intenta eliminar un vehículo de pasajeros de la flota
    # actual de la empresa.
    # Calificación Máxima = 1.0
    def test_6_desvincular_VP(self):
        iTest = 6
        sTitle = "Eliminar un vehículo de la flota de la Empresa de Transporte"
        fMax_nota = 1.0
        Nt6_1 = fMax_nota * 0.9 / 6  # desvincular_VP
        Nt6_2 = fMax_nota * 0.1 / 3  # len
        if self.dict_pruebas.get("desvincular"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """
            # Eliminación del vehículo de pasajeros ("345-2", "chevrolet", 13)
            vhp_3 = VehiculoPasajeros("345-2", "chevrolet", 13)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.emp_trans.desvincular_VP, [vhp_3],
                                    Nt6_1, le)

            # Evaluación del número de vehículos actualmente en la flota
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(4, len, [self.emp_trans], Nt6_2, le)

            # Eliminación del vehículo de pasajeros ("567-8", "hyundai", 15)
            vhp_5 = VehiculoPasajeros("567-8", "hyundai", 15)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.emp_trans.desvincular_VP, [vhp_5],
                                    Nt6_1, le)

            # Intentamos elimina un vehículo de pasajeros que NO EXISTE
            vhp_8 = VehiculoPasajeros("890-7", "chevrolet", 18)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.emp_trans.desvincular_VP, [vhp_8],
                                    Nt6_1, le)

            # Evaluación del número de vehículos actualmente en la flota
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(3, len, [self.emp_trans], Nt6_2, le)

            # Eliminación del vehículo de pasajeros ("567-8", "hyundai", 15)
            vhp_1 = VehiculoPasajeros("123-6", "mazda", 11)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.emp_trans.desvincular_VP, [vhp_1],
                                    Nt6_1, le)
            # Intentamos elimina un vehículo de pasajeros que NO EXISTE
            vhp_2e = VehiculoPasajeros("234-9", "Renault", 12)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.emp_trans.desvincular_VP, [vhp_2e],
                                    Nt6_1, le)

            # Evaluación del número de vehículos actualmente en la flota
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(2, len, [self.emp_trans], Nt6_2, le)

            # Comprobación de los vehículos registrados en la flota de la
            # empresa, generando una cadena con el formato especificado
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2("{[234-9:renault:12:0] -> "
                                    "[456-5:nissan:14:0]}",
                                    self.emp_trans.la_flota, [], Nt6_1, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final(modo_estudiante=True)


if __name__ == "__main__":
    unittest.main(verbosity=0)
