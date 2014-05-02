from flask import Flask, render_template, request, redirect, flash, url_for, abort

from flask_debugtoolbar import DebugToolbarExtension

import config_combined

def app_factory(**kwargs):
    app = Flask(__name__)
    app.config.from_object(config_combined)

    @app.route('/')
    def index():
        return 'Hello World'

    return app
