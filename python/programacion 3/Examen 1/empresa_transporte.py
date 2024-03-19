"""
    PROJECT: Evaluación 1 / Grupo 2

    MODULE: empresa_transporte.py

    DESCRIPTION:
    Construir un programa que permita administrar los vehículos de pasajeros
    que se encuentran adscritos a una Empresa de Transporte

    AUTHOR: Andrés Felipe Martínez Guerra
"""


class VehiculoPasajeros:
    """Un vehículo de pasajeros se caracteriza porque maneja un número único de
    registro, la marca, la capacidad máxima de pasajeros y el número de
    viajes realizado. Hay que tener en cuenta que el número de viajes realizado
    se inicializa en el constructor de forma automática a cero (0) y que la
    capacidad máxima por defecto es de diez (10) pasajeros
    """

    # Método constructor a ser implementado
    def __init__(self, cod_registro, marca, capacidad_maxima=10):
        self.cod_registro = cod_registro
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.numero_de_viajes = 0

    # Método VH # 1
    def __eq__(self, otro_vp):
        """Método de comparación de un vehículo de pasajeros, teniendo en
        cuenta el número único de registro, la marca y la capacidad máxima de
        pasajeros

        Parameters
        ----------
        otro_vp : VehiculoPasajeros
            El otro vehículo de pasajeros con el cual se van a ser las
            comparaciones

        Returns
        -------
        bool
            True si los vehículos de pasajeros son iguales. False en caso
        contrario
        """
        if otro_vp.cod_registro == self.cod_registro and otro_vp.marca == self.marca and otro_vp.capacidad_maxima == self.capacidad_maxima:
            return True
        else:
            return False
        

    # Método VH # 2
    def __repr__(self):
        """Método de presentación del vehículo de pasajeros

        Returns
        -------
        str
            Una cadena con el formato:
                "[NUR:marca:capacidad_máxima:número_de_viajes]"
            Ejemplo:
                "[836-7:Chevrolet:25:170]"
        """
        return f"[{self.cod_registro}:{self.marca}:{self.capacidad_maxima}:{self.numero_de_viajes}]"


class EmpresaTransporte:
    """La Empresa de Transporte se caracteriza por tener un NIT, un nombre, un
    número máximo de vehículos para su flota y el listado de todos los
    vehículos de pasajeros registrados (flota de vehículos de la empresa).
    """

    # Método constructor a ser implementado
    def __init__(self, nit, nombre, max_vehiculos):
        self.nit = nit
        self.nombre = nombre
        self.max_vehiculos = max_vehiculos
        self.vehiculos_registrados = []

    # Método ET # 1
    def vincular_VP(self, nuevo_vp):
        """Este método intenta registrar un vehículo de pasajeros a la flota de
        vehículos de la empresa. Hay que tener en cuenta que no se podrá
        registrar el mismo vehículo de pasajeros 2 veces o más y que se debe
        comprobar que con el nuevo vehículo no se sobrepase el límite del
        número máximo de vehículos de la flota. Tambien es necesario validar la
        Autenticidad del número de registro único del vehículo a registrar,
        teniendo en cuenta que este número consta de 2 partes:

                "número registro básico-dígito de verificación"

        donde el "dígito de verificación" es un valor igual al resíduo o módulo
        de la suma de los dígitos del número de registro básico entre diez (10)
        Ejm. Si el número de registro de un vehículo es "836-7" entonces para
        validar su AUTENTICIDAD sumamos 8 + 3 + 6 = 17 y a este resultado le
        sacamos el módulo entre 10, obteniendo como valor el 7. Por lo tanto el
        número de registro de identificación "836-7" es AUTÉNTICO.

        Parameters
        ----------
        nuevo_vp : VehiculoPasajeros
            El nuevo vehículo de pasajeros para ser adicionado a la flota de
            vehículos de la empresa

        Returns
        -------
        bool
            True si el nuevo vehículo es registrado por la empresa. False en
            caso contrario
        """
        suma = 0
        for digito in nuevo_vp.cod_registro[:-2]:  
            suma += int(digito)
        while suma % 10 != int(nuevo_vp.cod_registro[-1]):
            return False

        for vehiculo_registrado in self.vehiculos_registrados:
            if vehiculo_registrado.cod_registro == nuevo_vp.cod_registro:
                return False

        if len(self.vehiculos_registrados) + 1 > self.max_vehiculos:
            return False
        else:
            self.vehiculos_registrados.append(nuevo_vp)
            return True

    # Método ET # 2
    def posicionar_VP(self, nuevo_vp, pos):
        """Este método intenta ingresar un nuevo vehículo de pasajeros, en una
        determinada posición dentro de la flota de vehículos de la empresa. Al
        igual que en el método anterior, hay que tener en cuenta que no se
        podrá registrar el mismo vehículo de pasajeros 2 veces o más, que no se
        sobrepase el límite del número máximo de vehículos de la flota y
        también será necesario validar la Autenticidad del número de registro
        único del vehículo a registrar

        Parameters
        ----------
        nuevo_vp : VehiculoPasajeros
            El nuevo vehículo de pasajeros para ser adicionado a la flota de
            vehículos de la empresa
        pos : int
            Es el número de la posición en la que se requiere registrar el
            vehículo dentro de la flota, comenzando desde 0

            Ejemplo: Si el tamaño máximo de la flota es de 6 y actualmente
            se tiene 4 vehículos:
                [ 0   1   2   3]
                [🛺, 🚗, 🚙, 🛻]
            Se desea registrar 🚚 en la posición 2, entonces la flota queda:
                [ 0   1   2   3   4]
                [🛺, 🚗, 🚚, 🚙, 🛻]
            Ahora, si se desea registrar 🚐 en la posición 5, la flota queda:
                [ 0   1   2   3   4   5]
                [🛺, 🚗, 🚚, 🚙, 🛻, 🚐]
            Cualquier nuevo registro en una determinada posición ya no es
            posible, porque ya se alcanzó el límite máximo de la flota

        Returns
        -------
        bool
            True si el nuevo vehículo se pudo agregar a la flota en la
            posición determinada. False en caso contrario
        """
        suma = 0
        for digito in range(len(nuevo_vp.cod_registro)-1): 
            suma += int(digito)
        while suma % 10 != int(nuevo_vp.cod_registro[-1]):
            return False

        for vehiculo_registrado in self.vehiculos_registrados:
            if vehiculo_registrado.cod_registro == nuevo_vp.cod_registro:
                return False

        if len(self.vehiculos_registrados) + 1 > self.max_vehiculos:
            return False
        else:
            self.vehiculos_registrados.insert(pos, nuevo_vp)
            return True

        
        
        
        

    # Método ET # 3
    def despachar_VP(self, vehiculo_tp):
        """Método que realiza el despacho de un vehículo de pasajeros. Un
        vehículo de pasajeros, cada vez que es despachado, implica que su
        número de viajes de debe incrementar en una unidad

        Parameters
        ----------
        vehiculo_tp : VehiculoPasajeros
            El vehículo de pasajeros al cual se le incrementará su número de
            viajes

        Returns
        -------
        VehiculoPasajeros|None
            El vehículo de pasajeros al cual se le incrementó el número de
            viajes o None, cuando el vehículo de pasajeros no pertenece a la
            flota
        """
        
        if vehiculo_tp in self.vehiculos_registrados:
            vehiculo_tp.numero_de_viajes += 1
            return vehiculo_tp
        else:
            return None

    # Método ET # 4
    def mini_flota_marca(self, marca):
        """Este método crea una lista con todos los vehículos de pasajeros que
        pertenezcan a la flota y que sean de una determinada marca

            Parameters
        ----------
        marca : str
            El nombre de la marca a buscar en la flota

        Returns
        -------
        Lista Python
            Una lista con los vehículos de pasajeros que sean de la marca
            especificada y que pertenezcan actualmente a la flota
        """


        return [x for x in self.vehiculos_registrados if x.marca == marca]
        

    # Método ET # 5
    def desvincular_VP(self, vehiculo_tp):
        """Método que permite eliminar un vehículo de pasajeros de la flota
        actual de la empresa

        Parameters
        ----------
        vehiculo_tp : VehiculoPasajeros
            Es el vehículo de pasajeros que se desea desvincular de la empresa

        Returns
        -------
        bool
            True si el vehículo es desvinculado de la flota. False en caso
            contrario
        """
        if vehiculo_tp in self.vehiculos_registrados:
            self.vehiculos_registrados.remove(vehiculo_tp)
            return True
        else:
            return False
            

    # Método ET # 6
    def __len__(self):
        """Método que retorna el número de vehículos de pasajeros que se
        encuentran actualmente registrados en la flota de la empresa

        Returns
        -------
        int
            El número actual de vehículos que posee la flota de la empresa
        """
        numero = len(self.vehiculos_registrados)
        return numero

    # Método ET # 7
    def __str__(self):
        """Método que retorna la cadena de presentación de la empresa de
        transporte

        Returns
        -------
        str
            Una cadena de presentación en dos líneas de la empresa de
            transporte, utilizando el siguiente formato:
            "Empresa:nombre de empresa transporte/NIT:nit de la empresa
             Máx Vehículos:<número máximo de vehículos>"

            Por ejemplo:
            "Empresa:Team ACME/NIT:123
             Máx Vehículos:<5>"
        """
        return f"Empresa:{self.nombre}/NIT:{self.nit}\nMáx Vehículos:<{self.max_vehiculos}>"


    # Método ET # 8
    def la_flota(self):
        """Método que retorna una cadena con todos los vehículos de pasajeros
        pertenecientes a la flota de la empresa

        Returns
        -------
        str
            Una cadena con el siguiente formato:
            "{[presentación_vehículo_0] -> [presentación_vehículo_1] -> [presentación_vehículo_2] -> ... -> [presentación_vehículo_n]}"
            En caso de que la flota no tenga ningún vehículo registrado, se retornará:
            "{}"
        """

        presentacion = []

        if not self.vehiculos_registrados:
            return "{}"
        else:
            for vehiculo in self.vehiculos_registrados:
                presentacion.append(f"[{vehiculo.cod_registro}:{vehiculo.marca}:{vehiculo.capacidad_maxima}:{vehiculo.numero_de_viajes}]")

        for i in presentacion:
            if i >= 1 and i < len(presentacion):
                presentacion[i] = presentacion[i] + " -> "

        return "{".join(presentacion) + "}"

        

