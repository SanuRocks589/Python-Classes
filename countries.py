class USA():
    def capital(self):
        print("The capital of USA is Washington DC.")
    def language(self):
        print("The language spoke in US is English.")
    def food(self):
        print("The most common food eaten in USA is bread and eggs.")

class India():
    def capital(self):
        print("The capital of India is Delhi.")
    def language(self):
        print("Language spoken in India is Hindi.")
    def food(self):
        print("The most commonly eaten food in India is roti, lentils, and rice.")

obj = India()
ob = USA()

for country in (obj, ob):
    country.capital()
    country.language()
    country.food()