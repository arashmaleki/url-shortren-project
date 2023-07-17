# URL Shortener front-end

URL Shortener front-end is a Nuxt.js front-end that allows users to login, register, view and make their shortener urls.
## Getting Started

### Prerequisites

Before running the project, you'll need to have the following installed on your machine:

- Nuxt.js

### Environment Variables

This project uses environment variables to store sensitive information such as database credentials. To run the project, you'll need to create a `.env` file in the root directory of your project and add the required variables just like `.env.sample` file.

1. Create a `.env` file in the root directory of your project:

```bash
touch .env
```

2. Open the `.env.sample` file and copy its contents, paste the contents of the `.env.sample` file into the `.env` file.

3. Replace the default values of the variables with your own values.

```
API_SERVER_BASE_URL="<BACK_END_SERVER_URL>"
NUXT_SERVER_PORT_NUMBER=8000
NUXT_SERVER_HOST_ADDRESS="0.0.0.0"
```

Save the `.env` file.

### Running Locally

To run the project locally, follow these steps:

1. Ensure that PostgreSQL is installed and running locally.
2. Clone the repository to your local machine:

```bash
git clone https://github.com/arashmaleki77/url-shortener-project.git
cd url-shortener-project/front-end-service/
```

3. Install the project's dependencies:

```bash
npm install
```

4. Run:

````bash
npm run dev
````

Once the front-end is running, you can access the client at http://localhost:8000/.

## build for production and launch server

```bash
$ npm run build
$ npm run start
$ npm run generate

OR Running with pm2:
$ npm run build
$ pm2 start

To restart pm2:
$ pm2 restart Shortener
```

### Running with Docker

To run the project using Docker, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/arashmaleki77/url-shortener-project.git
cd url-shortener-project/front-end-service/
```

2. Build and start the Docker containers:

````bash
docker-compose up --build -d
````

Once the containers are running, you can access the API at http://localhost:8000/.





