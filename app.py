import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import plotly.express as px
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from typing import Optional, Tuple
import re
import bcrypt
from dotenv import load_dotenv
import uuid
import hashlib
import json

# Load environment variables from .env file
load_dotenv()

def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength.
    Returns (is_valid, message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, "Password is strong"

def validate_env_vars() -> Optional[str]:
    """Validate all required environment variables are set."""
    required_vars = {
        "DATABASE_URL": "PostgreSQL connection URL for NeonDB"
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"{var} ({description})")
    
    if missing_vars:
        return f"Missing required environment variables:\n" + "\n".join(missing_vars)
    return None

# Validate environment variables
if error_message := validate_env_vars():
    st.error(error_message)
    st.stop()

# Set page config
st.set_page_config(
    page_title="Pima",
    page_icon="📊",
    layout="wide"
)

# Session management functions
def init_session():
    """Initialize session state variables."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if 'user_id' not in st.session_state:
        st.session_state['user_id'] = None
    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = None
    if 'is_loading' not in st.session_state:
        st.session_state['is_loading'] = False

# Initialize session
init_session()

# Database connection functions
def get_db_connection():
    """Create and return a fresh database connection."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        st.error("DATABASE_URL environment variable is required but not set.")
        st.stop()
        
    try:
        conn = psycopg2.connect(database_url)
        return conn
    except Exception as e:
        st.error(f"Failed to connect to database: {e}")
        st.stop()

def execute_query(query: str, params: tuple = None, fetch: bool = False):
    """Execute a database query and return results if fetch=True."""
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            conn.commit()
            return cur.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def execute_query_one(query: str, params: tuple = None):
    """Execute a database query and return a single result."""
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# Authentication functions
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def sign_up(email: str, password: str, shop_name: str) -> Tuple[Optional[dict], Optional[str]]:
    """Create a new user account and shop."""
    try:
        # Check if user already exists
        existing_user = execute_query_one(
            "SELECT id FROM users WHERE email = %s",
            (email,)
        )
        
        if existing_user:
            return None, "An account with this email already exists"
        
        # Hash password
        password_hash = hash_password(password)
        
        # Create user
        user_id = str(uuid.uuid4())
        execute_query(
            "INSERT INTO users (id, email, password_hash) VALUES (%s, %s, %s)",
            (user_id, email, password_hash)
        )
        
        # Create shop
        execute_query(
            "INSERT INTO shops (id, shop_name) VALUES (%s, %s)",
            (user_id, shop_name)
        )
        
        user_data = {
            'id': user_id,
            'email': email,
            'shop_name': shop_name
        }
        
        return user_data, None
        
    except Exception as e:
        return None, f"Sign up failed: {str(e)}"

def sign_in(email: str, password: str) -> Tuple[Optional[dict], Optional[str]]:
    """Sign in a user with email and password."""
    try:
        # Get user by email
        user = execute_query_one(
            "SELECT u.id, u.email, u.password_hash, s.shop_name FROM users u LEFT JOIN shops s ON u.id = s.id WHERE u.email = %s",
            (email,)
        )
        
        if not user:
            return None, "Invalid email or password"
        
        # Verify password
        if not verify_password(password, user['password_hash']):
            return None, "Invalid email or password"
        
        user_data = {
            'id': user['id'],
            'email': user['email'],
            'shop_name': user['shop_name']
        }
        
        return user_data, None
        
    except Exception as e:
        return None, f"Sign in failed: {str(e)}"

def get_current_user() -> Optional[dict]:
    """Get current user from session state."""
    try:
        # Check session state
        if st.session_state.get('authenticated') and st.session_state.get('user_id'):
            # Return cached user data if available
            if st.session_state.get('user_data'):
                return st.session_state['user_data']
            
            # Fetch user data from database
            user_id = st.session_state['user_id']
            user = execute_query_one(
                "SELECT u.id, u.email, s.shop_name FROM users u LEFT JOIN shops s ON u.id = s.id WHERE u.id = %s",
                (user_id,)
            )
            
            # Cache user data in session
            if user:
                st.session_state['user_data'] = user
            
            return user
        
        return None
        
    except Exception:
        return None

def sign_out():
    """Sign out the current user."""
    # Clear all session state
    st.session_state['authenticated'] = False
    st.session_state['user_id'] = None
    st.session_state['user_data'] = None
    st.session_state['is_loading'] = False
    
    # Clear any other session keys that might exist
    keys_to_clear = [k for k in st.session_state.keys() if k.startswith('user_') or k in ['authenticated']]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    
    st.rerun()

# Database functions
def get_products(user_id: str) -> pd.DataFrame:
    """Get all products for a shop."""
    try:
        products = execute_query(
            "SELECT id, name, buying_price, selling_price, created_at FROM products WHERE shop_id = %s ORDER BY created_at DESC",
            (user_id,),
            fetch=True
        )
        return pd.DataFrame(products)
    except Exception as e:
        st.error(f"Error fetching products: {e}")
        return pd.DataFrame()

def add_product(user_id: str, name: str, buying_price: float, selling_price: float):
    """Add a new product to the shop."""
    execute_query(
        "INSERT INTO products (shop_id, name, buying_price, selling_price) VALUES (%s, %s, %s, %s)",
        (user_id, name, buying_price, selling_price)
    )

def update_stock(user_id: str, product_id: str, quantity: int, stock_date: date):
    """Update stock for a product."""
    execute_query(
        "INSERT INTO stock (shop_id, product_id, quantity, date) VALUES (%s, %s, %s, %s)",
        (user_id, product_id, quantity, stock_date)
    )

def record_sale(user_id: str, product_id: str, quantity: int, sale_date: date):
    """Record a sale."""
    execute_query(
        "INSERT INTO sales (shop_id, product_id, quantity, date) VALUES (%s, %s, %s, %s)",
        (user_id, product_id, quantity, sale_date)
    )

def get_daily_profit(user_id: str, target_date: date) -> Tuple[float, pd.DataFrame]:
    """Get daily profit and sales details for a specific date."""
    try:
        # Get sales for the day with product information
        sales_data = execute_query(
            """
            SELECT s.quantity, p.name, p.buying_price, p.selling_price
            FROM sales s
            JOIN products p ON s.product_id = p.id
            WHERE s.shop_id = %s AND s.date = %s
            ORDER BY s.created_at DESC
            """,
            (user_id, target_date),
            fetch=True
        )
        
        if not sales_data:
            return 0, pd.DataFrame()
        
        # Process sales data
        sales_list = []
        total_profit = 0
        
        for sale in sales_data:
            profit = (sale['selling_price'] - sale['buying_price']) * sale['quantity']
            total_profit += profit
            
            sales_list.append({
                'name': sale['name'],
                'buying_price': float(sale['buying_price']),
                'selling_price': float(sale['selling_price']),
                'sold_quantity': sale['quantity'],
                'profit': profit
            })
        
        return total_profit, pd.DataFrame(sales_list)
        
    except Exception as e:
        st.error(f"Error calculating profit: {e}")
        return 0, pd.DataFrame()

def get_sales_report(user_id: str, start_date: date, end_date: date) -> pd.DataFrame:
    """Get sales report for a date range."""
    try:
        sales_data = execute_query(
            """
            SELECT s.date, s.quantity, p.name, p.buying_price, p.selling_price
            FROM sales s
            JOIN products p ON s.product_id = p.id
            WHERE s.shop_id = %s AND s.date >= %s AND s.date <= %s
            ORDER BY s.date DESC, s.created_at DESC
            """,
            (user_id, start_date, end_date),
            fetch=True
        )
        
        if not sales_data:
            return pd.DataFrame()
        
        processed_data = []
        for sale in sales_data:
            profit = (float(sale['selling_price']) - float(sale['buying_price'])) * sale['quantity']
            processed_data.append({
                'date': sale['date'],
                'name': sale['name'],
                'buying_price': float(sale['buying_price']),
                'selling_price': float(sale['selling_price']),
                'quantity': sale['quantity'],
                'profit': profit
            })
        
        return pd.DataFrame(processed_data)
        
    except Exception as e:
        st.error(f"Error generating report: {e}")
        return pd.DataFrame()



# Authentication UI
def show_auth():
    st.title("📊 Pima")
    st.markdown("**Track your daily profits with ease**")
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        with st.form("sign_in_form"):
            email = st.text_input("Email", placeholder="Enter your email address")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Sign In")
            
            if submitted:
                if email and password:
                    with st.spinner("Signing in..."):
                        st.session_state['is_loading'] = True
                        response, error = sign_in(email, password)
                        st.session_state['is_loading'] = False
                        
                        if error:
                            st.error(f"Sign in failed: {error}")
                        elif response:
                            st.session_state['authenticated'] = True
                            st.session_state['user_id'] = response['id']
                            st.session_state['user_data'] = response
                            st.success("Successfully signed in!")
                            st.rerun()
                        else:
                            st.error("Sign in failed: Invalid response")
                else:
                    st.error("Please enter both email and password")
    
    with tab2:
        with st.form("sign_up_form"):
            shop_name = st.text_input("Shop Name", placeholder="Enter your shop name")
            email = st.text_input("Email", placeholder="Enter your email address")
            password = st.text_input("Password", type="password", placeholder="Create a strong password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")
            st.markdown("""
            Password requirements:
            - At least 8 characters long
            - Must contain uppercase and lowercase letters
            - Must contain at least one number
            - Must contain at least one special character
            """)
            submitted = st.form_submit_button("Create Account")
            
            if submitted:
                if not all([shop_name, email, password, confirm_password]):
                    st.error("Please fill all fields")
                elif password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    # Validate password
                    is_valid, message = validate_password(password)
                    if not is_valid:
                        st.error(message)
                    else:
                        # Validate email format
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                            st.error("Please enter a valid email address")
                        else:
                            response, error = sign_up(email, password, shop_name)
                            if error:
                                st.error(error)
                            elif response:
                                st.session_state['authenticated'] = True
                                st.session_state['user_id'] = response['id']
                                st.session_state['user_data'] = response
                                st.success("Account created successfully!")
                                st.rerun()

# Main app UI
def show_app():
    user_id = st.session_state['user_id']
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Dashboard", "Add Products", "Update Stock", "Record Sales", "View Reports"])
    
    # User info and logout
    st.sidebar.markdown("---")
    try:
        user = get_current_user()
        shop_name = user['shop_name'] if user and user['shop_name'] else "Your Shop"
        st.sidebar.write(f"Logged in as: **{shop_name}**")
    except Exception:
        st.sidebar.write("Logged in")
    
    if st.sidebar.button("Sign Out"):
        sign_out()
    
    # Dashboard
    if menu == "Dashboard":
        st.header("Dashboard")
        
        # Date selector
        selected_date = st.date_input("Select date", value=date.today())
        
        # Display daily profit
        profit, sales_details = get_daily_profit(user_id, selected_date)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Selected Date", selected_date.strftime("%B %d, %Y"))
        
        with col2:
            st.metric("Total Sales", f"{len(sales_details)} products" if not sales_details.empty else "0 products")
        
        with col3:
            st.metric("Daily Profit", f"KSh {profit:,.2f}")
        
        # Display sales details
        if not sales_details.empty:
            st.subheader("Sales Details")
            display_df = sales_details[['name', 'buying_price', 'selling_price', 'sold_quantity', 'profit']].copy()
            display_df.columns = ['Product', 'Buying Price (KSh)', 'Selling Price (KSh)', 'Quantity Sold', 'Profit (KSh)']
            st.dataframe(display_df, use_container_width=True)
            
            # Visualization
            if len(sales_details) > 0:
                fig = px.bar(sales_details, x='name', y='profit', title='Profit by Product')
                fig.update_layout(xaxis_title='Product', yaxis_title='Profit (KSh)')
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No sales recorded for selected date.")

    # Add Products
    elif menu == "Add Products":
        st.header("Add New Products")
        
        with st.form("product_form"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                name = st.text_input("Product Name")
            
            with col2:
                buying_price = st.number_input("Buying Price (KSh)", min_value=0.0, step=10.0, format="%.2f")
            
            with col3:
                selling_price = st.number_input("Selling Price (KSh)", min_value=0.0, step=10.0, format="%.2f")
            
            submitted = st.form_submit_button("Add Product")
            
            if submitted:
                if name and selling_price > buying_price:
                    try:
                        add_product(user_id, name, buying_price, selling_price)
                        st.success(f"Product '{name}' added successfully!")
                    except Exception as e:
                        st.error(f"Error adding product: {e}")
                elif selling_price <= buying_price:
                    st.error("Selling price must be higher than buying price!")
                else:
                    st.error("Please fill all fields!")
        
        # Display existing products
        st.subheader("Existing Products")
        products_df = get_products(user_id)
        
        if not products_df.empty:
            display_products = products_df[['name', 'buying_price', 'selling_price']].copy()
            display_products.columns = ['Product Name', 'Buying Price (KSh)', 'Selling Price (KSh)']
            st.dataframe(display_products, use_container_width=True)
        else:
            st.info("No products added yet.")

    # Update Stock
    elif menu == "Update Stock":
        st.header("Update Stock Levels")
        
        products_df = get_products(user_id)
        
        if not products_df.empty:
            with st.form("stock_form"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    product_names = products_df['name'].tolist()
                    selected_product = st.selectbox("Select Product", product_names)
                    product_id_map = dict(zip(products_df['name'], products_df['id']))
                    product_id = product_id_map.get(selected_product)
                    if product_id is None:
                        st.error("Product not found")
                        st.stop()
                
                with col2:
                    quantity = st.number_input("Quantity", min_value=1, step=1)
                
                with col3:
                    stock_date = st.date_input("Stock Date", value=date.today())
                
                submitted = st.form_submit_button("Update Stock")
                
                if submitted:
                    try:
                        update_stock(user_id, product_id, quantity, stock_date)
                        st.success(f"Stock updated for '{selected_product}'!")
                    except Exception as e:
                        st.error(f"Error updating stock: {e}")
        else:
            st.info("Please add products first before updating stock.")

    # Record Sales
    elif menu == "Record Sales":
        st.header("Record Sales")
        
        products_df = get_products(user_id)
        
        if not products_df.empty:
            with st.form("sales_form"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    product_names = products_df['name'].tolist()
                    selected_product = st.selectbox("Select Product", product_names)
                    product_id_map = dict(zip(products_df['name'], products_df['id']))
                    product_id = product_id_map.get(selected_product)
                    if product_id is None:
                        st.error("Product not found")
                        st.stop()
                
                with col2:
                    quantity = st.number_input("Quantity Sold", min_value=1, step=1)
                
                with col3:
                    sale_date = st.date_input("Sale Date", value=date.today())
                
                submitted = st.form_submit_button("Record Sale")
                
                if submitted:
                    try:
                        record_sale(user_id, product_id, quantity, sale_date)
                        st.success(f"Sale recorded for '{selected_product}'!")
                    except Exception as e:
                        st.error(f"Error recording sale: {e}")
        else:
            st.info("Please add products first before recording sales.")

    # View Reports
    elif menu == "View Reports":
        st.header("Advanced Sales Reports")
        
        # Report filters
        st.subheader("Report Filters")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            start_date = st.date_input("Start Date", value=date.today().replace(day=1))
        
        with col2:
            end_date = st.date_input("End Date", value=date.today())
        
        with col3:
            # Product filter
            products_df = get_products(user_id)
            product_options = ["All Products"] + products_df['name'].tolist() if not products_df.empty else ["All Products"]
            selected_product_filter = st.selectbox("Filter by Product", product_options)
        
        # Quick date range buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("Today"):
                start_date = end_date = date.today()
                st.rerun()
        
        with col2:
            if st.button("This Week"):
                end_date = date.today()
                start_date = end_date - timedelta(days=6)
                st.rerun()
        
        with col3:
            if st.button("This Month"):
                end_date = date.today()
                start_date = end_date.replace(day=1)
                st.rerun()
        
        with col4:
            if st.button("Last 30 Days"):
                end_date = date.today()
                start_date = end_date - timedelta(days=29)
                st.rerun()
        
        if st.button("Generate Advanced Report", type="primary"):
            if start_date <= end_date:
                report_df = get_sales_report(user_id, start_date, end_date)
                
                # Apply product filter
                if selected_product_filter != "All Products" and not report_df.empty:
                    report_df = report_df[report_df['name'] == selected_product_filter]
                
                if not report_df.empty:
                    st.subheader(f"Sales Report: {start_date} to {end_date}")
                    if selected_product_filter != "All Products":
                        st.caption(f"Filtered by: {selected_product_filter}")
                    
                    # Enhanced summary metrics
                    total_sales = len(report_df)
                    total_profit = report_df['profit'].sum()
                    total_revenue = (report_df['selling_price'] * report_df['quantity']).sum()
                    total_cost = (report_df['buying_price'] * report_df['quantity']).sum()
                    avg_profit_per_sale = total_profit / total_sales if total_sales > 0 else 0
                    profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
                    
                    # Display metrics in cards
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Total Sales", total_sales)
                        st.metric("Total Revenue", f"KSh {total_revenue:,.2f}")
                    
                    with col2:
                        st.metric("Total Profit", f"KSh {total_profit:,.2f}")
                        st.metric("Total Cost", f"KSh {total_cost:,.2f}")
                    
                    with col3:
                        st.metric("Avg Profit/Sale", f"KSh {avg_profit_per_sale:,.2f}")
                        st.metric("Profit Margin", f"{profit_margin:.1f}%")
                    
                    st.markdown("---")
                    
                    # Export functionality
                    st.subheader("Export Data")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # CSV export
                        csv_data = report_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv_data,
                            file_name=f"sales_report_{start_date}_{end_date}.csv",
                            mime="text/csv"
                        )
                    
                    with col2:
                        # Summary export
                        summary_data = f"""Sales Report Summary
Period: {start_date} to {end_date}
Product Filter: {selected_product_filter}

Key Metrics:
- Total Sales: {total_sales}
- Total Revenue: KSh {total_revenue:,.2f}
- Total Profit: KSh {total_profit:,.2f}
- Total Cost: KSh {total_cost:,.2f}
- Average Profit per Sale: KSh {avg_profit_per_sale:,.2f}
- Profit Margin: {profit_margin:.1f}%

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
                        st.download_button(
                            label="📋 Download Summary",
                            data=summary_data,
                            file_name=f"sales_summary_{start_date}_{end_date}.txt",
                            mime="text/plain"
                        )
                    
                    # Enhanced visualizations
                    st.subheader("Analytics Charts")
                    
                    # Daily profit trend
                    if len(report_df) > 0:
                        daily_profit = report_df.groupby('date')['profit'].sum().reset_index()
                        daily_revenue = report_df.groupby('date').apply(lambda x: (x['selling_price'] * x['quantity']).sum()).reset_index()
                        daily_revenue.columns = ['date', 'revenue']
                        
                        tab1, tab2, tab3 = st.tabs(["Profit Trend", "Product Performance", "Revenue vs Cost"])
                        
                        with tab1:
                            fig = px.line(daily_profit, x='date', y='profit', title='Daily Profit Trend', markers=True)
                            fig.update_layout(xaxis_title='Date', yaxis_title='Profit (KSh)')
                            st.plotly_chart(fig, use_container_width=True)
                        
                        with tab2:
                            # Product performance
                            product_performance = report_df.groupby('name').agg({
                                'profit': 'sum',
                                'quantity': 'sum'
                            }).reset_index().sort_values('profit', ascending=False)
                            
                            fig2 = px.bar(product_performance, x='name', y='profit', title='Profit by Product')
                            fig2.update_layout(xaxis_title='Product', yaxis_title='Total Profit (KSh)')
                            st.plotly_chart(fig2, use_container_width=True)
                            
                            # Top products table
                            st.subheader("Top Performing Products")
                            top_products = product_performance.head(10).copy()
                            top_products.columns = ['Product', 'Total Profit (KSh)', 'Total Quantity Sold']
                            st.dataframe(top_products, use_container_width=True)
                        
                        with tab3:
                            # Revenue vs Cost analysis
                            daily_analysis = report_df.groupby('date').agg({
                                'profit': 'sum'
                            }).reset_index()
                            
                            # Calculate revenue and cost separately
                            daily_revenue = report_df.groupby('date').apply(
                                lambda x: (x['selling_price'] * x['quantity']).sum()
                            ).to_frame('revenue').reset_index()
                            
                            daily_cost = report_df.groupby('date').apply(
                                lambda x: (x['buying_price'] * x['quantity']).sum()
                            ).to_frame('cost').reset_index()
                            
                            # Merge all metrics
                            daily_analysis = daily_analysis.merge(daily_revenue, on='date').merge(daily_cost, on='date')
                            
                            fig3 = px.line(daily_analysis, x='date', y=['revenue', 'cost'], title='Daily Revenue vs Cost')
                            fig3.update_layout(xaxis_title='Date', yaxis_title='Amount (KSh)')
                            st.plotly_chart(fig3, use_container_width=True)
                    
                    # Detailed report table
                    st.subheader("Detailed Sales Data")
                    display_columns = ['date', 'name', 'buying_price', 'selling_price', 'quantity', 'profit']
                    if len(report_df) > 0:
                        display_report = pd.DataFrame(report_df[display_columns])
                        display_report.columns = ['Date', 'Product', 'Buying Price (KSh)', 'Selling Price (KSh)', 'Quantity', 'Profit (KSh)']
                        st.dataframe(display_report, use_container_width=True)
                    else:
                        st.info("No detailed sales data to display.")
                    
                else:
                    st.info("No sales data found for the selected criteria.")
            else:
                st.error("End date must be after start date!")

# Check for existing session
def check_session():
    """Check if user has an active session."""
    try:
        user = get_current_user()
        if user and not st.session_state.get('authenticated'):
            st.session_state['authenticated'] = True
            st.session_state['user_id'] = user['id']
            return True
        return st.session_state.get('authenticated', False)
    except Exception:
        return False

# Main app logic
def main():
    if not check_session():
        show_auth()
    else:
        show_app()

if __name__ == "__main__":
    main()
