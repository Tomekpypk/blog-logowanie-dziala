import unittest
from flask_testing import TestCase
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm

class TestBlog(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_entry_form_and_model(self):
        with self.app.app_context():
            form = EntryForm()
            entry = Entry(title="Test Title", body="Test Body", is_published=True)
            db.session.add(entry)
            db.session.commit()

            retrieved_entry = Entry.query.filter_by(title="Test Title").first()

            self.assertEqual(form.__class__.__name__, 'EntryForm')
            self.assertEqual(entry.title, "Test Title")
            self.assertEqual(retrieved_entry.body, "Test Body")
            self.assertTrue(retrieved_entry.is_published)

if __name__ == '__main__':
    unittest.main()
