# HelloSign-HelloWorld
A template for getting started with HelloSign Embedded Signatures <br />

**To deploy on Heroku:**
1. Create new app in Heroku and a new API app in HelloSign
2. Create environment variables in Heroku: 
    -   HS_APP_KEY (From your HS App)
    -   HS_CLIENT_ID (From your HS App)
    -   TEMPLATE_ID (From a HS Template you have created)
    -   FLASK_SECRET_KEY (Create a random Flask secret key)
3. Clone this repository:
    ~~~
    $ git clone https://github.com/benchello/HelloSign-HelloWorld.git
    ~~~
4. CD into local repository and Deploy to Heroku:
    ~~~
    $ heroku login
    $ heroku remote -a my-heroku-project-name
    $ heroku push master
    ~~~
5. Monitor with:
    ~~~
    heroku logs --tail
    ~~~