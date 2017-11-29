from project import db
from project.models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("start", "start", "start", "Asdf23rx", 1))

'''
# for local
db.session.add(BlogPost(1, 1, 1, 12))
db.session.add(BlogPost(1, 1, 2, 13))
'''

# commit the changes
db.session.commit()
