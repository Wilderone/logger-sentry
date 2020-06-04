import os
import random
import messages as m

from bottle import route, run


def generate_message():
    return "use api"


@route("/api/generate/")
def one_message():
    onem = m.Declar()
    return onem.return_declar()


@route("/api/generate/<num:int>")
def one_message(num):
    onem = m.Declar(num)
    return onem.return_declar()

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html




if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8085, debug=True)
