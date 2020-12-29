##
# This function create a global list in config with name HEADER_MENU
# @param app
# @return none
# #
def init_app(app):
    app.config['HEADER_MENU'] = [
        {
            "name": "SOBRE",
            "path": "/#sobre"   
        },
        {
            "name": "POSTS",
            "path": "/#post"
        },
        {
            "name": "CONTATO",
            "path": "/#contato"
        }
    ]