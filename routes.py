from flask import render_template, request

def configure_routes(app):
    
    @app.route('/')
    def index():
        render_template('index.html')
        
    @app.route("/", methods=["GET", "POST"])    
    def conversor_temperatura():
        pass