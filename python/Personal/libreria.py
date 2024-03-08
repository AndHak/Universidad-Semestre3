class Libro:
    """Clase para representar un libro."""
    
    def __init__(self, titulo, autor, ISBN):
        """
        Inicializa un libro con un título, autor e ISBN.

        Parámetros:
        - titulo (str): El título del libro.
        - autor (str): El autor del libro.
        - ISBN (str): El ISBN (Número Estándar Internacional del Libro) del libro.
        """
        # Tu código aquí
        self.titulo = titulo
        self.autor = autor
        self.isbn = ISBN

    def __repr__(self):
        """
        Devuelve una representación en cadena del libro.

        Devoluciones:
        str: Una cadena en el formato "[Título] de Autor (ISBN: XXX)"
        """
        # Tu código aquí
        return f"[{self.titulo}] de {self.autor} (ISBN: {self.isbn})"

class Biblioteca:
    """Clase para representar una biblioteca."""
    
    def __init__(self, nombre, max_libros):
        """
        Inicializa una biblioteca con un nombre y un número máximo de libros.

        Parámetros:
        - nombre (str): El nombre de la biblioteca.
        - max_libros (int): El número máximo de libros que la biblioteca puede contener.
        """
        # Tu código aquí
        self.nombre = nombre
        self.max_lbros = max_libros
        self.biblioteca = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.

        Parámetros:
        - libro (Libro): El libro que se agregará.

        Devoluciones:
        bool: True si el libro se agregó con éxito, False en caso contrario.
        """
        # Tu código aquí
        for i in self.biblioteca:
            if i.isbn == libro.isbn:
                return False
        self.biblioteca.append(libro)
        return True

    def eliminar_libro(self, ISBN):
        """
        Elimina un libro de la biblioteca basándose en su ISBN.

        Parámetros:
        - ISBN (str): El ISBN del libro que se eliminará.

        Devoluciones:
        bool: True si el libro se eliminó con éxito, False en caso contrario.
        """
        # Tu código aquí
        for i in self.biblioteca:
            if i.isbn == ISBN:
                self.biblioteca.remove(i)
                return True
        return False

    def buscar_libros_por_autor(self, autor):
        """
        Busca libros de un autor específico.

        Parámetros:
        - autor (str): El autor que se buscará.

        Devoluciones:
        list: Una lista de libros del autor especificado.
        """
        # Tu código aquí
        return [x for x in self.biblioteca if x.autor == autor]

    def __len__(self):
        """
        Devuelve el número actual de libros en la biblioteca.

        Devoluciones:
        int: El número de libros en la biblioteca.
        """
        # Tu código aquí
        return len(self.biblioteca)


# Pruebas
libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
libro2 = Libro("Matar a un ruiseñor", "Harper Lee", "978-0-06-112008-4")
libro3 = Libro("1984", "George Orwell", "978-0-452-28423-4")

biblioteca = Biblioteca("Biblioteca Municipal", 2)

assert biblioteca.agregar_libro(libro1) == True
assert biblioteca.agregar_libro(libro2) == True
assert biblioteca.agregar_libro(libro3) == False  # La biblioteca está llena

assert len(biblioteca) == 2

assert biblioteca.eliminar_libro("978-0-7432-7356-5") == True
assert biblioteca.eliminar_libro("978-0-7432-7356-5") == False  # El libro no está en la biblioteca

assert len(biblioteca) == 1

assert biblioteca.buscar_libros_por_autor("Harper Lee") == [libro2]
assert biblioteca.buscar_libros_por_autor("George Orwell") == []

print("¡Todas las pruebas pasaron!")
