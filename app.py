import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import plotly.express as px
from supabase import create_client, Client
import os

# Set page config
st.set_page_config(
    page_title="Duka Profit Tracker",
    page_icon="📊",
    layout="wide"
)

# Initialize Supabase client
@st.cache_resource
def init_supabase():
    supabase_url = "https://dbwguevzaldnkveqfagd.supabase.co"
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_key:
        st.error("SUPABASE_KEY environment variable is required but not set.")
        st.stop()
    return create_client(supabase_url, supabase_key)

supabase = init_supabase()

# Authentication functions
def sign_up(email, password, shop_name):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
        })
        
        if response.user:
            # Create shop profile
            shop_result = supabase.table("shops").insert({
                "id": response.user.id,
                "shop_name": shop_name,
                "created_at": datetime.now().isoformat()
            }).execute()
            
            # Check if email confirmation is required
            if not response.session:
                return response, "Please check your email to confirm your account before signing in."
            
            return response, None
        elif hasattr(response, 'error') and response.error:
            return None, f"Sign up failed: {response.error.message}"
        else:
            return None, "Failed to create account - unknown error"
    except Exception as e:
        return None, f"Sign up error: {str(e)}"

def sign_in(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        if response.user and response.session:
            return response, None
        elif hasattr(response, 'error') and response.error:
            return None, f"Sign in failed: {response.error.message}"
        else:
            return None, "Sign in failed: Invalid credentials or unconfirmed email"
    except Exception as e:
        return None, f"Sign in error: {str(e)}"

def get_current_user():
    try:
        return supabase.auth.get_user()
    except:
        return None

def sign_out():
    supabase.auth.sign_out()
    if 'user_id' in st.session_state:
        del st.session_state['user_id']
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    st.rerun()

# Database functions
def get_products(user_id):
    try:
        response = supabase.table("products").select("*").eq("shop_id", user_id).execute()
        return pd.DataFrame(response.data)
    except:
        return pd.DataFrame()

def add_product(user_id, name, buying_price, selling_price):
    supabase.table("products").insert({
        "shop_id": user_id,
        "name": name,
        "buying_price": buying_price,
        "selling_price": selling_price,
        "created_at": datetime.now().isoformat()
    }).execute()

def update_stock(user_id, product_id, quantity, stock_date):
    supabase.table("stock").insert({
        "shop_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "date": stock_date.isoformat(),
        "created_at": datetime.now().isoformat()
    }).execute()

def record_sale(user_id, product_id, quantity, sale_date):
    supabase.table("sales").insert({
        "shop_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "date": sale_date.isoformat(),
        "created_at": datetime.now().isoformat()
    }).execute()

def get_daily_profit(user_id, target_date):
    try:
        # Get sales for the day
        sales_response = supabase.table("sales").select("*, products(name, buying_price, selling_price)").eq("shop_id", user_id).eq("date", target_date.isoformat()).execute()
        
        sales_data = sales_response.data
        if not sales_data:
            return 0, pd.DataFrame()
            
        # Process sales data
        sales_list = []
        total_profit = 0
        
        for sale in sales_data:
            product_info = sale.get('products', {})
            buying_price = product_info.get('buying_price', 0)
            selling_price = product_info.get('selling_price', 0)
            quantity = sale.get('quantity', 0)
            
            profit = (selling_price - buying_price) * quantity
            total_profit += profit
            
            sales_list.append({
                'name': product_info.get('name', 'Unknown'),
                'buying_price': buying_price,
                'selling_price': selling_price,
                'sold_quantity': quantity,
                'profit': profit
            })
        
        return total_profit, pd.DataFrame(sales_list)
    except Exception as e:
        st.error(f"Error calculating profit: {e}")
        return 0, pd.DataFrame()

def get_sales_report(user_id, start_date, end_date):
    try:
        response = supabase.table("sales").select("*, products(name, buying_price, selling_price)").eq("shop_id", user_id).gte("date", start_date.isoformat()).lte("date", end_date.isoformat()).execute()
        
        sales_data = response.data
        if not sales_data:
            return pd.DataFrame()
            
        processed_data = []
        for sale in sales_data:
            product_info = sale.get('products', {})
            processed_data.append({
                'date': sale.get('date'),
                'name': product_info.get('name', 'Unknown'),
                'buying_price': product_info.get('buying_price', 0),
                'selling_price': product_info.get('selling_price', 0),
                'quantity': sale.get('quantity', 0),
                'profit': (product_info.get('selling_price', 0) - product_info.get('buying_price', 0)) * sale.get('quantity', 0)
            })
        
        return pd.DataFrame(processed_data)
    except Exception as e:
        st.error(f"Error generating report: {e}")
        return pd.DataFrame()

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

# Authentication UI
def show_auth():
    st.title("📊 Duka Profit Tracker")
    st.markdown("**Track your daily profits with ease**")
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        with st.form("sign_in_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign In")
            
            if submitted:
                if email and password:
                    response, error = sign_in(email, password)
                    if error:
                        st.error(f"Sign in failed: {error}")
                    elif response and response.user:
                        st.session_state['authenticated'] = True
                        st.session_state['user_id'] = response.user.id
                        st.success("Successfully signed in!")
                        st.rerun()
                    else:
                        st.error("Sign in failed: Invalid response")
                else:
                    st.error("Please enter both email and password")
    
    with tab2:
        with st.form("sign_up_form"):
            shop_name = st.text_input("Shop Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Create Account")
            
            if submitted:
                if shop_name and email and password:
                    response, error = sign_up(email, password, shop_name)
                    if error:
                        if "check your email" in error.lower():
                            st.info(error)
                        else:
                            st.error(error)
                    else:
                        st.success("Account created successfully! You can now sign in.")
                else:
                    st.error("Please fill all fields")

# Main app UI
def show_app():
    user_id = st.session_state['user_id']
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Dashboard", "Add Products", "Update Stock", "Record Sales", "View Reports"])
    
    # User info and logout
    st.sidebar.markdown("---")
    try:
        shop_info = supabase.table("shops").select("shop_name").eq("id", user_id).execute()
        shop_name = shop_info.data[0]["shop_name"] if shop_info.data else "Your Shop"
        st.sidebar.write(f"Logged in as: **{shop_name}**")
    except:
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

# Main app logic
def main():
    if not st.session_state['authenticated']:
        show_auth()
    else:
        show_app()

if __name__ == "__main__":
    main()
