from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="A webpage powered by GitHub Actions and created by Ashish Singh." />
  <meta name="author" content="Ashish Singh - Learning-DevOps-LLC" />
  <title>Ashish Singh | GitHub Actions</title>
  <link rel="icon" href="/static/favicon.ico" />
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      color: #333;
    }
    header, footer {
      background-color: #222;
      color: #fff;
      padding: 1em;
      text-align: center;
    }
    main {
      padding: 2em;
      text-align: center;
    }
    .org-name {
      margin-top: 1.5em;
      font-size: 1em;
      color: #555;
    }
    .dynamic-msg {
      margin-top: 1em;
      font-style: italic;
      color: #007acc;
    }
    .connects {
      margin-top: 2em;
    }
    .connects a {
      margin: 0 10px;
      text-decoration: none;
      color: #007acc;
      font-weight: bold;
    }
    .connects a:hover {
      text-decoration: underline;
    }
    .icon {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Jarvis - GitHub Actions</h1>
  </header>

  <main>
    <h2>Hello, Ashish Singh</h2>
    <div class="org-name">Organization: Learning-DevOps-LLC</div>
    <div class="dynamic-msg">{{ message }}</div>

    <div class="connects">
      <h3>Connect with me</h3>
      <a href="https://github.com/ASHISHs21" target="_blank" rel="noopener noreferrer">
        🔗 GitHub
      </a>
      <a href="https://www.linkedin.com/in/ashish-singh-874012195/" target="_blank" rel="noopener noreferrer">
        💼 LinkedIn
      </a>
      <a href="mailto:ksinghashish357@gmail.com">
        ✉️ Email
      </a>
      <a href="https://ashishs21.github.io/portfolio/" target="_blank" rel="noopener noreferrer">
        🌐 Portfolio
      </a>
    </div>
  </main>

  <footer>
    &copy; 2025 Ashish Singh | Powered by GitHub Actions
  </footer>
</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.now().strftime("Page loaded on %Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, message=current_time)

if __name__ == "__main__":
    app.run(debug=True)
