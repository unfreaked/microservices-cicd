# Microservices CI/CD Project

## Project Structure
- `backend/` - Flask microservices (`user-service`, `product-service`)
- `frontend/` - React app
- `nginx/` - NGINX reverse proxy config
- `docker-compose.yml` - Orchestrates all services

## Running Locally with Docker Compose

1. **Build and start all services:**
   ```sh
   docker-compose up --build
   ```

2. **Access the app:**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - User API: [http://localhost:80/api/users](http://localhost:80/api/users)
   - Product API: [http://localhost:80/api/products](http://localhost:80/api/products)

3. **Stopping services:**
   ```sh
   docker-compose down
   ```

## Next Steps
- Add CI/CD with GitHub Actions
- Add Ansible playbooks for deployment
