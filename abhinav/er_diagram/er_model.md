# Database Design

<!-- ![alt text](image.png) -->


```mermaid
erDiagram
    USER ||--o{ REVIEW : writes
    USER ||--o{ FORUM_POST : creates
    USER ||--o{ COMMENT : posts
    
    LOCATION ||--o{ ATTRACTION : categorizes
    LOCATION ||--o{ LISTING : categorizes
    LOCATION ||--o{ EVENT : hosts
    
    ATTRACTION ||--o{ REVIEW : receives
    LISTING ||--o{ REVIEW : receives
    
    FORUM_POST ||--o{ COMMENT : has
    COMMENT ||--o{ COMMENT : replies_to

    USER {
        uuid id PK
        string username
        string email
        string password_hash
        datetime created_at
    }

    LOCATION {
        uuid id PK
        string name
        string address
        float latitude
        float longitude
        string category_type
    }

    ATTRACTION {
        uuid id PK
        uuid location_id FK
        blob photo
        string title
        string description
        string address
        decimal entry_fee
        string opening_hours
    }

    LISTING {
        uuid id PK
        uuid location_id FK
        string business_type
        blob photo
        string contact_info
        string address
        boolean is_verified
    }

    EVENT {
        uuid id PK
        uuid location_id FK
        blob event_image
        string event_name
        string description
        datetime start_time
        datetime end_time
        string organiser_info
        string ticket_url
    }

    REVIEW {
        uuid id PK
        uuid user_id FK
        uuid target_id FK
        int rating
        text content
        datetime created_at
    }

    FORUM_POST {
        uuid id PK
        uuid user_id FK
        string title
        text content
        string city_zone
    }

    COMMENT {
        uuid id PK
        uuid forum_id FK
        uuid user_id FK
        text content
        int upvotes
        int downvotes
        boolean is_deleted 
        datetime created_at
    }



# API Design


## 1. API Endpoints (REST)

### Users
| Method | Endpoint | Success Code | Body Parameters |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | `201 Created` | `username`, `email`, `password_hash` |
| `GET` | `/users/:id` | `200 OK` | - |

### Locations & Content
| Method | Endpoint | Success Code | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/locations` | `200 OK` | List all locations |
| `GET` | `/locations/:id/attractions` | `200 OK` | Get attractions for a specific location |
| `GET` | `/locations/:id/listings` | `200 OK` | Get listings for a specific location |
| `GET` | `/locations/:id/events` | `200 OK` | Get events for a specific location |

### Details
| Method | Endpoint | Success Code | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/attractions/:id` | `200 OK` | Fetch specific attraction details |
| `GET` | `/listings/:id` | `200 OK` | Fetch specific business listing details |
| `GET` | `/events/:id` | `200 OK` | Fetch specific event details |

### Community & Engagement
| Method | Endpoint | Success Code | Body Parameters |
| :--- | :--- | :--- | :--- |
| `POST` | `/reviews` | `201 Created` | `user_id`, `target_id`, `rating`, `content` |
| `GET` | `/forum-posts` | `200 OK` | Query param: `city_zone` |
| `POST` | `/forum-posts/:id/comments` | `201 Created` | `user_id`, `content` |
| `PATCH` | `/comments/:id` | `200 OK` | `upvotes`, `downvotes`, `is_deleted` |


## 2. Operations & Logic

### Polymorphic Reviews
- The `target_id` in the `REVIEW` table must be validated against both `ATTRACTION.id` and `LISTING.id`. 
- One user can write multiple reviews (`USER ||--o{ REVIEW`).

### Nested Conversations
- `COMMENT` has a self-relationship (`COMMENT ||--o{ COMMENT`). 
- When fetching comments for a `FORUM_POST`, the API should structure the JSON to represent "replies to" logic using the `id` references.

### Soft Deletion
- For `COMMENT`, do not use a `DELETE` operation. Use `PATCH` to set `is_deleted = true`. This preserves the database row while signaling the UI to hide the `content`.

---

## 3. Error Handling & Constraints

### Validation Errors (HTTP 400)
- **Rating**: Must be an integer between `1` and `5`.
- **Enums**: 
    - `category_type` must be exactly "Attraction", "Listing", or "Event".
    - `business_type` must be "Restaurant", "Shop", or "Hotel".
    - `city_zone` must be "North" or "South".
- **Time Logic**: In `EVENT`, `end_time` cannot be earlier than `start_time`.

### Integrity Errors (HTTP 404/409)
- **Foreign Keys**: Returns error if `location_id`, `user_id`, or `forum_id` does not exist during creation.
- **Uniqueness**: Returns error if `email` or `username` already exists in the `USER` table.

### Content Errors (HTTP 413/500)
- **BLOB Handling**: Errors related to file size for `photo` or `event_image` payloads.