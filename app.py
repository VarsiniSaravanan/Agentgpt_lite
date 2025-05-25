from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello This is Project AgentGPT_lite!"

if __name__ == '__main__':
    app.run(debug=True)
