from website import create_app
import os

app = create_app()

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'production' or os.path.exists('/.dockerenv'):
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(debug=True, host='0.0.0.0', port=80)