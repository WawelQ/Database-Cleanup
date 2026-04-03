## Setup - Run as a Docker Image
### Method 1: Pull from Docker Hub (Recommended)
**You can simply pull the pre-built image directly from Docker Hub:**

`docker pull wawelq/db-cleanup:latest`
**Run the image and pass .env file to it:**

`docker run --env-file .env wawelq/db-cleanup:latest`

### Method 2: Build Manually
1. **Clone the repository from GitHub:**
`git clone https://github.com/WawelQ/Database-Cleanup`

2. **Set up your `.env` file with your database configuration**
3. **Build Docker image & Run it:**

`docker build -t db-cleanup .`

`docker run --env-file .env db-cleanup`
