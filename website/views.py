from flask import Blueprint, render_template, request, flash, jsonify , redirect , url_for
from flask_login import login_required, current_user
from .models import *
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        name = request.form.get('search_prompt')
        print(name)
        return redirect(url_for('profile_views.search_profile', name=name))
        
    return render_template("home.html", user=current_user)














