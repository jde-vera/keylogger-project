from app import create_app, db
from app.models import User

app = create_app

with app.app_context():
    db.create_all()

    if User.query.count == 0:
        admin = User(username='admin')
        admin.set_password('admin')

        john = User(username='john')
        john.set_password('smith123')

        jane = User(username='jane')
        jane.set_password('doe123')

        db.session.add_all([admin,john,jane])
        db.session.commit()