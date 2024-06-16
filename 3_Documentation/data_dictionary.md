### Data Dictionary

This data dictionary provides detailed information on the structure, contents, and meaning of each field in the various tables used in the TelcoCorp data platform. The tables are categorized into fact tables and dimension tables based on the star schema design.

---

## Fact Table

### `transaction_facts`
| Column Name              | Data Type  | Description                                      |
|--------------------------|------------|--------------------------------------------------|
| user_id                  | VARCHAR(50)| Unique identifier for the user                   |
| total_page_views         | INT        | Total number of page views by the user           |
| total_transaction_amount | FLOAT      | Total amount spent by the user in transactions   |

---

## Dimension Tables

### `user_dim`
| Column Name  | Data Type  | Description                                      |
|--------------|------------|--------------------------------------------------|
| user_id      | VARCHAR(50)| Unique identifier for the user                   |
| user_name    | VARCHAR(100)| Name of the user                                |
| user_email   | VARCHAR(100)| Email address of the user                       |

### `product_dim`
| Column Name  | Data Type  | Description                                      |
|--------------|------------|--------------------------------------------------|
| product_id   | VARCHAR(50)| Unique identifier for the product                |
| product_name | VARCHAR(100)| Name of the product                             |
| product_price| FLOAT      | Price of the product                             |

### `date_dim`
| Column Name  | Data Type  | Description                                      |
|--------------|------------|--------------------------------------------------|
| date_id      | DATE       | Date (YYYY-MM-DD)                                |
| day          | INT        | Day of the month (1-31)                          |
| month        | INT        | Month of the year (1-12)                         |
| year         | INT        | Year                                             |

### `campaign_dim`
| Column Name  | Data Type  | Description                                      |
|--------------|------------|--------------------------------------------------|
| campaign_id  | VARCHAR(50)| Unique identifier for the campaign               |
| campaign_name| VARCHAR(100)| Name of the campaign                            |
| campaign_type| VARCHAR(50)| Type of the campaign (e.g., email, social media) |

---

## Source Data Details

### Network Traffic Logs
- **File Format:** JSON
- **Key Fields:**
  - `user_id`: Unique identifier for the user
  - `session_id`: Unique identifier for the session
  - `timestamp`: Timestamp of the log entry
  - `page_viewed`: Page viewed by the user
  - `response_time`: Response time for the page load
  - `source_ip`: Source IP address of the user

### Transactional Data
- **File Format:** Parquet
- **Key Fields:**
  - `transaction_id`: Unique identifier for the transaction
  - `user_id`: Unique identifier for the user
  - `product_id`: Unique identifier for the product
  - `transaction_amount`: Amount spent in the transaction
  - `timestamp`: Timestamp of the transaction

---

## Detailed Field Descriptions

### `transaction_facts`

#### user_id
- **Description:** Unique identifier for the user.
- **Example Values:** `U12345`

#### total_page_views
- **Description:** Total number of page views by the user within a specified period.
- **Example Values:** `120`

#### total_transaction_amount
- **Description:** Total amount spent by the user in all transactions within a specified period.
- **Example Values:** `450.75`

### `user_dim`

#### user_id
- **Description:** Unique identifier for the user.
- **Example Values:** `U12345`

#### user_name
- **Description:** Full name of the user.
- **Example Values:** `John Doe`

#### user_email
- **Description:** Email address of the user.
- **Example Values:** `john.doe@example.com`

### `product_dim`

#### product_id
- **Description:** Unique identifier for the product.
- **Example Values:** `P98765`

#### product_name
- **Description:** Name of the product.
- **Example Values:** `SuperFast Internet Package`

#### product_price
- **Description:** Price of the product.
- **Example Values:** `99.99`

### `date_dim`

#### date_id
- **Description:** Date in YYYY-MM-DD format.
- **Example Values:** `2024-06-13`

#### day
- **Description:** Day of the month (1-31).
- **Example Values:** `13`

#### month
- **Description:** Month of the year (1-12).
- **Example Values:** `6`

#### year
- **Description:** Year.
- **Example Values:** `2024`

### `campaign_dim`

#### campaign_id
- **Description:** Unique identifier for the campaign.
- **Example Values:** `C2021`

#### campaign_name
- **Description:** Name of the campaign.
- **Example Values:** `Summer Promo`

#### campaign_type
- **Description:** Type of the campaign (e.g., email, social media).
- **Example Values:** `email`

---

## Notes
- **Primary Keys:** Each dimension table has a primary key that uniquely identifies each record (e.g., `user_id` in `user_dim`).
- **Foreign Keys:** Fact tables have foreign keys that reference primary keys in dimension tables (e.g., `user_id` in `transaction_facts` references `user_id` in `user_dim`).
- **Data Types:** Data types are chosen to ensure efficient storage and query performance. VARCHAR is used for text fields, INT for integers, FLOAT for decimal numbers, and DATE for date fields.
- **Normalization:** Dimension tables are designed to be normalized to eliminate redundancy and ensure data integrity.

By adhering to these specifications, the data dictionary ensures a clear understanding of the data structure, facilitating accurate data integration, transformation, and analysis.