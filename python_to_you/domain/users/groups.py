from python_to_you.extensions.marshmallow import ma
from flask_marshmallow.fields import fields
from python_to_you.models import Groups
from marshmallow.exceptions import ValidationError
from python_to_you.domain.core.error import Error

class Group():
    def __init__(self):
        self.group = Groups


    def get(self, id):
        return self.group.query.filter_by(id=id).first()


    def create(self, user_id, create_post, edit_post, update_post, read_post, 
                add_post, remove_post, block_post, title, description):
        try:
            GroupsSchema().load(user_id, create_post, edit_post, update_post, read_post, 
                add_post, remove_post, block_post, title, description)
            group = self.group(
                user_id,
                create_post,
                edit_post,
                update_post,
                read_post,
                add_post,
                remove_post,
                block_post,
                title,
                description
            )
        except ValidationError as error:
            Error(error.normalized_messages(), 400)


    def update(self, id, user_id, create_post, edit_post, update_post, read_post, 
                add_post, remove_post, block_post, title, description):
        try:
            GroupsSchema().load(user_id, create_post, edit_post, update_post, read_post, 
                add_post, remove_post, block_post, title, description)
            group = self.group.query.filter_by(id=id).first()
            group.user_id = user_id
            group.create_post = create_post
            group.edit_post = edit_post
            group.update_post = update_post
            group.read_post = read_post
            group.add_post = add_post
            group.remove_post = remove_post
            group.block_post = block_post
            group.title = title
            group.description = description
        except ValidationError as error:
            Error(error.normalized_messages(), 400)


    def delete(self):
        try:
            group = self.group.query.filter_by(id=id).first()
            self.group.session.delete(group)
            self.group.session.commit()
        except TypeError as error:
            Error(error.normalized_messages(), 400)



class GroupsSchema(ma.Schema):
    user_id = fields.Int(required=True, 
        error_messages={"message": "user_id field is required"})
    create_post = fields.Boolean(required=True, 
        error_messages={"message": "create_post field is required"})
    edit_post = fields.Boolean(required=True, 
        error_messages={"message": "edit_post field is required"})
    update_post = fields.Boolean(required=True, 
        error_messages={"message": "update_post field is required"})
    read_post = fields.Boolean(required=True, 
        error_messages={"message": "read_post field is required"})
    add_post = fields.Boolean(required=True, 
        error_messages={"message": "add_post field is required"})
    remove_post = fields.Boolean(required=True, 
        error_messages={"message": "remove_post field is required"})
    block_post = fields.Boolean(required=True, 
        error_messages={"message": "block_post field is required"})
    title = fields.Str(required=True, 
        error_messages={"message": "title field is required"})
    description =fields.Str(required=True, 
        error_messages={"message": "description field is required"})
    
    class Meta:
        fields = (
            "user_id",
            "create_post",
            "edit_post",
            "update_post",
            "read_post",
            "add_post",
            "remove_post",
            "block_post",
            "title",
            "description"            
        )