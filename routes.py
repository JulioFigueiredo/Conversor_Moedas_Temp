from flask import render_template, request
from forms import Temperature

def configure_routes(app):
    app.secret_key = 'secret'
    
    @app.route('/')
    def index():
        return render_template('index.html')
        
    @app.route("/temperature", methods=["GET", "POST"])    
    def temperature_conversor():
        form = Temperature()
        if form.validate_on_submit():
            value = form.value.data
            type = form.type.data
            
            if type == 'c_to_f':
                result = (value * 9/5) + 32
            else:
                result = (value - 32) * 5/9
                
            return render_template('temperature_conversor.html', form=form, result=result)
        
        return render_template('temperature_conversor.html', form=form)