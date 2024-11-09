import os
from werkzeug.middleware.profiler import ProfilerMiddleware
from app import create_app

profile_dir = 'tmp/profile'
os.makedirs(profile_dir, exist_ok=True)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[25], profile_dir=profile_dir)

if __name__ == "__main__":
    app.run(debug=False)