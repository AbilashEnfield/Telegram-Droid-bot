This a basic Telegram bot application
In this readme file I"ll give an overview of what's going on:

1. Initially when you visit the first url "https://telegram-droid.herokuapp.com/bot/"
    An basic HTML page is rendered which contains the name of the user and counts each button is clicked.

2. When you visit the second url "https://telegram-droid.herokuapp.com/bot/activate/" the Telegram bot is activated.
    You may see the thread error but it does not affect the working.
    in order to rectify that error you can use the command.
    $ python manage.py runserver --nothreading --noreload

3. visit your telegram app and click a button or enter the name of the button or randomly type anything.
    It will trigger the functions in views.py starting from the "trigger function".

4. Where as trigger function calls actions.py via 'press_button_callback' and 'handle_message'functions.

5. actions.py decides the message to be replied and its where the database model 'telegram_bot_chats' is triggered.
