from flask import Flask, render_template, g, request
import sqlite3



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
    return render_template(
        "courses.html",
        custom_css="courses",
        courses=courses,
        companies=companies,
        courses_name=courses_name,
        certificate=certificate,
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

    # نحضّر قائمة المدن المميزة لعرضها في القائمة المنسدلة
    cities_cursor = db.execute("SELECT DISTINCT city FROM Spaces")
    cities = cities_cursor.fetchall()

    return render_template("spaces.html", custom_css="spaces", spaces=spaces, cities=cities)

@app.route("/help")
def help():
    return render_template("help.html", custom_css ="help")


@app.route("/youtube_channels")
def youtube_channels():
    return render_template("youtube_channels.html", custom_css="youtube_channels")

if __name__ == "__main__":
    app.run(debug=True, port=9000)


from flask import Response
from datetime import datetime

@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    pages = [
        {"loc": "https://pcgplatform.com/", "lastmod": "2024-05-13"},
        {"loc": "https://pcgplatform.com/about", "lastmod": "2024-05-13"},
        {"loc": "https://pcgplatform.com/courses", "lastmod": "2024-05-13"},
        {"loc": "https://pcgplatform.com/spaces", "lastmod": "2024-05-13"},
        {"loc": "https://pcgplatform.com/help", "lastmod": "2024-05-13"}
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in pages:
        xml.append("  <url>")
        xml.append(f"    <loc>{page['loc']}</loc>")
        xml.append(f"    <lastmod>{page['lastmod']}</lastmod>")
        xml.append("    <changefreq>monthly</changefreq>")
        xml.append("    <priority>0.8</priority>")
        xml.append("  </url>")

    xml.append("</urlset>")

    response = Response("\n".join(xml), mimetype="application/xml")
    return response

