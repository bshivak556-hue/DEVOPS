from flask import Flask, request, render_template_string
app = Flask(__name__)
PAGE = """<!doctype html><html lang='en'><head><title>My Containerized Application</title></head>
<body><h1>Registration demo</h1><form method='post'>
<label>Name <input name='name' required></label>
<label>Email <input name='email' type='email' required></label>
<button name='submit' type='submit'>Submit</button></form>
{% if result %}<p id='result'>{{ result }}</p>{% endif %}</body></html>"""
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        if name and email:
            result = "Form submitted successfully!"
    return render_template_string(PAGE, result=result)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)