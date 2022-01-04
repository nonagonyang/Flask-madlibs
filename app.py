
from flask import Flask, request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint,choice,sample
from stories import Story
# get a server up and running
app= Flask(__name__)
app.config["SECRET_KEY"]="maomijing"
debug=DebugToolbarExtension(app)

 
@app.route("/form")
def show_form():
    return render_template("form.html")

@app.route("/story")
def show_story():
    place=request.args["place"]
    noun=request.args["noun"]
    verb=request.args["verb"]
    adjective=request.args["adjective"]
    plural_noun=request.args["plural_noun"]
    color=request.args["color"]
    prompts= [place, noun, verb, adjective, plural_noun, color]
    template_txt="""Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} the {color} {plural_noun}."""
    story=Story(prompts,template_txt)
    return render_template("story.html", story=story)
