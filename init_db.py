#!/usr/bin/env python3
"""
Database initialization script for Pima app with NeonDB PostgreSQL
Run this script to create the database schema.
"""

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_database():
    """Initialize the database with the schema."""
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print("ERROR: DATABASE_URL environment variable is not set!")
        return False
    
    try:
        # Connect to database
        print("Connecting to NeonDB PostgreSQL...")
        conn = psycopg2.connect(database_url)
        
        # Read schema file
        print("Reading schema.sql...")
        with open('schema.sql', 'r') as f:
            schema_sql = f.read()
        
        # Execute schema
        print("Creating database schema...")
        with conn.cursor() as cur:
            cur.execute(schema_sql)
            conn.commit()
        
        print("✅ Database schema created successfully!")
        print("✅ Your Pima app is ready to use with NeonDB PostgreSQL!")
        
        conn.close()
        return True
        
    except FileNotFoundError:
        print("ERROR: schema.sql file not found!")
        print("Make sure schema.sql exists in the current directory.")
        return False
    except Exception as e:
        print(f"ERROR: Failed to initialize database: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Initializing Pima App Database...")
    print("=" * 50)
    
    success = init_database()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 Database initialization completed!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Update your .env file with a strong COOKIE_PASSWORD")
        print("3. Run the app: streamlit run app.py --server.port 8502")
    else:
        print("\n❌ Database initialization failed!")
        print("Please check the error messages above and try again.")