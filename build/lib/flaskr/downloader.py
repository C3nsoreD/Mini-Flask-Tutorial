from flask import (
    Blueprint, flash ,g, redirect, url_for, render_template, request
)
from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('donwloader', __name__, url_prefix="download")
