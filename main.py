from pokedex import Database
from salva_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

#primeira funcao - pokemon id 10
def getPokemonById(number: int):
    return db.collection.find({"id": number})

pokemonId = getPokemonById(10)
writeAJson(pokemonId, "PesquisaPokemon10")

#retornando pokemons com ataque menor que 40
attack = db.collection.find({"base.Attack": {"$lte": 40}})
writeAJson(attack, "Ataque_menor_40")

#retornando pokemon com o nome que possui 7 letras ou mais em frances
def get_7_letters_or_less(collection):
  names = collection.find({}, {"name.french": 1})
  seven_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 7:
      if all(len(word) <= 7 for word in name["name"].values()):
        seven_letters_or_less.append(name["name"].values())
  return seven_letters_or_less

writeAJson(get_7_letters_or_less(db.collection), "pokemon_7_words_or_more_in_french")

#retornando pokemons do tipo fogo
tipo_fogo = db.collection.find({"type": "Fire"})
writeAJson(tipo_fogo, "pokemon_Fire")

#retornando do tipo agua e defesa
tipo_defesa = db.collection.find({"type": "Water", "base.Defese": { "$lte": 110 }})
writeAJson(tipo_defesa, "pokemon_water_defese_110")