from flask import Flask, render_template_string
import time

app = Flask(__name__)

# HTML básico para teste
HTML_BASICO = '''
<!DOCTYPE html>
<html>
<head>
    <title>Teste Mikrotik</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>🚀 TESTE FUNCIONANDO!</h1>
    <canvas id="meuGrafico" width="400" height="200"></canvas>
    <script>
        console.log("✅ JavaScript carregado!");
        const ctx = document.getElementById('meuGrafico').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fev', 'Mar'],
                datasets: [{
                    label: 'Teste',
                    data: [10, 20, 30],
                    borderColor: 'blue'
                }]
            }
        });
        console.log("✅ Gráfico criado!");
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_BASICO)

if __name__ == '__main__':
    print("🌐 Servidor teste rodando em http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)