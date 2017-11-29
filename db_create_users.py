from project import db
from project.models import User

db.create_all()

#insert data
db.session.add(User("admin"))
#db.session.add(User("admin", "ad@min.com", "admin"))

#commit changes
db.session.commit() 