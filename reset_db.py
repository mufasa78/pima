#!/usr/bin/env python3
"""
Database reset script for Pima app with NeonDB PostgreSQL
Run this script to drop all tables and recreate the schema.
WARNING: This will delete all data!
"""

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def reset_database():
    """Drop all tables and recreate the schema."""
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print("ERROR: DATABASE_URL environment variable is not set!")
        return False
    
    # Get user confirmation
    confirmation = input("⚠️  WARNING: This will delete ALL data in your database!\nType 'RESET' to confirm: ")
    if confirmation != "RESET":
        print("❌ Operation cancelled.")
        return False
    
    try:
        # Connect to database
        print("Connecting to NeonDB PostgreSQL...")
        conn = psycopg2.connect(database_url)
        
        # Drop existing tables in correct order (respecting foreign keys)
        print("Dropping existing tables...")
        drop_sql = """
        DROP TABLE IF EXISTS sales CASCADE;
        DROP TABLE IF EXISTS stock CASCADE;
        DROP TABLE IF EXISTS products CASCADE;
        DROP TABLE IF EXISTS shops CASCADE;
        DROP TABLE IF EXISTS users CASCADE;
        DROP FUNCTION IF EXISTS update_updated_at_column() CASCADE;
        """
        
        with conn.cursor() as cur:
            cur.execute(drop_sql)
            conn.commit()
        
        print("✅ Existing tables dropped successfully!")
        
        # Read and execute schema
        print("Reading schema.sql...")
        with open('schema.sql', 'r') as f:
            schema_sql = f.read()
        
        print("Creating new database schema...")
        with conn.cursor() as cur:
            cur.execute(schema_sql)
            conn.commit()
        
        print("✅ Database schema recreated successfully!")
        print("✅ Your Pima app database has been reset!")
        
        conn.close()
        return True
        
    except FileNotFoundError:
        print("ERROR: schema.sql file not found!")
        print("Make sure schema.sql exists in the current directory.")
        return False
    except Exception as e:
        print(f"ERROR: Failed to reset database: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Resetting Pima App Database...")
    print("=" * 50)
    
    success = reset_database()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 Database reset completed!")
        print("\nYour database is now clean and ready for fresh data.")
        print("You can start using the app with new registrations.")
    else:
        print("\n❌ Database reset failed!")
        print("Please check the error messages above and try again.")