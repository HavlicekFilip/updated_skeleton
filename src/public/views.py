"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, redirect,url_for,flash
from .forms import LogUserForm, secti,masoform
from ..data.database import db
from ..data.models import LogUser,Emaily
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

from forms import letadloForm
from ..data.models.letadlo import LetadloSQL
from forms import emailForm


@blueprint.route('/letadlo', methods=['GET','POST'])
def letadlo():
    pole=[['Kuba','Autista', 2000],['Pepa','Dyslektic'],['Filip','Normalni',1999]]
    form = letadloForm()
    if form.validate_on_submit():

        LetadloSQL.create(**form.data)
    return render_template('public/letadlo.tmpl', form=form,pole=pole)

@blueprint.route('/email', methods=['GET','POST'])
def EmailForm():
    form = emailForm()
    if form.validate_on_submit():
        Emaily.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/email.tmpl', form=form)

@blueprint.route('/testlist',methods=['GET'])
def formularlist():
    pole = db.session.query(Emaily).all()
    return render_template('public/testlist.tmpl',pole=pole)

@blueprint.route('/smazEmail/<id>',methods=['GET'])
def formularDel(id):
    iddel = db.session.query(Emaily).filter_by(id=id).first()
    Emaily.delete(iddel)
    return redirect(url_for('public.formularlist'))