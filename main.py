from website import create_app

app = create_app()
print("Start")
if __name__ == '__main__':
    app.run(debug=False , host = '0.0.0.0' , port = 80)
