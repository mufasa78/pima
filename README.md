# Pima# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
## Overview# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
Pima is a multi-shop SaaS application built with Streamlit that allows shop owners to track their daily profits and business performance. The application provides authentication, data visualization, and profit tracking capabilities for multiple independent shop owners. Users can register their shops, log daily profits, and view analytics through interactive charts and dashboards.# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
## User Preferences# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
Preferred communication style: Simple, everyday language.# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
## System Architecture# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Frontend Architecture# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Framework**: Streamlit web application framework# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **UI Components**: Native Streamlit components with custom CSS styling# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Data Visualization**: Plotly Express for interactive charts and graphs# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Layout**: Wide layout configuration optimized for dashboard viewing# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **State Management**: Streamlit's built-in session state and caching mechanisms# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Backend Architecture# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Authentication System**: Supabase Auth for user registration and login# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Database Operations**: Direct Supabase client integration for CRUD operations# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Data Models**: # Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
  - Shops table for storing shop information and owner details# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
  - Profit tracking tables for daily business metrics# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Session Management**: Cookie-based session persistence with encryption# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **API Integration**: RESTful communication with Supabase backend# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Data Storage# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Primary Database**: Supabase (PostgreSQL-based)# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Authentication**: Supabase Auth service# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Data Structure**: Relational model linking shops to their profit records# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Real-time Features**: Supabase real-time subscriptions capability# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Security Architecture# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Environment Variables**: Sensitive keys stored as environment variables# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Authentication Flow**: Email/password authentication with Supabase# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Session Security**: Encrypted cookie management for session persistence# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Data Isolation**: Shop-specific data access patterns# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
## External Dependencies# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Core Services# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Supabase**: Backend-as-a-Service providing authentication, database, and real-time features# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **Streamlit**: Python web application framework for rapid prototyping and deployment# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Python Packages# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **pandas**: Data manipulation and analysis# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **plotly**: Interactive data visualization# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **supabase-py**: Official Python client for Supabase# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **extra-streamlit-components**: Extended UI components for Streamlit# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **streamlit-cookies-manager**: Secure cookie management for session persistence# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Configuration Requirements# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **SUPABASE_KEY**: API key for Supabase project access# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **SUPABASE_URL**: Project-specific Supabase endpoint# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **COOKIE_PASSWORD**: Encryption key for secure cookie management# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
### Database Schema# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **shops** table: User profiles and shop information# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- **profit_records** table: Daily profit tracking data with foreign key relationships to shops# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
- Built-in Supabase auth tables for user management# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
# Pima - Multi-Shop SaaS Profit Tracking App

**Pima** is a multi-shop SaaS application designed to help shop owners track daily profits and analyze business performance. Built using Streamlit and powered by NeonDB PostgreSQL, it enables independent shop owners to manage their financial data through an intuitive dashboard.

## Features

- **User Authentication**: Secure registration and login system with bcrypt password hashing
- **Shop Management**: Register and manage shop profiles
- **Product Management**: Add and manage products with buying/selling prices
- **Inventory Tracking**: Track stock levels for products
- **Sales Recording**: Record daily sales transactions
- **Profit Analytics**: View daily, weekly, and monthly profit analysis
- **Interactive Dashboard**: Real-time visualizations with Plotly charts
- **Data Export**: Export sales reports to CSV and summary formats
- **Multi-tenant**: Data isolation between different shops

## Technology Stack

- **Frontend**: Streamlit (Python)
- **Backend**: NeonDB PostgreSQL
- **Authentication**: Custom bcrypt-based authentication
- **Data Visualization**: Plotly Express
- **Session Management**: Encrypted cookies
- **Database**: PostgreSQL with UUID primary keys

## Quick Start

### Prerequisites

- Python 3.9+
- NeonDB PostgreSQL account
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pima-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://your-neondb-connection-string
   COOKIE_PASSWORD=your-strong-encryption-key-change-this
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py --server.port 8502
   ```

6. **Access the app**:
   Open your browser and navigate to `http://localhost:8502`

## Database Schema

The application uses the following PostgreSQL tables:

- **users**: User authentication and account information
- **shops**: Shop profiles linked to users
- **products**: Product catalog with pricing
- **stock**: Inventory tracking
- **sales**: Sales transaction records

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `DATABASE_URL` | NeonDB PostgreSQL connection string | Yes |
| `COOKIE_PASSWORD` | Secret key for encrypting session cookies | Yes |

## Usage

### First Time Setup

1. Register a new account with your shop name, email, and password
2. Add your products with buying and selling prices
3. Start recording daily sales
4. View your profit analytics on the dashboard

### Daily Operations

1. **Record Sales**: Add daily sales transactions
2. **Update Stock**: Track inventory levels
3. **View Reports**: Analyze performance with interactive charts
4. **Export Data**: Download reports for external analysis

## Security Features

- **Password Hashing**: Secure bcrypt password hashing
- **Session Management**: Encrypted cookie-based sessions
- **Data Isolation**: PostgreSQL Row Level Security (RLS)
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: Parameterized queries

## Development

### Project Structure

```
pima-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── schema.sql            # Database schema definition
├── init_db.py            # Database initialization script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

### Database Management

- **Initialize**: `python init_db.py`
- **Reset**: Drop tables manually and re-run init script
- **Backup**: Use `pg_dump` with your NeonDB connection

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify your `DATABASE_URL` is correct
   - Check NeonDB connection limits
   - Ensure your IP is whitelisted (if required)

2. **Cookie/Session Issues**:
   - Generate a strong `COOKIE_PASSWORD`
   - Clear browser cookies if needed

3. **Permission Errors**:
   - Ensure database user has necessary permissions
   - Check if tables were created successfully

### Support

If you encounter issues:
1. Check the Streamlit logs in the terminal
2. Verify all environment variables are set
3. Test database connectivity separately

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NeonDB](https://neon.tech/) PostgreSQL
- Charts created with [Plotly](https://plotly.com/)
- Secure authentication with [bcrypt](https://pypi.org/project/bcrypt/)
 ### c:\Users\Mufasa\Desktop\Work\Stan\Pima\pima-app\venv\Scripts\python.exe -m streamlit run app.py --server.port 8502