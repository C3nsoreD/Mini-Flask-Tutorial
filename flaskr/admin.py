from flask import (
    Blueprint, flash ,g, redirect, url_for, render_template, request
)
from flask.auth import login_required
from flask.db import get_db()


bp = Blueprint('admin', __name__)

@bp.route('/admin', methods=['GET', 'POST'])
def adminIndex():
    pass
