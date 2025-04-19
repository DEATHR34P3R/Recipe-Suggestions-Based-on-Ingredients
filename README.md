# 🥗 Ingredient-Based Recipe Search Web App

A web application built with **Flask** that allows users to input a list of ingredients and receive relevant recipes from a large offline dataset. 
The app is ideal for those who want to make the most out of their available ingredients and discover new dishes without having to search the internet manually.

---

## 🌟 Key Features

- 🔎 **Search Recipes by Ingredients**: Type in what ingredients you have, and the app returns matching recipes.
- ✅ **Cleans & Validates Recipe Data**: Filters out incomplete or noisy entries to improve result quality.
- 📖 **Formatted Output**: Recipes are displayed with clear sections for the title, ingredients, and instructions.
- 🗃️ **Offline Dataset Support**: Uses a pre-downloaded dataset of 200k+ recipes from real-world sources.
- ⚡ **Fast Search**: Ingredient matching is optimized by checking lowercased strings.
- 🧪 Great for learning Flask, file handling, and data preprocessing!

---

## 🔧 Setup Instructions

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/yourusername/recipe-search-app.git](https://github.com/DEATHR34P3R/Recipe-Suggestions-Based-on-Ingredients
cd Recipe-Suggestions-Based-on-Ingredients
```

### 2. 📦 Install Dependencies

Ensure Python 3.7+ is installed. Then install Flask:

```bash
pip install flask
```

### 3. 📥 Add the Dataset

Download the dataset `recipes_raw.zip` from (https://eightportions.com/) or from another source and place it in **one of these locations**:

- Recommended: `./recipes_raw.zip` (next to `app.py`)
- Or: `./tmp/recipes_raw.zip`

⚠️ **Do not extract it manually** — the app handles extraction at runtime.

---

## 🚀 How to Run the App

Run the Flask app using:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. **User Input**: On the homepage, the user enters a comma-separated list of ingredients.
2. **Dataset Extraction**:
   - The app checks for `recipes_raw.zip` in the root or `./tmp/`.
   - If found, it extracts the archive into the `tmp/` folder.
3. **Loading Data**:
   - The app loads JSON files from three sources:
     - `recipes_raw_nosource_ar.json`
     - `recipes_raw_nosource_epi.json`
     - `recipes_raw_nosource_fn.json`
   - All recipes are combined into one list.
4. **Validation**:
   - Recipes missing `title`, `ingredients`, or `instructions` are discarded.
   - Noise such as the word "ADVERTISEMENT" is removed.
5. **Searching**:
   - The app checks if all user-input ingredients are found in the recipe’s ingredient list.
   - Matching recipes are formatted into a readable string.
6. **Result Display**:
   - The final matching recipes are displayed to the user with clear formatting:
     ```
     📗 Chicken Curry

     🥕
     • chicken breast
     • onion
     • garlic

     📝
     ▪︎ Heat oil in a pan...
     ▪︎ Add onions and sauté...
     ```

---

## 🧪 Example Usage

### Input

```
onion, chicken, garlic
```

### Output

```
✅ Found 4 matching recipes:

--- Recipe 1 ---
📗 Spicy Chicken Delight

🥕
• chicken breast
• onion
• garlic
• tomato

📝
▪︎ Marinate the chicken...
▪︎ Heat oil in a pan...
...
```

## ⚠️ Notes & Limitations

- The dataset **must be downloaded manually** due to its size.
- Some recipes may still contain minor formatting issues.
- This app **does not use a database** — everything is done in memory for simplicity.

---



## 🙋 FAQ

**Q: Why use a ZIP file and not raw JSON?**  
A: To keep the app lightweight and allow bundling of all source JSONs in one place.

**Q: Will it work without an internet connection?**  
Yes! Once the dataset is downloaded, no internet is required.

