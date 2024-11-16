from flask import Flask, render_template

app = Flask(__name__)

# Mock data for students in the "HPCAP" course
students = [
    {"name": "Chaitali Ingale", "prn": "240840141007"},
    {"name": "Atharv Ganer", "prn": "240840141004"},
    {"name": "Apurva Jadhav", "prn": "240840141099"}
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)
