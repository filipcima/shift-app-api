# ShiftAppAPI
## Usage
```
git clone https://github.com/filipcima/shift-app-api.git
cd shift-app-api
docker build -t shift-app-api .
docker run -i -p 5000:5000 -e MONGODB_URI="your-local-ip" shift-app-api
```
API will be available on port 5000.

## Database restore
- `mongorestore` database dump in __dump__ folder and run mongodb on its default port.
