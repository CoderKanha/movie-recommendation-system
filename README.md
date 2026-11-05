# 🎬 Movie Recommendation System

A simple content-based movie recommender built with [Streamlit](https://streamlit.io/). Pick a movie from the dropdown, click **Recommend**, and the app shows the 5 most similar movies based on precomputed similarity scores.

## How It Works

1. `movies_recommend.pickle` holds a pandas DataFrame of movies (including a `title` column).
2. `similarities.joblib` holds a precomputed similarity matrix, where row *i* contains the similarity of movie *i* to every other movie.
3. When you select a movie and click **Recommend**, the app:
   - finds the movie's index in the DataFrame,
   - looks up its row in the similarity matrix,
   - sorts the scores in descending order,
   - skips the first result (the movie itself), and
   - displays the next 5 most similar titles.

## Project Structure

```
.
├── app.py                    # Streamlit application
├── movies_recommend.pickle   # Movies DataFrame (must contain a "title" column)
├── similarities.joblib       # Precomputed similarity matrix
├── requirements.txt          # Python dependencies
└── README.md
```

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

The app also imports `pickle` (standard library) and `joblib`, plus `pandas` to unpickle the DataFrame. If `joblib` or `pandas` are not already installed alongside Streamlit, install them too:

```bash
pip install streamlit pandas joblib
```

> **Tip:** Consider adding `pandas`, `joblib`, and `scikit-learn` (if used to build the similarity matrix) to `requirements.txt`, and pin versions to match the environment the pickle/joblib files were created in.

## Installation

```bash
# 1. Clone or download the project
git clone <your-repo-url>
cd <your-project-folder>

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install pandas joblib
```

## Running the App

Make sure `movies_recommend.pickle` and `similarities.joblib` are in the same directory as `app.py`, then run:

```bash
streamlit run app.py
```

Streamlit will open the app in your browser, usually at `http://localhost:8501`.

## Usage

1. Choose a movie from the **Movies** dropdown.
2. Click the **Recommend** button.
3. The app lists 5 recommended movies similar to your selection.

## Notes

- The lookup compares `movie_name.lower()` against the `title` column, so titles in the DataFrame are expected to be stored in **lowercase**.
- The similarity matrix rows must be aligned with the DataFrame's index order.
- Pickle and joblib files can execute arbitrary code when loaded. Only use files from sources you trust.
- Loading the data on every rerun can be slow for large datasets. You can speed things up with `@st.cache_data` / `@st.cache_resource` around the loading code.

## Possible Improvements

- Cache the data loading with Streamlit's caching decorators.
- Show movie posters and details (e.g., via the TMDB API).
- Let users choose how many recommendations to display.
- Add search/autocomplete for large movie lists.

## License

Add your preferred license here (e.g., MIT).