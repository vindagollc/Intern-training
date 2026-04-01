# Database Design

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



