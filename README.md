## Setup - run this program as a Docker image:
### First method (Recommended):
You can simply pull already made image from Docker Hub

`docker pull wawelq/db-cleanup:latest`
### Second method:
**Build docker image manually**
1. **Clone repository from github:**
`git clone https://github.com/WawelQ/Database-Cleanup`

2. **Set up your `.env` file with your database configuration**
3. **Build Docker image & Run it:**

`docker build -t db-cleanup .`

`docker run --env-file .env db-cleanup`
