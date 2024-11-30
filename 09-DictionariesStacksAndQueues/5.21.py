import json
favorite_movie = {
    "title":"Openheimer",
    "origin":"USA",
    "release date":2018,
    "Colors":"Monochrome",
    "best movie": True
}
with open("favorite.json", "w", encoding="utf-8") as file:
    json.dump(favorite_movie, file)