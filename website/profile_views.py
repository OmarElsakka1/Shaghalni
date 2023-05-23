from datetime import datetime
import re
from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user

from .UserSystem import UserSystem



profile_views = Blueprint('profile_views', __name__)

@profile_views.route('/profile/<int:id>/view',  methods=['GET', 'POST'])
@login_required
def view_profile(id : int) :

    user = UserSystem.GetUser(id)
    return render_template('profile.html', user=current_user , target = user)

# Search by name
@profile_views.route('/profile/search?/<string:name>',  methods=['GET', 'POST'])
@login_required 
def search_profile(name : str) :
    users = UserSystem.SearchUsersByName(name)
    return render_template('search.html',  user=current_user,search_prompt = name ,found=users)


@profile_views.route('/users/<int:user_id>/get-image', methods=['GET'])
@login_required
def get_image(user_id : int) :
    user = UserSystem.GetUser(user_id)
    if user is None :
        return "User not found"
    if user.file :
        print(user.file)
        return send_file( user.file, mimetype='image/jpg')
    else :
        return send_file('static/Images/default_profile_image.png' , mimetype='image/jpg')