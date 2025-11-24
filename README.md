# mikrotik-bandwidth-monitor-web

## 🎯 Objetivo

Este repositório contém o código-fonte de uma Interface Web de Monitoramento de Tráfego de Rede para roteadores Mikrotik.

## 📁 Estrutura de Pastas e Arquivos 

```
mikrotik-bandwidth-monitor-web/
├── app.py                      # Servidor Flask principal
├── config.py                   # Configurações e variáveis de ambiente
├── requirements.txt            # Dependências Python
├── .env                        # Variáveis de ambiente (CREDENCIAIS)
├── static/                     # Arquivos estáticos
│   ├── css/
│   │   └── style.css           # Estilos da interface
│   └── js/
│       └── script.js           # Lógica frontend e gráficos
├── templates/                  # Templates HTML
│   └── index.html              # Interface principal
└── README.md                   # Documentação
```

## 💻 Tecnologias Utilizadas

### 🌐 Frontend & Visualização

- HTML5/CSS3: Estrutura e estilização
- JavaScript (ES6+): Lógica do cliente
- Chart.js: Gráficos dinâmicos em tempo real
- CSS Responsivo: Adaptação para diferentes telas

### ⚙️ Backend & Tempo Real

- Python 3.13: Linguagem principal
- Flask: Framework web
- RouterOS API: Comunicação com Mikrotik
- HTTP Polling: Comunicação em tempo real (alternativa a WebSockets)

### Dependências

Antes de rodar baixe:
- Python 3.8+
- Roteador Mikrotik com API habilitada
- Acesso às credenciais do Mikrotik

Instalação das dependências:
  pip install -r requirements.txt


### Configuração das Credenciais
- Edite o arquivo .env:

-- Configurações de Segurança
FLASK_SECRET_KEY="sua_chave_secreta_aqui"
--Credenciais Mikrotik
MIKROTIK_HOST="seu_host"
MIKROTIK_USER="seu_usuario"
MIKROTIK_PASSWORD="sua_senha"
INTERFACE_TO_MONITOR="sua_interface"

### 🔬 Teste de Funcionamento e Comprovação

Esta seção demonstra como comprovar a funcionalidade em tempo real da interface web, atendendo ao requisito de apresentação.

- Pré-requisito
Certifique-se de que a aplicação Python (app.py) esteja rodando e que o navegador esteja aberto em http://127.0.0.1:5000/.

- Passo a Passo do Teste
1. Acesse o Mikrotik: Use o Winbox e conecte-se ao seu roteador virtual (MIKROTIK_HOST).

2. Abra o Bandwidth Test: No Winbox, navegue até Tools (Ferramentas) → Bandwidth Test.

3. Configurar o Teste:

- Interface: A interface que você está monitorando (ex: ether2 ou bridge-local).

- Protocol: Use TCP (recomendado para gerar tráfego constante).

- Direction: Escolha both (ambos: RX e TX) para simular tráfego de subida e descida.

- User/Password: Deixe em branco, ou use credenciais de teste.

- Iniciar o Teste de Tráfego: Clique em Start no Winbox.

Observação da Interface:

- Imediatamente, observe a interface web aberta no seu navegador.

- O gráfico de linha (trafficChart) deve registrar um pico nos dados de RX e TX.

- Os valores numéricos sob o gráfico (RX (Download) e TX (Upload)) devem exibir as taxas de transferência em KB/s ou MB/s.

- Parar o Teste: Clique em Stop no Winbox.

Comprovação: Após interromper o teste, o gráfico deve retornar rapidamente aos níveis de tráfego de baseline (próximo de zero), comprovando a comunicação contínua e em tempo real com o roteador.

## 👥 Equipe

**Este projeto foi desenvolvido por:**

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/alanaagne">
        <img src="https://avatars.githubusercontent.com/u/141842450?v=4" width="100px;" alt="Alana Ágne Brandao Rocha"/>
        <br/>
        <sub><b></b>Alana Ágne Brandao Rocha</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Erica1110">
        <img src="https://avatars.githubusercontent.com/u/89529255?v=4" width="100px;" alt="Erica Meire Prates Ferreira"/>
        <br/>
        <sub><b></b>Erica Meire Prates Ferreira</sub>
      </a>
    </td>