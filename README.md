# Deploying Flask apps on Heroku

Heroku is a cloud-based platform for deploying web applications.

See the [basic Flask demo](https://github.com/wellesleynlp/flaskdemo) to get started on building a Flask app.
 
## Requirements

1. Flask (`pip install flask`)
2. gunicorn (http://gunicorn.org or `brew install gunicorn` if you have `brew`)
3. heroku (https://devcenter.heroku.com/articles/heroku-command or `brew install heroku`)

## Code Modification

In contrast to the basic Flask demo, you'll need to separate out your application into an "app" module -- just move all your code into a directory named `app`, with an `__init__.py` file.
Create a new Python file (`main.py` in this example) outside the `app` directory that simply runs the app.

Note that any data files that your application reads should remain in the top level (not the `app` directory).

## Gunicorn

The built-in Flask server isn't powerful enough for deployment. 
Once you've installed `gunicorn`, run 

    gunicorn app:app

This should serve up your app just as before. 
Test that everything works before deploying.

## Deploy publicly on Heroku

1. Create an account on https://signup.heroku.com
1. Type `heroku login` from the top level of your code, and sign in with your account credentials
1. Create new files named `requirements.txt` containing the required programs for your app, and `Procfile`, like the examples here.
1. Create a new application on Heroku with `heroku apps:create yourappname`. 
1. Add, commit, and push your code to Heroku by typing `git push heroku master`

If all goes well, this will automatically build your application on the Heroku servers, and deploy it on the displayed URL. 
For example, this demo is on https://tranquil-ocean-84646.herokuapp.com/
(I didn't choose a name on the creation step, so it assigned me a random one.)
 
Updating your code is just a matter of committing your changes as you would for any git repository.

Note that if your code was already versioned on GitHub, creating the heroku application added a new remote named "heroku" that points to your Heroku repository. So now you have two remotes for the same repository -- the second one is "origin", that presumably points to GitHub. 

You can selectively push changes either by specifying the remote (`git push heroku master` or `git push origin master`). When no name is specified, it defaults to "origin". Whatever is pushed to heroku is automatically built.

