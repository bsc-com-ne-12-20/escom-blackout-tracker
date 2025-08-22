# ESCOM Load Shedding Tracker API Documentation

## Base URL
```
http://127.0.0.1:8000/tracker/api/
```

## Overview
The ESCOM Load Shedding Tracker API provides endpoints to query load shedding schedules and location information for Malawi's power grid groups. Users can search by region, location, group ID, or affected areas.

## Data Structure

### Groups
Load shedding groups (A, A1, A2, B, B1, B2, C1, C2) that represent different power grid sections.

### Locations
Specific locations within each group, organized by region (Central, Southern, Northern).

### Schedules
Blackout schedules associated with each group, including date, start time, and end time.

---

## Endpoints

### 1. List All Regions
**GET** `/api/regions/`

Returns all available regions in the system.

#### Response
```json
{
  "regions": [
    "Central Region",
    "Northern Region", 
    "Southern Region"
  ]
}
```

#### Example
```bash
curl http://127.0.0.1:8000/tracker/api/regions/
```

---

### 2. Get Locations by Region
**GET** `/api/region/{region}/locations/`

Returns all locations within a specific region.

#### Parameters
- `region` (string): Region name (e.g., "Central Region", "Southern Region", "Northern Region")

#### Response
```json
[
  {
    "group_id": "A",
    "region": "Central Region",
    "location": "Lilongwe A",
    "affected_areas": "Area 48"
  },
  {
    "group_id": "A1", 
    "region": "Central Region",
    "location": "Area 25",
    "affected_areas": "Area 25 Sectors 1 2 3 4 5 6 7 8 9 Kings Foundation..."
  }
]
```

#### Example
```bash
curl "http://127.0.0.1:8000/tracker/api/region/Central%20Region/locations/"
```

---

### 3. Get Schedule by Location
**GET** `/api/location/{location}/schedule/`

Returns group information and blackout schedules for a specific location.

#### Parameters
- `location` (string): Exact location name (e.g., "Lilongwe A", "Zomba", "Blantyre")

#### Response
```json
{
  "location_info": {
    "group_id": "A",
    "region": "Central Region", 
    "location": "Lilongwe A",
    "affected_areas": "Area 48"
  },
  "schedules": [
    {
      "group_id": "A",
      "date": "2025-08-22",
      "start_time": "05:00:00",
      "end_time": "09:30:00"
    },
    {
      "group_id": "A",
      "date": "2025-08-22", 
      "start_time": "16:00:00",
      "end_time": "21:00:00"
    }
  ]
}
```

#### Error Response
```json
{
  "error": "Location not found"
}
```

#### Example
```bash
curl "http://127.0.0.1:8000/tracker/api/location/Lilongwe%20A/schedule/"
```

---

### 4. Search Affected Areas
**GET** `/api/search/?q={query}`

Search for locations by affected areas or location names.

#### Parameters
- `q` (string): Search query (e.g., "Area 48", "Bangwe", "University")

#### Response
```json
{
  "query": "Area 48",
  "results": [
    {
      "group_id": "A",
      "region": "Central Region",
      "location": "Lilongwe A", 
      "affected_areas": "Area 48",
      "schedules": [
        {
          "group_id": "A",
          "date": "2025-08-22",
          "start_time": "05:00:00",
          "end_time": "09:30:00"
        }
      ]
    }
  ],
  "count": 1
}
```

#### Error Response
```json
{
  "error": "Query parameter \"q\" is required"
}
```

#### Example
```bash
curl "http://127.0.0.1:8000/tracker/api/search/?q=Area%2048"
curl "http://127.0.0.1:8000/tracker/api/search/?q=Bangwe"
curl "http://127.0.0.1:8000/tracker/api/search/?q=University"
```

---

### 5. List All Locations
**GET** `/api/locations/`

Returns all locations in the system with their group information.

#### Response
```json
[
  {
    "group_id": "A",
    "region": "Central Region",
    "location": "Lilongwe A",
    "affected_areas": "Area 48"
  },
  {
    "group_id": "A",
    "region": "Southern Region", 
    "location": "Limbe A",
    "affected_areas": "Bangwe Chirimba Thothozi Machinjiri Areas 1 2 3 5 6 7 8 9 10 11 and 12"
  }
]
```

#### Example
```bash
curl http://127.0.0.1:8000/tracker/api/locations/
```

---

### 6. Get Group Locations
**GET** `/api/group/{group_id}/locations/`

Returns all locations for a specific group.

#### Parameters
- `group_id` (string): Group identifier (A, A1, A2, B, B1, B2, C1, C2)

#### Response
```json
[
  {
    "group_id": "A1",
    "region": "Southern Region",
    "location": "Zomba", 
    "affected_areas": "Old Naisi Naisi Jokala Sakata Naming'azi..."
  },
  {
    "group_id": "A1",
    "region": "Central Region",
    "location": "Lilongwe B",
    "affected_areas": "Area 47 Mtandire Mtsiriza Piyasani and Gateway Shopping Mall"
  }
]
```

#### Example
```bash
curl http://127.0.0.1:8000/tracker/api/group/A1/locations/
```

---

### 7. Get Group Blackout Schedule
**GET** `/api/group/{group_id}/blackout-schedule/`

Returns blackout schedules for a specific group.

#### Parameters
- `group_id` (string): Group identifier (A, A1, A2, B, B1, B2, C1, C2)

#### Response
```json
[
  {
    "group_id": "A",
    "date": "2025-08-22",
    "start_time": "05:00:00", 
    "end_time": "09:30:00"
  },
  {
    "group_id": "A",
    "date": "2025-08-22",
    "start_time": "16:00:00",
    "end_time": "21:00:00" 
  }
]
```

#### Error Response
```json
{
  "error": "Group not found"
}
```

#### Example
```bash
curl http://127.0.0.1:8000/tracker/api/group/A/blackout-schedule/
```

---

## User Flow Examples

### Scenario 1: User knows their region
1. **GET** `/api/regions/` - Get all regions
2. **GET** `/api/region/Central Region/locations/` - Get locations in Central Region  
3. Find your location and note the group_id
4. **GET** `/api/group/{group_id}/blackout-schedule/` - Get schedule

### Scenario 2: User knows their area name
1. **GET** `/api/search/?q=Area 25` - Search directly for your area
2. Response includes group info and schedules

### Scenario 3: User knows their location name
1. **GET** `/api/location/Lilongwe A/schedule/` - Get schedule directly

### Scenario 4: User wants to browse all options
1. **GET** `/api/locations/` - See all available locations
2. Find your location and note the group_id
3. **GET** `/api/group/{group_id}/blackout-schedule/` - Get schedule

---

## Error Handling

### HTTP Status Codes
- `200` - Success
- `400` - Bad Request (missing required parameters)
- `404` - Not Found (group, location, or region not found)
- `500` - Internal Server Error

### Error Response Format
```json
{
  "error": "Description of the error"
}
```

---

## Rate Limiting
Currently no rate limiting is implemented. For production use, consider implementing rate limiting to prevent abuse.

---

## Authentication
Currently no authentication is required. All endpoints are publicly accessible.

---

## Content Type
All responses are in JSON format with `Content-Type: application/json`.

---

## Examples in Different Languages

### JavaScript (Fetch API)
```javascript
// Search for an area
fetch('http://127.0.0.1:8000/tracker/api/search/?q=Area 48')
  .then(response => response.json())
  .then(data => console.log(data));

// Get schedule by location
fetch('http://127.0.0.1:8000/tracker/api/location/Lilongwe A/schedule/')
  .then(response => response.json()) 
  .then(data => console.log(data));
```

### Python (requests)
```python
import requests

# Search for an area
response = requests.get('http://127.0.0.1:8000/tracker/api/search/', 
                       params={'q': 'Area 48'})
data = response.json()

# Get schedule by location  
response = requests.get('http://127.0.0.1:8000/tracker/api/location/Lilongwe A/schedule/')
schedule = response.json()
```

### PHP (cURL)
```php
// Search for an area
$url = 'http://127.0.0.1:8000/tracker/api/search/?q=' . urlencode('Area 48');
$response = file_get_contents($url);
$data = json_decode($response, true);

// Get schedule by location
$url = 'http://127.0.0.1:8000/tracker/api/location/' . urlencode('Lilongwe A') . '/schedule/';
$response = file_get_contents($url);
$schedule = json_decode($response, true);
```

---

## Notes

1. **URL Encoding**: Always URL-encode location names and search queries that contain spaces or special characters.

2. **Case Sensitivity**: Location searches are case-insensitive, but exact matches work best.

3. **Partial Matching**: The search endpoint supports partial matching in affected areas.

4. **Empty Schedules**: If no blackout schedules exist for a group, the schedules array will be empty `[]`.

5. **Data Updates**: Schedule data needs to be manually updated through Django admin or management commands.
