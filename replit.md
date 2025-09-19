# Duka Profit Tracker

## Overview

Duka Profit Tracker is a multi-shop SaaS application built with Streamlit that allows shop owners to track their daily profits and business performance. The application provides authentication, data visualization, and profit tracking capabilities for multiple independent shop owners. Users can register their shops, log daily profits, and view analytics through interactive charts and dashboards.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web application framework
- **UI Components**: Native Streamlit components with custom CSS styling
- **Data Visualization**: Plotly Express for interactive charts and graphs
- **Layout**: Wide layout configuration optimized for dashboard viewing
- **State Management**: Streamlit's built-in session state and caching mechanisms

### Backend Architecture
- **Authentication System**: Supabase Auth for user registration and login
- **Database Operations**: Direct Supabase client integration for CRUD operations
- **Data Models**: 
  - Shops table for storing shop information and owner details
  - Profit tracking tables for daily business metrics
- **Session Management**: Cookie-based session persistence with encryption
- **API Integration**: RESTful communication with Supabase backend

### Data Storage
- **Primary Database**: Supabase (PostgreSQL-based)
- **Authentication**: Supabase Auth service
- **Data Structure**: Relational model linking shops to their profit records
- **Real-time Features**: Supabase real-time subscriptions capability

### Security Architecture
- **Environment Variables**: Sensitive keys stored as environment variables
- **Authentication Flow**: Email/password authentication with Supabase
- **Session Security**: Encrypted cookie management for session persistence
- **Data Isolation**: Shop-specific data access patterns

## External Dependencies

### Core Services
- **Supabase**: Backend-as-a-Service providing authentication, database, and real-time features
- **Streamlit**: Python web application framework for rapid prototyping and deployment

### Python Packages
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive data visualization
- **supabase-py**: Official Python client for Supabase
- **extra-streamlit-components**: Extended UI components for Streamlit
- **streamlit-cookies-manager**: Secure cookie management for session persistence

### Configuration Requirements
- **SUPABASE_KEY**: API key for Supabase project access
- **SUPABASE_URL**: Project-specific Supabase endpoint
- **COOKIE_PASSWORD**: Encryption key for secure cookie management

### Database Schema
- **shops** table: User profiles and shop information
- **profit_records** table: Daily profit tracking data with foreign key relationships to shops
- Built-in Supabase auth tables for user management