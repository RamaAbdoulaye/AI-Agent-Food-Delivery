import json
import os

DATA_FILE = os.path.join("data", "memory.json")

def load_memory():
    """Chargeons les données depuis le fichier JSON."""
    if not os.path.exists(DATA_FILE):

        return []

    with open(DATA_FILE, 'r', encoding='utf-8') as file:

        try:

            return json.load(file)

        except json.JSONDecodeError:
            return []


def save_memory(data):

    """Sauvegardons les données dans le fichier JSON."""

    with open(DATA_FILE, 'w', encoding='utf-8') as file:

        json.dump(data, file, indent=4, ensure_ascii=False)


def add_order(order):

    """Ajoutons une commande à la mémoire existante."""

    memory = load_memory()

    memory.append(order)

    save_memory(memory)