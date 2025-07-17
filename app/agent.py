from app.menu import get_menu


class FoodAgent:
    def __init__(self):
        self.menu = get_menu()

    def ask(self, question):
        question = question.lower()
        if "menu" in question:
            return "Menu :" + ",".join(item["name"] for item in self.menu)
        elif "recommande" in question or "conseilles" in question:
            return "Je recommande notre spécialité: Sushi Box !"
        else:
            return "Je suis désolé, je ne comprends pas votre demande."
