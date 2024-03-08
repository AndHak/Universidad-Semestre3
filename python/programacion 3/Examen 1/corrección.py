"""
    PROJECT: Evaluación 1 / Grupo 2

    MODULE: empresa_transporte.py

    DESCRIPTION:
    Construir un programa que permita administrar los vehículos de pasajeros
    que se encuentran adscritos a una Empresa de Transporte

    AUTHOR: Andrés Felipe Martínez Guerra
"""


class VehiculoPasajeros:
    def __init__(self, numero_registro, marca, capacidad_maxima=10):
        self.numero_registro = numero_registro
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima
        self.numero_viajes = 0

    def __eq__(self, otro_vp):
        return (
            self.numero_registro == otro_vp.numero_registro
            and self.marca == otro_vp.marca
            and self.capacidad_maxima == otro_vp.capacidad_maxima
        )

    def __repr__(self):
        return f"[{self.numero_registro}:{self.marca}:{self.capacidad_maxima}:{self.numero_viajes}]"

     


class EmpresaTransporte:
    def __init__(self, nit, nombre, max_vehiculos):
        self.nit = nit
        self.nombre = nombre
        self.max_vehiculos = max_vehiculos
        self.flota = []

    def vincular_VP(self, nuevo_vp):
        if len(self.flota) < self.max_vehiculos and nuevo_vp not in self.flota:
            registro_basico, digito_verificacion = map(int, nuevo_vp.numero_registro.split('-'))
            if sum(map(int, str(registro_basico))) % 10 == digito_verificacion:
                self.flota.append(nuevo_vp)
                return True
        return False

    def posicionar_VP(self, nuevo_vp, pos):
        if len(self.flota) < self.max_vehiculos and nuevo_vp not in self.flota and pos < self.max_vehiculos:
            registro_basico, digito_verificacion = map(int, nuevo_vp.numero_registro.split('-'))
            if sum(map(int, str(registro_basico))) % 10 == digito_verificacion:
                self.flota.insert(pos, nuevo_vp)
                return True
        return False

    def despachar_VP(self, vehiculo_tp):
        if vehiculo_tp in self.flota:
            vehiculo_tp.numero_viajes += 1
            return vehiculo_tp
        return None

    def mini_flota_marca(self, marca):
        return [vp for vp in self.flota if vp.marca == marca]

    def desvincular_VP(self, vehiculo_tp):
        if vehiculo_tp in self.flota:
            self.flota.remove(vehiculo_tp)
            return True
        return False

    def __len__(self):
        return len(self.flota)

    def __str__(self):
        return f"Empresa:{self.nombre}/NIT:{self.nit}\nMáx Vehículos:{self.max_vehiculos}"

    def la_flota(self):
        if self.flota:
            return "{" + " -> ".join(str(vp) for vp in self.flota) + "}"
        else:
            return "{}"
