# django-template

Starting django template with logging, custom user model, docker and postgres

## How to use

### Replace all replace_some_text with your values.

### Here is checklist to ensure that you replace all values

| File               | Value      |
| ------------------ | ---------- |
| .env.example       | SECRET_KEY |
| docker-compose.yml | image      |
|                    |            |
|                    |            |
|                    |            |
|                    |            |
|                    |            |
|                    |            |

### Create .env file using

## How to add dependencies

### First way

Manually add it to requirements.txt file and rebuild docker container using next command:

```
docker compose build
```

### Second way is in some way easier

-   First you need to enter docker container terminal
-   Inside terminal run install command

```
pip install <your-dep>
```

-   After you finished adding dependencies run

```
pip freeze > requirements.txt
```

-   And now you can re-build docker container

```
docker compose build
```
