# URL Shortener app

URL Shortener app is a full-stack website that allows authenticated users to create, view and delete their shortener urls.

### Getting Started

```bash
git clone https://github.com/arashmaleki77/url-shortener-project.git
```

## Back-End-Service

### Services

1. Handling Users, Shortener URLs.

2. This service can handle new shortener urls, be responsible for login and register.

### Technology stack

1. Python

    a. Django Rest Framework 

```
Swagger URL: <BACK_END_SERVICE_URL>/doc
```

2. Postgresql
    
    a. Used for our database

### Database schemas

1. UML file is in `/back-end-service/docs/uml.png`


### Getting Started

```bash
cd back-end-service/
```

Open `README.md` file and follow the instruction.


## Front-End-Service

### Technology stack

1. Javascript

   a. VueJS framework

      1. Using its guidelines and basics for our main framework which is NuxtJS, in fact Nuxt uses Vue in its back.

   b. NuxtJS framework
      
      1. Managing routing system: VueRouter

      2. Managing global states (State Management): VueX

2. Architecture

   a. Component based


### Getting Started

```bash
cd front-end-service/
```

Open `README.md` file and follow the instruction.