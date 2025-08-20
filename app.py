from flask import Flask, render_template, request, Markup
from rendergit_core import render_repo_to_html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    html_result = None
    error = None
    repo_url = ''
    if request.method == 'POST':
        repo_url = request.form.get('repo_url', '').strip()
        if not repo_url:
            error = 'Please enter a GitHub repository URL.'
        else:
            try:
                html_result = render_repo_to_html(repo_url)
            except Exception as e:
                error = f'Error: {e}'
    return render_template('index.html', html_result=Markup(html_result) if html_result else None, error=error, repo_url=repo_url)

if __name__ == '__main__':
    app.run(debug=True)
