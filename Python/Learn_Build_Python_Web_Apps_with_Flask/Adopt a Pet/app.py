# Set Up the Flask App
from helper import pets
from flask import Flask
app = Flask(__name__)

# Create the index Route
@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''

# Create the animals route
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for i, item in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{i}">' + item["name"] + '</a></li>'
  html += '</ul>'
  return html

# Create a pet route
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'''
  <h1>{pet["name"]}</h1>
  <img src="{pet["url"]}"/>
  <p>{pet["description"]}</p>
  <ul>
    <li>breed : {pet["breed"]}</li>
    <li>age : {pet["age"]}</li>
  </ul>
  '''
