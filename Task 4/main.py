# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        return self.budget > 100000000

shawshank_redemption = Movie("The Shawshank Redemption", "Frank Darabont", 25000000)

interstellar = Movie("Interstellar", "Christopher Nolan", 165000000)

shawshank_redemption_expensive = shawshank_redemption.was_expensive()

print(f"Was The Shawshank Redemption expensive? {shawshank_redemption_expensive}")

interstellar_expensive = interstellar.was_expensive()

print(f"Was Interstellar expensive? {interstellar_expensive}")
