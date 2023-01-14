# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Ananya Kannan" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Natarajan Kannan"
    age = "53"
    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Subashini Kannan"
    age = ""
    return render_template("mother.html", name = name, age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "ishwarya Gowrishankar"
    age = "16"
    return render_template("friend.html", name = name, age = age)

@app.route("/friend1")
def friend1():
    name = "Krishnaharini"
    age = "16"
    return render_template("friend1.html", name = name, age = age)


@app.route("/friend2")
def friend2():
    name = "Harinie Chandrashekar"
    age = "16"
    return render_template("friend1.html", name = name, age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
