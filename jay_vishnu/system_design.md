# System Design

## Mermaid Tool

This is an Architecture Diagram, and it’s the big picture of how your project actually works.

## Architecture Diagram

![Architecture Diagram](image.png)

## Database Design

THis is a Database Design designed using Mermaid tool

erDiagram
    USER ||--o{ REVIEW : writes
    USER ||--o{ FORUM_POST : creates
    USER ||--o{ COMMENT : posts
    
    Tourist ||--o{ REVIEW : receives
    Business_Listings ||--o{ REVIEW : receives
    
    FORUM_POST ||--o{ COMMENT : has
    COMMENT ||--o{ COMMENT : "replies to"

    USER {
        uuid id PK
        string username
        string email
        var date_of_birth
        string password_hash
        datetime created_at
    }

    Tourist {
        uuid id PK
        uuid location_id FK
        blob Image
        string title
        string description
        string address
        decimal entry_fee
        string opening_hours
    }

    Business_Listings {
        uuid id PK
        uuid location_id FK
        string business_type "Restaurant | Shop | Hotel"
        blob photo
        string contact_info
        string address
        boolean is_verified
    }

    EVENTS {
        uuid id PK
        uuid location_id FK
        blob event_image
        string event_name
        string description
        datetime start_time
        datetime end_time
        string oraganiser_info
        string ticket_url
    }

    REVIEW {
        uuid id PK
        uuid user_id FK
        uuid target_id FK "Polymorphic: Attraction or Listing"
        int rating "1-5"
        text content
        time_stamp created_at
    }

    FORUM_POST {
        uuid id PK
        uuid user_id FK
        string title
        text content
        string city_zone "North | South"
    }

    COMMENT {
        uuid id PK
        uuid forum_id FK
        uuid user_id FK
        text content
        int upvotes "0"
        int downvotes "0"
        boolean is_deleted 
        time_stamp created_at
    }


# API Design

## 1. Business Listings

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **GET** | `/v1/businesses` | Search businesses with filters (category, city, radius, sort) | **Public** |
| **GET** | `/v1/businesses/{slug}` | Get detailed info: hours, gallery, rating, and reviews | **Public** |
| **POST** | `/v1/businesses` | Submit a new listing (name, category, address, phone) | **User** |
| **PATCH** | `/v1/businesses/{id}` | Update specific fields of a listing | **Owner** |
| **DELETE** | `/v1/businesses/{id}` | Soft delete a listing (marks as inactive in DB) | **Owner** |
| **POST** | `/v1/businesses/{id}/media` | Upload up to 8 images (Multipart, jpg/png/webp) | **Owner** |
| **DELETE** | `/v1/businesses/{id}/media/{media_id}` | Remove photo and purge from cloud storage | **Owner** |
| **PUT** | `/v1/businesses/{id}/hours` | Full replacement of 7-day operating hours | **Owner** |
| **POST** | `/v1/businesses/{id}/claim` | Claim an unowned listing for admin verification | **User** |

## 2. Events

| Method | Endpoint | 








