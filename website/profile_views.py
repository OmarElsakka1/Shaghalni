from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
from .user_system import userSystem



profile_views = Blueprint('profile_views', __name__)

@profile_views.route('/profile/<int:id>/view',  methods=['GET', 'POST'])
@login_required
def view_profile(id : int) :

    user = userSystem.GetUser(id)
    return render_template('profile.html', user=current_user , target = user)

# Search by name
@profile_views.route('/profile/search?/<string:name>',  methods=['GET', 'POST'])
@login_required 
def search_profile(name : str) :
    users = userSystem.SearchUsersByName(name)
    return render_template('search.html',  user=current_user,search_prompt = name ,found=users)


@profile_views.route('/users/<int:user_id>/get-image', methods=['GET'])
@login_required
def get_image(user_id : int) :
    user = userSystem.GetUser(user_id)
    print(user.image_name)
    if user is None :
        return "User not found"
    if user.image_name :
        print(user.image_name)
        return send_file( '../'+ user.image_name, mimetype='image/jpg') , 200
    else :
        return send_file('static/Images/default_profile_image.png' , mimetype='image/jpg') ,200