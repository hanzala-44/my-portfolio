from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Email configuration (optional - for contact form)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'E-Commerce Platform',
            'description': 'Full-stack e-commerce solution with payment integration',
            'technologies': ['Python', 'Flask', 'PostgreSQL', 'Stripe'],
            'github': 'https://github.com/yourusername/project1',
            'demo': 'https://demo.com'
        },
        {
            'title': 'Task Management App',
            'description': 'Real-time collaborative task management system',
            'technologies': ['React', 'Node.js', 'MongoDB', 'Socket.io'],
            'github': 'https://github.com/yourusername/project2',
            'demo': 'https://demo.com'
        },
        {
            'title': 'Data Analytics Dashboard',
            'description': 'Interactive dashboard for business intelligence',
            'technologies': ['Python', 'Dash', 'Pandas', 'Plotly'],
            'github': 'https://github.com/yourusername/project3',
            'demo': 'https://demo.com'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields', 'error')
            return redirect(url_for('contact'))
        
        # Send email (requires email configuration)
        try:
            msg = Message('Portfolio Contact Form Submission',
                        sender=app.config['MAIL_USERNAME'],
                        recipients=['your-email@example.com'])
            msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)
            flash('Thank you for your message! I will get back to you soon.', 'success')
        except:
            flash('Message sent! (Email not configured yet)', 'success')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)