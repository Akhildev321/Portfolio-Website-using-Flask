from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f"\n📥 New Contact Message:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}\n")

    flash("Message sent successfully! Thank you for reaching out!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
