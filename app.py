from flask import Flask, render_template, g, request
import sqlite3
from datetime import datetime


app = Flask(__name__, static_folder='static', static_url_path='/static')

db = sqlite3.connect("pcg.db")

DATABASE = "pcg.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("pcg.db")
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route("/")
def homepage():
    return render_template("homepage.html", custom_css ="homepage")

@app.route("/about")
def about():
    return render_template("about.html", custom_css ="about")

@app.route("/courses", methods=["GET"])
def courses():
    db = get_db()

    # Get filter values from the form
    mode = request.args.get("mode")
    certificate = request.args.get("certificate")
    company = request.args.get("company")
    course = request.args.get("course")

    # Build dynamic SQL query
    query = "SELECT * FROM courses WHERE 1=1"
    params = []

    if mode:
        query += " AND `online/in-person` = ?"
        params.append(mode)

    if certificate:
        query += " AND `certificate` = ?"
        params.append(certificate)

    if company:
        query += " AND english_name_company = ?"
        params.append(company)

    if course:
        query += " AND english_name_course = ?"
        params.append(course)

    cursor = db.execute(query, params)
    courses = cursor.fetchall()

    # Populate dropdowns
    companies = db.execute("SELECT DISTINCT english_name_company FROM courses").fetchall()
    courses_name = db.execute("SELECT DISTINCT english_name_course FROM courses").fetchall()
    certificate = db.execute("SELECT DISTINCT certificate FROM courses").fetchall()
    onlineOrInperson = db.execute("SELECT DISTINCT `online/in-person` FROM courses").fetchall()
    result_count = len(courses)

    return render_template(
        "courses.html",
        custom_css="courses",
        courses=courses,
        companies=companies,
        courses_name=courses_name,
        certificate=certificate,
        result_count=result_count,
        onlineOrInperson=onlineOrInperson
    )


@app.route("/spaces")
def spaces():
    db = get_db()
    city_filter = request.args.get("city")

    query = "SELECT * FROM Spaces"
    params = []

    if city_filter:
        query += " WHERE city = ?"
        params.append(city_filter)

    cursor = db.execute(query, params)
    spaces = cursor.fetchall()
    cities_cursor = db.execute("SELECT DISTINCT city FROM Spaces")
    cities = cities_cursor.fetchall()
    result_count = len(spaces)
    return render_template("spaces.html", 
                                custom_css="spaces", 
                                spaces=spaces, 
                                result_count=result_count,
                                cities=cities)

@app.route("/help")
def help():
    return render_template("help.html", custom_css ="help")


@app.route("/youtube_channels")
def youtube_channels():
    db = get_db()
    cursor = db.cursor()

    
    query = "SELECT * FROM youtube_courses WHERE 1=1"
    params = []

    categorys_cursor = db.execute("SELECT DISTINCT category FROM youtube_courses")
    categorys = categorys_cursor.fetchall()

    course_title = db.execute("SELECT DISTINCT course_title FROM youtube_courses")
    course_titles = course_title.fetchall()

    category_filter = request.args.get("category")
    course_title_filter = request.args.get("course_title")

    if course_title_filter:
        query += " AND course_title = ?"
        params.append(course_title_filter)

    if category_filter:
        query += " AND category = ?"
        params.append(category_filter)


    cursor = db.execute(query, params)
    youtube_courses = cursor.fetchall()
    result_count = len(youtube_courses)
    return render_template(
        "youtube_channels.html",
        custom_css="youtube_channels", 
        youtube_courses=youtube_courses, 
        result_count=result_count,
        course_titles=course_titles,
        categorys=categorys)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', custom_css='privacy')


@app.route('/terms')
def terms():
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('terms.html', custom_css='terms', today=today)

@app.route('/podcast')
def podcast():
    db = get_db()


    query = "SELECT * FROM podcast WHERE 1=1"
    params = []

    podcast_field_filter = request.args.get("podcast_field")
    podcast_guest_filter = request.args.get("podcast_guest")
    podcast_name_filter = request.args.get("podcast_name")

    if podcast_field_filter:
        query += " AND podcast_field = ?"
        params.append(podcast_field_filter)

    if podcast_guest_filter:
        query += " AND podcast_guest = ?"
        params.append(podcast_guest_filter)
    
    if podcast_name_filter:
        query += " AND podcast_name = ?"
        params.append(podcast_name_filter)

    cursor = db.execute(query, params)
    podcasts = cursor.fetchall()

    podcast_fields_cursor = db.execute("SELECT DISTINCT podcast_field FROM podcast")
    podcast_fields = podcast_fields_cursor.fetchall()

    podcast_guests_cursor = db.execute("SELECT DISTINCT podcast_guest FROM podcast")
    podcast_guests = podcast_guests_cursor.fetchall()

    podcast_names_cursor = db.execute("SELECT DISTINCT podcast_name FROM podcast")
    podcast_names = podcast_names_cursor.fetchall()

    result_count = len(podcasts)
    return render_template(
        'podcast.html', 
        custom_css='podcast', 
        podcasts=podcasts, 
        podcast_fields=podcast_fields, 
        podcast_guests=podcast_guests,
        podcast_names=podcast_names,
        result_count=result_count)

@app.route('/ai_tools')
def ai_tools():
    db = get_db()
    query = "SELECT * FROM ai_tools WHERE 1=1"
    params = []

    category = request.args.get("category")
    cursor = db.execute("SELECT DISTINCT category FROM ai_tools")
    categorys = cursor.fetchall()
    if category:
        query += " AND category = ?"
        params.append(category)

    cursor = db.execute(query, params)
    ai_tools = cursor.fetchall()

    result_count = len(ai_tools)

    return render_template(
        'ai_tools.html', 
        custom_css='ai_tools',
        ai_tools=ai_tools,
        categorys=categorys,
        result_count=result_count)

if __name__ == "__main__":
    app.run(debug=True, port=9000)
