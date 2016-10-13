from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='electronic_phone_book')
app = Flask('Phone_book_app')
@app.route('/')
def home_page_render():
    query = db.query('select * from phonebook')

    return render_template(
        'index.html',
        title = 'Phonebook entry page',
        name_list=query.namedresult()
    )

@app.route('/new_entry')
# def new_entry():
def form_render():
    return render_template(
        'new_entry.html',
        title='Your magic phonebook database'
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

@app.route('/update_entry')
# def new_entry():
def update_form_render():
    entry_id = request.args.get('id')
    phonebook_list = db.query("select * from phonebook where id = '%s'" % entry_id)
    return render_template(
        'update_entry.html',
        title='Update an entry',
        phonebook = phonebook_list.namedresult()[0]
    )

@app.route('/submit_update_entry', methods=['POST'])
def update_submit_form():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    entry_id = request.form.get('id')
    button = request.form.get('action')
    if button == "1":
        db.update(
            'phonebook',
            id = entry_id,
            name=name,
            phone_number=phone_number,
            email=email)
        return redirect('/')
    elif button == '2':
        db.delete(
            'phonebook',
            id = entry_id,
            name=name,
            phone_number=phone_number,
            email=email)
        return redirect('/')
    else:
        pass    

if __name__ == '__main__':
    app.run(debug=True)
