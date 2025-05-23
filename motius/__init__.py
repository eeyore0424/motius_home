from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_motius():
        return render_template('index.html')
    
    @app.route('/terms')
    def terms():
        return render_template('terms.html')
    
    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html')
    
    # @app.route('/static/<path:filename>')
    # def static_file(filename):
    #     return send_from_directory('static', filename)
    
    return app