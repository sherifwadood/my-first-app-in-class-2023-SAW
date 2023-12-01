# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    # Uncomment the line below to return a simple message instead of rendering a template
    # return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    # Uncomment the line below to return a simple message instead of rendering a template
    # return "About Me"
    return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) # can be empty like {} or full of params like {"name":"Harper"}
    name = url_params.get("name") or "World"
    message = f"Hello, {name}!"

    # Uncomment the line below to return a simple message instead of rendering a template
    # return message
    return render_template("hello.html", message=message)

