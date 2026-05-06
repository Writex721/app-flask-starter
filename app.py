from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.args.get("name")
	surname=request.args.get("surname")

	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["POST", "GET"])
def pozdrav_post():
	check=True
	zprava_jmeno="jmeno splňuje požadavky"
	zprava="Uhodl jsi heslo!"
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name = request.form.get("name")
	surname = request.form.get("surname")
	password = request.form.get("password")


	if not name:
		zprava_jmeno="Error - nelze nezadat jméno"
		check=False

	elif len(name) > 50:
		zprava_jmeno="Error - jméno je příliš dlouhé"
		check=False


	
	if password == "tajneheslo" and check==True:
		zprava="Uhodl jsi heslo!"

	else:
		zprava="Error - špatné heslo"
		

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, zprava=zprava, zprava_jmeno=zprava_jmeno)

if __name__=="__main__":
	app.run(debug=True)