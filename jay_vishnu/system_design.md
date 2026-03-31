# System Design

## Mermaid Tool

This is an Architecture Diagram, and it’s the big picture of how your project actually works.

## Architecture Diagram

![Architecture Diagram](image.png)

## Database Design

THis is a Database Design designed using Mermaid tool

![Database Design ER Diagram](image-2.png)


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








