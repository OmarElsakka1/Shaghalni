from datetime import datetime
import re
from flask import Blueprint, render_template, request, flash , redirect , url_for , session
from flask_login import login_required, current_user
from .ImageManager import  ImageManager
from .UserSystem import UserSystem
from .JobSystem import jobSystem
from .models import User
import os 


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