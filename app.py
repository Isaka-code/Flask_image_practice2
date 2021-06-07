from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("extend.html", title="Flask")

if __name__ == "__main__":
    app.run()