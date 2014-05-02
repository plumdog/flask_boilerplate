from flask import Flask, render_template, request, redirect, flash, url_for, abort

from flask_debugtoolbar import DebugToolbarExtension

import config_combined

def app_factory(**kwargs):
    app = Flask(__name__)
    app.config.from_object(config_combined)
    DebugToolbarExtension(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def err404(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def err500(e):
        return render_template('500.html'), 500

    return app
