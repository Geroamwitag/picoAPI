# ENSURE YOU HAVE THE DB CREDENTIALS IN YOU ENVIRONMENT

in an administrator terminal run:

```
setx ALEKS_DB_URL "postgresql://neondb_owner:npg_cVOowHj6NuI1@ep-dark-union-b2fckmdf.c-6.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require" /M
```

```
setx ALEKS_DB_POOLED "postgresql://neondb_owner:npg_cVOowHj6NuI1@ep-dark-union-b2fckmdf-pooler.c-6.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require" /M
```

# RUNNING DEVELOPMENT API

simply run in the terminal:

```
uvicorn main:app --reload
```

or, to host on local wifi:

```
uvicorn main:app --reload --host 0.0.0.0
```

run ipconfig in a terminal to get the ipaddress for your network, and visit:

```
http://192.168.178.XXX:8000/
```

This will show the API running on the local network, and accessible by and device connected to that network.


# EXPLORING THE API

you can visit the docs route with this url:

```
https://picoapi.onrender.com/docs
```

or this when in development:

```
http://192.168.178.XXX:8000/docs
```

The docs `swagger docs` show all end points of the API along with their required inputs, and even allows you to run a request for testing or manual database post requests.
