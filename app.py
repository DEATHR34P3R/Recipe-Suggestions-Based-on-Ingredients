
from flask import Flask, render_template, request
import json
import zipfile
import os
import pathlib

app = Flask(__name__)

STOP_WORD_TITLE = '📗 '
STOP_WORD_INGREDIENTS = '\n🥕\n\n'
STOP_WORD_INSTRUCTIONS = '\n📝\n\n'

def load_dataset(cache_dir):
    dataset_file_names = [
        'recipes_raw_nosource_ar.json',
        'recipes_raw_nosource_epi.json',
        'recipes_raw_nosource_fn.json',
    ]
    dataset = []
    for dataset_file_name in dataset_file_names:
        dataset_file_path = f'{cache_dir}/datasets/{dataset_file_name}'
        with open(dataset_file_path) as dataset_file:
            json_data_dict = json.load(dataset_file)
            json_data_list = list(json_data_dict.values())
            dataset += json_data_list
    return dataset

def recipe_validate_required_fields(recipe):
    required_keys = ['title', 'ingredients', 'instructions']
    if not recipe:
        return False
    for required_key in required_keys:
        if not recipe[required_key]:
            return False
        if isinstance(recipe[required_key], list) and len(recipe[required_key]) == 0:
            return False
    return True

def recipe_to_string(recipe):
    noize_string = 'ADVERTISEMENT'
    title = recipe['title']
    ingredients = recipe['ingredients']
    instructions = recipe['instructions'].split('\n')

    ingredients_string = ''
    for ingredient in ingredients:
        ingredient = ingredient.replace(noize_string, '')
        if ingredient:
            ingredients_string += f'• {ingredient}\n'

    instructions_string = ''
    for instruction in instructions:
        instruction = instruction.replace(noize_string, '')
        if instruction:
            instructions_string += f'▪︎ {instruction}\n'

    return f'{STOP_WORD_TITLE}{title}\n{STOP_WORD_INGREDIENTS}{ingredients_string}{STOP_WORD_INSTRUCTIONS}{instructions_string}'

def search_by_ingredients(dataset, user_ingredients):
    results = []
    for recipe in dataset:
        ingredients_text = " ".join(ingredient.lower() for ingredient in recipe['ingredients'])
        if all(item.lower() in ingredients_text for item in user_ingredients):
            results.append(recipe_to_string(recipe))
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    if request.method == "POST":
        ingredients_input = request.form.get("ingredients", "")
        user_ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]
        cache_dir = './tmp'
        pathlib.Path(cache_dir).mkdir(exist_ok=True)
        zip_path = os.path.join(cache_dir, 'recipes_raw.zip')
        if os.path.exists('recipes_raw.zip'):
            with zipfile.ZipFile('recipes_raw.zip', 'r') as zip_ref:
                zip_ref.extractall(cache_dir)
        elif os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(cache_dir)
        else:
            return render_template("index.html", recipes=[], error="Dataset not found!")
        dataset_raw = load_dataset(cache_dir)
        dataset_validated = [r for r in dataset_raw if recipe_validate_required_fields(r)]
        recipes = search_by_ingredients(dataset_validated, user_ingredients)
    return render_template("index.html", recipes=recipes, error=None)

if __name__ == "__main__":
    app.run(debug=True)
