# G2-3OTA
Implementation of DozenalFTW's guess 2/3 of the average game using KACPAW


### Game Objectives

1. Each person makes a guess from 0 to 1000. We should have three sliders for each digit so it's harder to visualize the numbers (or even weirder, 10 switches as a binary rep)
    * Possibly, we could allow decimals... not sure
1. After a week, the bot takes all guesses and averages them, then multiples by 2/3
1. Everyone receives a notification of how they did... closest to 2/3 of the average wins


### Getting Started

To get started, clone this repo.  You should probably also install Python 3 if you haven't already.

For the front end:

1. Write jinja2 templates in the templates folder.  `program.html` jinja2 entry point.
2. Run `view-front-end.py` to open up a browser window displaying the formatted file.  
    * You will need jinja2 for this to work.  `pip install` it.  
    * `view-front-end.py` should roughly match the back end in terms of stuff passed into the render function.  If this is not the case, update it.

For the back end:

1. Install virtualenv (you don't have to, but that's what we'll use in these instructions)
2. Create and activate a virtualenv (see [these instructions](https://virtualenv.readthedocs.org/en/latest/userguide.html) for details)
3. Inside the virtualenv, `pip install ./external/kacpaw`.  
    * If your virtualenv doesn't know about jinja2 or any other libraries we might use, `pip install` those too
4. Currently, the back end is empty, but you will probably need to set some environment variables like `KA_USERNAME` and `KA_PASSWORD` for it to work.
5. Run stuff.