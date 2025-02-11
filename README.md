# Receipt Processor API

This is a **Python-based API** for processing receipts and calculating points. The application is **Dockerized**, making it easy to set up and run.

---

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/anirudhb-a/receipt-processor-challenge.git
cd receipt-processor-challenge
```

### 2. Run the Application with Docker
Ensure **Docker** is installed, then start the service:
```sh
docker-compose up --build
```
This will build the Docker image and start the API.

---

## API Endpoints

Once the service is running, the API will be available at `http://localhost:5000`.

### Submit a Receipt

- **Endpoint:** `POST /receipts/process`
- **Example Request:**
  ```json
  {
    "retailer": "Target",
    "purchaseDate": "2025-02-10",
    "purchaseTime": "13:01",
    "items": [
      { "shortDescription": "Mountain Dew", "price": "1.99" },
      { "shortDescription": "Doritos", "price": "2.99" }
    ],
    "total": "4.98"
  }
  ```
- **Example Response:**
  ```json
  { "id": "abc123" }
  ```

---

### Get Receipt Points

- **Endpoint:** `GET /receipts/{receipt_id}/points`
- **Example Request:**
  ```sh
  curl -X GET http://localhost:5000/receipts/abc123/points
  ```
- **Example Response:**
  ```json
  { "points": 12 }
  ```

---

## Stopping the Application

To stop the running container:
```sh
docker-compose down
```

---

## Notes for Reviewers

- The application is **stateless**, meaning data is stored in memory and is lost when the service stops.
- Business logic for **point calculation** is located in the `app/` directory.
- The API is built using **Flask** and structured for easy scalability.
- To debug any issues, check the container logs:
  ```sh
  docker logs <container_id>
  ```

---


