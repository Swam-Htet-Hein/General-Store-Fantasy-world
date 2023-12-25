from random import *
topics = [
    "Weather is fine today, Sir",
    "Prices are increasing these days",
    "I'm very happy to live here, it's peaceful",
    "The king is kind to all",
    "Do you know about gunpowder, it's very powerful in combat",
    "I prefer swords than firearms"
]

def talk_topic():
    print(f"\"{choice(topics)}\"")