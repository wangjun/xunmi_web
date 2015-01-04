from flask import Flask, request
from flask import  render_template
from spider import get_html, get_results
# import util

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/search')
def search():
    keywords = request.args.get('q').split(" ")
    if request.args.get("pn") != None:
        page = int(request.args.get("pn"))
        print "aaaaaaaa"
    else:
        page = 1
    if page == 1:
        pageup_url = "/search?q=" + "+".join(keywords) + "&pn=" + str(page)
    else:
        pageup_url = "/search?q=" + "+".join(keywords) + "&pn=" + str(page - 1)
    pagedown_url = "/search?q=" + "+".join(keywords) + "&pn=" + str(page + 1)
    keywords = filter(lambda x: x != "", keywords)
    html = get_html(keywords, page).encode("utf-8")
    results = get_results(html)
    return render_template("search.html", results=results, pageup_url=pageup_url, pagedown_url=pagedown_url)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/android')
def android():
    return render_template("android.html")

if __name__ == "__main__":
    app.run()