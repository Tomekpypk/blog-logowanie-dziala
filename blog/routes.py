from flask import render_template, request, redirect, session, flash, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
#from werkzeug.exceptions import ValidationError

@app.route("/")
def index():
    # Zmieniłem ten fragment kodu na zapytanie, które pobiera wszystkie wpisy
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc()).all()
    return render_template("homepage.html", all_posts=all_posts)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
            db.session.commit()  # Dodane zatwierdzenie sesji
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)

@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash('You are now logged in.', 'success')
           return redirect(next_url or url_for('index'))
       else:
        errors = form.errors
        raise ValidationError("Invalid password")
   return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('You are now logged out.', 'success')
   return redirect(url_for('index'))