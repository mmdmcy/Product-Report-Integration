class Config:
    """Configuration settings for the product report integration system."""

    # Application settings
    REPORT_GENERATION_INTERVAL = "daily"  # Options: daily, weekly, monthly
    LOGGING_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Database connection settings
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 5432
    DATABASE_NAME = "product_reports"
    DATABASE_USER = "user"
    DATABASE_PASSWORD = "password"

    # API connection settings
    API_BASE_URL = "https://api.example.com"
    API_TIMEOUT = 30  # seconds

    # Email notification settings
    EMAIL_SMTP_SERVER = "smtp.example.com"
    EMAIL_PORT = 587
    EMAIL_USERNAME = "notify@example.com"
    EMAIL_PASSWORD = "email_password"

    @staticmethod
    def get_database_uri():
        """Constructs the database URI from the configuration settings."""
        return f"postgresql://{Config.DATABASE_USER}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_HOST}:{Config.DATABASE_PORT}/{Config.DATABASE_NAME}"