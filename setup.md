Prior to running this stack you will need to ensure that you have docker desktop installed. You can find it at: https://www.docker.com/products/docker-desktop/


If you run the docker compose in the terminal the stack should come up. To run the entire stack, from the project root use the command:
```bash
docker-compose up --force-recreate --build -d
```

The api-migrations container is responsible for making changes to the database and the database tables. 
We use something called Alembic to do migrations to ensure that the database can easily be changed with new upgrades.
Within the files you will see a migrations and a versions folder. 
This shows the database changes. 
When the api-migrations container is started, it will check the current migration the database is on. 
If it needs to it will then run all new database migrations and then will stop. You can see it running upgrades within the logs of the container.

If you create a shell on the DB and use the command:
```bash
mysql -uroot -p$MYSQL_ROOT_PASSWORD apidb;
```
You will be able to connect to the db and can run commands to see the database structure.

The current stack is operating with a given URL and handling the traffic using NGINX. Looking at the .env it is currently using nerdl.test for WEB and api.nerdl.test for API 

To update your local machines DNS so that it knows these urls are local run:

For Windows in an Admin cmd:
```bash
notepad.exe c:\Windows\System32\Drivers\etc\hosts
```
For MAC or Linux
```bash
sudo nano /etc/hosts
```

Add:
```
127.0.0.1 nerdl.test 
127.0.0.1 api.nerdl.test
```
This will make it so that it hits your local docker stack instead of the public dns when entering these into the url bar of a browser.

You can test this by running the stack and visiting:
http://api.nerdl.test/public/courses 
or 
http://nerdl.test

If these pages load successfully then all should be set up correctly

You can find passwords etc within the .env



To run the React Webapp on its own - to be able to view changes in real time rather than having to recreate the container after each change (will require node installed):
```bash
cd web/app/
npm install
npm start
```

If you have any questions please reach out to:
james.eldridge@nerdl.io
