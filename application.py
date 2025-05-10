from flask import Flask, request, render_template

application = Flask(__name__)  # EB looks for 'application'

@application.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        # In production, store this in a database
        return f"Received: {user_input}"
    return render_template("form.html")  # Make sure templates/form.html exists

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
