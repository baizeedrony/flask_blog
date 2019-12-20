from flask import Flask,render_template,url_for

app = Flask(__name__)

posts=[
    {
        'author': 'Baizeed Hossain Rony',
        'title': '1st blog',
        'content': 'first post content',
        'date_posted': '20 december,2019'
    },

{
        'author': 'Espi putul',
        'title': '2nd blog',
        'content': '2nd post content',
        'date_posted': '21 december,2019'
    }
]


@app.route('/')
def home():
    return render_template('home.html', vpost=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__=='__main__':
    app.run(debug=True)