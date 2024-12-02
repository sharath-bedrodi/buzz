from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Secret key for session management (for flashing messages)

# Simulated users (In a real app, you should use a database)
users = {
    'test@example.com': 'password123',
    'admin@example.com': 'adminpassword'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if email exists and if password matches
        if email in users and users[email] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if password and confirm password match
        if password != confirm_password:
            flash("Passwords don't match. Please try again.", 'error')
            return redirect(url_for('signup'))

        # Check if the email already exists
        if email in users:
            flash("Email already registered. Please log in.", 'error')
            return redirect(url_for('login'))

        # Simulate adding the user to the database
        users[email] = password
        flash("Account created successfully! Please log in.", 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
