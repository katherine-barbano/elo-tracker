from flask import current_app as app

class Member_of:
    
    def __init__(self, l_id, user_id, status):
        self.l_id = l_id
        self.user_id = user_id
        self.status = status

    @staticmethod
    def get_all():
        rows = app.db.execute('''
SELECT name, email, status
FROM Member_of
''')
        return [Member_of(*row) for row in rows]


    @staticmethod # get the leagues the logged in user is a member of.
    def get_user_leagues(email):
        rows = app.db.execute('''
SELECT name, email, status
FROM Member_of
WHERE email = :email
''', email = email)
        return [row for row in rows]

    # add a new Member_of.
    @staticmethod
    def addMember(name, email, status): 
        rows = app.db.execute("""
INSERT INTO Member_of(name, email, status)
VALUES(:name, :email, :status)
RETURNING name
""", name=name, email=email, status=status)
        name = rows[0][0]
        return name