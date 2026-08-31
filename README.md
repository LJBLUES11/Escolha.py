# adivinha.py 🎯

Um jogo simples de "Adivinhe o Número", reescrito do zero em **Python + Django**, rodando em uma página web. O projeto nasceu de um trabalho acadêmico e é a evolução de um projeto anterior em Flask (chamado `pychoice`), migrado para Django com toda a exibição das informações feita no front-end.

O computador escolhe um número secreto entre **1 e 10** e o jogador tenta adivinhar. Cada tentativa é registrada em um terminal simulado na tela, e os melhores resultados (menor número de tentativas) entram em um ranking.

---

## 📋 Sumário

- [Como o jogo funciona](#-como-o-jogo-funciona)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como rodar o projeto](#-como-rodar-o-projeto)
- [Jogando](#-jogando)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)

---

## 🎮 Como o jogo funciona

Como uma página web não tem um `while` de verdade (como teria um script rodando no terminal), cada palpite chega como uma requisição `POST` separada. Por isso, o estado da partida — nome do jogador, número secreto e quantidade de tentativas — fica salvo na **sessão** do Django entre uma jogada e outra.

O fluxo é o seguinte:

1. O jogador digita o próprio nome.
2. O sistema sorteia um número entre 1 e 10 e guarda esse número na sessão.
3. A cada palpite enviado, o sistema compara com o número secreto e responde se é maior, menor, ou se o jogador acertou.
4. Ao acertar, o resultado (nome + número de tentativas) é salvo no banco de dados e aparece no ranking dos 10 melhores.
5. O jogador pode jogar novamente ou reiniciar a sessão a qualquer momento.

---

## 🗂️ Estrutura do projeto

```
Escolha.py-main/
├── manage.py                  # utilitário de linha de comando do Django
├── requirements.txt           # dependências do projeto
├── db.sqlite3                 # banco de dados (SQLite)
├── projeto/                   # configurações principais do Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── game/                      # app responsável pelo jogo
    ├── views.py                # laço do jogo e validação do palpite (via sessão)
    ├── models.py                # tabela `Jogador`, via ORM do Django
    ├── urls.py                  # rotas do jogo e de reinício de partida
    ├── admin.py
    ├── static/
    │   └── index.css            # estilos da página
    └── templates/game/
        └── index.html           # página do jogo (terminal + ranking)
```

| Arquivo | Responsabilidade |
|---|---|
| `views.py` | Laço do jogo e validação do palpite, guardados na sessão |
| `models.py` | Tabela de jogadores, via ORM do Django |
| `urls.py` | Rotas do jogo e de reinício de partida |
| `templates/game/index.html` | Página exibida ao usuário |

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.10+** (recomendado)
- **pip** (gerenciador de pacotes do Python)
- Git (opcional, apenas para clonar o repositório)

Para verificar se o Python e o pip estão instalados, rode:

```bash
python --version
pip --version
```

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório (ou baixe o .zip)

```bash
git clone https://github.com/seu-usuario/Escolha.py.git
cd Escolha.py-main
```

### 2. Crie um ambiente virtual (venv)

Dentro da pasta do projeto, crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows (cmd):**
  ```bash
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```bash
  venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

Quando o ambiente estiver ativado, você verá `(venv)` no início da linha do terminal.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Isso vai instalar:

- `Django` — o framework web
- `asgiref` — suporte assíncrono usado internamente pelo Django
- `sqlparse` — usado pelo Django para formatar SQL
- `tzdata` — dados de fuso horário
- `python-dotenv` — carregamento de variáveis de ambiente (`.env`)

### 4. Aplique as migrações do banco de dados (recomendado)

Embora o projeto já venha com um `db.sqlite3`, é uma boa prática garantir que as tabelas estejam atualizadas:

```bash
python manage.py migrate
```

### 5. Inicie o servidor do Django

```bash
python manage.py runserver
```

Se tudo ocorrer certo, você verá uma mensagem parecida com esta no terminal:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 6. Acesse o jogo

Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

---

## 🕹️ Jogando

1. Ao abrir a página, role até a seção **Game**.
2. Digite seu nome e envie.
3. O sistema pensa em um número entre 1 e 10.
4. Digite um número e envie — o terminal vai te dizer se o número secreto é maior, menor, ou se você acertou.
5. Ao acertar, sua pontuação (número de tentativas) entra no ranking dos 10 melhores jogadores.
6. Use o botão de reiniciar para zerar a sessão e começar do zero a qualquer momento.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Django** — backend, views, sessões e ORM
- **SQLite** — banco de dados padrão do Django, usado para guardar o ranking de jogadores
- **HTML/CSS** — front-end da página (terminal simulado + ranking)

---

## 📌 Observações

- O projeto está configurado com `DEBUG = True`, ou seja, é voltado para **ambiente de desenvolvimento/estudo**, não para produção.
- O ranking é armazenado em cache por 5 minutos para reduzir consultas ao banco de dados a cada carregamento da página.
- Este projeto tem fins **acadêmicos/demonstrativos**.
- 
- Obrigado por ter visitado meu Repositório, ass:LJBLUES
