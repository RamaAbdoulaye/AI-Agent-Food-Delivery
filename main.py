from flask import Flask
from agent.route import bp as agent_bp

app = Flask(__name__)
app.register_blueprint(agent_bp)

if __name__ == "__main__":
    app.run(debug=True)
