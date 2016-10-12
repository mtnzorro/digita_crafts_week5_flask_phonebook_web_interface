from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='electronic_phone_book')
app = Flask('Phone_book_app')
@app.route('/')
def home_page_render():
    query = db.query('select * from phonebook')

    return render_template(
        'index.html',
        name_list=query.namedresult()
    )

@app.route('/new_entry')
# def new_entry():
def form_render():
    return render_template(
        'new_entry.html',
    )

@app.route('/submit_new_entry', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    db.insert(
        'phonebook',
        name=name,
        phone_number=phone_number,
        email=email)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
