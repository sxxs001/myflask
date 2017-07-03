from flask import Flask
from forms import LoginForm
from flask import render_template, flash, redirect
from cmdblib.client import Client
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route('/index')
def index():
    user = {'nickname': 'Bob'}
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', user=user, title='home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for OpenID="'+form.openid.data+'",rember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)


@app.route('/group', methods=['GET', 'POST'])
def ShowGroup():
    data = GetGroup('lpd_team.galaxy_engine')
    return render_template('grous.html', groups=data)


def GetGroup(appid):
    client = Client(host="cmdb.elenet.me", port=80, client_id="2d8dae19c0c44a82a707b507104d0594",
                    secret="isQfGATK9CoIyyzIcZRf0jpgc2MnzksEmiTdTgPLY0Kx2FZdb7Hnc8JjzDLyLdF3gUl5KoxQX98QQu7XMwbOIyEF6FkRSKkTLTmDve1aILbWWvBColx6RsnXUpkCEEDO")
    search_results = client.search_entities_by_query('\"' + appid + '\"', size=1000)
    resaults = {}
    for i in search_results:
        if str(type(i)) == "<class 'cmdblib.entity.rl_group_hosts'>":
            if i.env == 'prod' and len(i.hosts) != 0:
                resaults[i.name] = (i.hosts)
    return resaults


if __name__ == '__main__':
    app.run(debug=True)
