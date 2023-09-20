from flask import Flask, request, jsonify, render_template
from . import home
from libgen_api import LibgenSearch

# Create a LibgenSearch object
search = LibgenSearch()

@home.route("/")
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template("page/home/index.html", title="Welcome")

@home.route('/search', methods=['GET','POST'])
def search_books():
    query = request.form.get('search')
    print(query)

    if not query:
        return jsonify({"error": "Please provide a 'query' parameter"}), 400

    results = search.search_title(query)
    formatted_results = []
    for result in results:
        formatted_result = {
            "ID": result['ID'],
            "Author": result['Author'],
            "Title": result['Title'],
            "Publisher": result['Publisher'],
            "Year": result['Year'],
            "Pages": result['Pages'],
            "Language": result['Language'],
            "Size": result['Size'],
            "Extension": result['Extension'],
            "Mirror_1": result['Mirror_1'],
            "Mirror_2": result['Mirror_2'],
            "Mirror_3": result['Mirror_3']
            # "Mirror_4": result['Mirror_4'],
            # "Mirror_5": result['Title']
        }
        formatted_results.append(formatted_result)
    print (formatted_results)
    return jsonify(formatted_results)


# @home.route("/dashboard")
# def dashboard():
#     """
#     Render the dashboard template on the /dashboard route
#     """
#     return render_template("page/home/dashboard.html", title="Dashboard")