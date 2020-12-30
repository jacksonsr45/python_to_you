from python_to_you.models import Role

class Role():
    def __init__(self):
        self.role = Role


    def get(self, id):
        return self.role.query.filter_by(id=id).first()


    def create(self, user_id, is_admin):
        role = self.role(
                user_id,
                is_admin                                                                                          
            )
        self.role.session.add(role)
        self.role.session.commit()


    def update(self, user_id, is_admin):
        role = self.role.query.filter_by(id=id).first()
        role.user_id = user_id 
        role.is_admin = is_admin
        role.session.commit()