from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)



@app.route('/users', methods=['GET'])
def index():
    users = User.get_all()
    print(users)
    return render_template('Read.html', all_users=users)



@app.route('/users/new', methods=['GET'])
def show():
    return render_template('Create.html')



@app.route('/create/user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)