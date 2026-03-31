# 🏢 Business & Media API Specification

## 1. Business Directory
These endpoints handle the discovery and lifecycle of business listings.

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **GET** | `/v1/businesses` | Search businesses with filters (category, city, radius, sort) | **Public** |
| **GET** | `/v1/businesses/{slug}` | Get detailed info: hours, gallery, rating, and reviews | **Public** |
| **POST** | `/v1/businesses` | Submit a new listing (name, category, address, phone) | **User** |
| **PATCH** | `/v1/businesses/{id}` | Update specific fields of a listing | **Owner** |
| **DELETE** | `/v1/businesses/{id}` | Soft delete a listing (marks as inactive in DB) | **Owner** |

### 🔍 Search Query Parameters
The `GET /v1/businesses` endpoint supports the following parameters:
* `q`: Search keyword (string)
* `category_slug`: Filter by specific category (string)
* `city`: Filter by location (string)
* `lat` & `lng`: Coordinates for proximity search (float)
* `radius_km`: Distance from coordinates (integer)
* `verified`: Filter by verification status (boolean)

---

## 2. Media & Operating Hours
Handling rich media content and business availability.

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **POST** | `/v1/businesses/{id}/media` | Upload up to 8 images (Multipart, jpg/png/webp) | **Owner** |
| **DELETE** | `/v1/businesses/{id}/media/{media_id}` | Remove photo and purge from cloud storage | **Owner** |
| **PUT** | `/v1/businesses/{id}/hours` | Full replacement of 7-day operating hours | **Owner** |
| **POST** | `/v1/businesses/{id}/claim` | Claim an unowned listing for admin verification | **User** |

---

## 💡 Implementation Notes

### Soft Delete vs. Hard Delete
The `DELETE /v1/businesses/{id}` is a **Soft Delete**. Instead of removing the row from the database, the API updates a `deleted_at` column. This allows the owner to recover the listing later if needed.

### The Claim Process
The `/claim` endpoint doesn't grant immediate ownership. It creates a "Verification Request" in the database that an admin must approve via the Admin Dashboard.

### Hours Management (PUT vs PATCH)
We use **PUT** for `/hours` because it is easier to send the entire 7-day schedule object at once rather than updating individual days.