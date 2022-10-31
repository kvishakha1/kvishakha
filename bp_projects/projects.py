from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html

@app_projects.route('/hangman/')
def hangman():
    return render_template("FinalProject.html")