from flaskr import create_app
import os

app = create_app()

PORT = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
