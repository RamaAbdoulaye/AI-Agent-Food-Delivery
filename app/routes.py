from flask import Blueprint, request, jsonify
import json
import os

bp = Blueprint('agent', __name__)

DATA_PATH = os.path.join("data", "commandes.json")

# Charger les commandes depuis le fichier


def load_commandes():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# Sauvegarder les commandes dans le fichier


def save_commandes(commandes):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(commandes, f, indent=4)

# Route POST pour ajouter une commande


@bp.route("/ajouter", methods=["POST"])
def ajouter_commande():
    data = request.get_json()
    commandes = load_commandes()
    commandes.append(data)
    save_commandes(commandes)
    return jsonify({
        "message": "Commande ajoutée avec succès",
        "commande": data
    }), 201


# Route GET pour voir toutes les commandes


@bp.route("/commandes", methods=["GET"])
def afficher_commandes():
    commandes = load_commandes()
    return jsonify(commandes), 200
