# Swiftype/Django Example Project

This is a simple blogging engine built using the Django framework that pushes updates to Swiftype via the [swiftype-py](http://github.com/swiftype/swiftype-py) library. Full-text search and autocompletion are built in using the [jQuery search plugin](https://github.com/swiftype/swiftype-autocomplete-jquery) and [jQuery auto-complete plugin](https://github.com/swiftype/swiftype-search-jquery).

## Running the demo

1. Sign up for a [Swiftype account](http://swiftype.com/), then create an API based engine with a Document Type called "posts".
2. Set your Swiftype API and Engine keys as environment variables from the terminal:
    
        export SWIFTYPE_API_KEY=your_api_key
        export SWIFTYPE_ENGINE_KEY=your_engine_key

3. Install the [swiftype-py](http://github.com/swiftype/swiftype-py) library with `pip install swiftype`
4. Clone this repository, `cd` into the directory and run `python manage.py syncdb`. Create a superuser at the prompt.
5. Start the app with: `python manage.py runserver`.
6. Create new posts by visiting localhost:8000/admin and logging in as the superuser.
7. View the blog's index at localhost:8000

As you create, update, and delete blog posts, these changes will be sent to Swiftype to ensure search results are up to date.

Note that this application, by itself, is not production-ready. It's simply meant to act as an example for incorporating the Swiftype API into a Django application.
