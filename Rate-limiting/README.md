# nginx-learning-lab

A hands-on lab to learn and practice NGINX concepts including static site hosting, reverse proxy, load balancing, and rate limiting, with FastAPI integration and Docker support.

## Project Structure

```
nginx-learning-lab
│
├── static-site
│   └── index.html
│
├── fastapi-app
│   └── main.py
│
├── nginx-config
│   ├── static.conf
│   ├── reverse-proxy.conf
│   ├── load-balancer.conf
│   └── rate-limit.conf
│
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── README.md
```

## Contents

- **static-site/**: Simple static website to be served by NGINX.
- **fastapi-app/**: FastAPI application to demonstrate reverse proxy and load balancing.
- **nginx-config/**: NGINX configuration files for different scenarios:
  - `static.conf`: Serve static files
  - `reverse-proxy.conf`: Reverse proxy to FastAPI
  - `load-balancer.conf`: Load balancing setup
  - `rate-limit.conf`: Rate limiting example
- **docker/**: Docker and Docker Compose files to run the lab easily.

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd nginx-learning-lab
   ```

2. **Build and run with Docker Compose:**
   ```sh
   cd docker
   docker-compose up --build
   ```

3. **Access the services:**
   - Static site: http://localhost:8080
   - FastAPI app (proxied): http://localhost:8000

## Learning Scenarios

- **Static Site Hosting:**
  - Serve HTML files using NGINX.
- **Reverse Proxy:**
  - Forward requests to FastAPI backend.
- **Load Balancing:**
  - Distribute traffic across multiple FastAPI instances.
- **Rate Limiting:**
  - Limit client requests using NGINX.

## Requirements
- Docker & Docker Compose

## License
MIT
