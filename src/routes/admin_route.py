from flask import Blueprint 

from src.utils.constants.app import BASEDIR
from src.controllers.admin_controller import controller 
 
admin =Blueprint('admin', __name__, template_folder= BASEDIR /'templates/admin') 

admin.route('/')(controller)
admin.route('/<string:page>')(controller)
admin.route('/<string:page>/<string:section>')(controller)
admin.route('/<string:page>/<string:section>/<string:action>', methods =['GET', 'POST'])(controller) 
admin.route('/<string:page>/<string:section>/<string:action>/<string:id>', methods =['GET', 'POST'])(controller) 
# admin.route('/404')(error_404)
# admin.route('/403')(error_403)