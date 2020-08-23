# hap.py
Too lazy to find some funny jokes? hap.py is here to help! hap.py is a one stop facial recognition software that will send you the greatest (and most appropriate) jokes based on your mood and age. On top of that, jokes will be sent straight to your phone, allowing you to be connected with the top memes at your convenience. 

## Inspiration
Whenever we feel happy, sad, angry, or anything in between, jokes can provide the necessary moral support to make your day one thousand times better. But how could we make jokes *even better*? Ever since we have been stuck at home, finding shortcuts to every day problems has been essential. That's where facial recognition can come in! Having a mood-detecting software that **also** sends you jokes would be the perfect combination to satisfy your everyday needs.

## What it does


## How we built it
1. Create routes to index.html and results.html with Flask
2. Use Microsoft Face API to detect age and emotion (happiness index)
3. Calculates joke category based on emotion detected
4. Parses through Joke API and retrieves joke with corresponding parameters
5. Send joke to inputted phone number with Twilio API
6. Run localhost and test out the app!

## Challenges we ran into
- Used an outdated version of Jokes API at first
- Version control issues with Git
- Converting web data to JSON objects
- Developing algorithm to relate happiness and joke category

## Accomplishments that we're proud of
- Utilized multiple APIs in conunction with each other
- Developed fully functional web application using Flask
- Learned how to create full stack apps

## What we learned

## What's next for hap.py
Now that we've developed the basic framework for hap.py, we have a lot in store for the future! First, we plan on cleaning up the UI/UX of the web app to provide a more aesthetic interface for users. Once that is done, we will deploy hap.py to the internet using Heroku, so that it will be accessible to everyone!


