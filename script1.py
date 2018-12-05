from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    ip = request.remote_addr
    inputName = inputName.upper()+" hi!  Visiting from" + str(ip)
    return render_template("home.html",myName=inputName)

@app.route('/')
def index():
session['number'] = random.randrange(1,50)
print session['number']
return render_template("home.html")

@app.route('/guess', methods=['POST'])
def result():
if request.form['guess'] == session['number']:
    answer = "Good job! You guessed the number in " + numberofGuesses + " tries :)"
    return render_template("home.html", answer=answer)
elif int(request.form['guess']) < session['number']:
    answer = "Your guess is too low! You have " + guessesLeft + " guesses left"
    return render_template("home.html", answer=answer)
else:
    answer = "Your guess is too high! You have " + guessesLeft + " guesses left"
      return render_template("index.html", answer=answer)

@app.route('/')
def home():
    
    return render_template("home.html",myName="")



if __name__=="__main__":
    app.run(debug=True)

