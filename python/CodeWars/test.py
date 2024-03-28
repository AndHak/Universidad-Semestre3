class User():
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if isinstance(rank, list):  # Si rank es una lista
            for r in rank:
                self.inc_progress(r)  # Llama a inc_progress para cada elemento de la lista
        else:
            if rank not in range(-8, 9) or rank == 0:
                raise ValueError("Invalid activity rank")

            rank_difference = rank - self.rank

            if rank_difference == 0:
                self.progress += 3
            elif rank_difference == -1:
                self.progress += 1
            elif rank_difference > 0:
                self.progress += 10 * rank_difference * rank_difference

            while self.progress >= 100:
                if self.rank == -1:
                    self.rank += 2
                else:
                    self.rank += 1
                if self.rank == 0:
                    self.rank = 1
                self.progress -= 100

            if self.rank == 8:
                self.progress = 0


# Ejemplo de uso
user = User()
user.inc_progress([1, 1])

print(user.rank)  # Salida esperada: -2
print(user.progress)  # Salida esperada: 40
