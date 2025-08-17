# 📊 FastAPI CSV/Excel Data Manager

A clean, flexible backend built with **FastAPI + SQLAlchemy + Pandas** that provides complete functionality for uploading, reviewing, and editing CSV/Excel data.

## 🚀 Features

- ✅ **Upload CSV/Excel files** - Supports both `.csv` and `.xlsx/.xls` formats
- ✅ **Review datasets** - List all uploaded datasets with metadata
- ✅ **View data** - Get detailed view of any dataset with all records
- ✅ **Edit records** - Update dataset records via REST API
- ✅ **Web interface** - Simple HTML frontend for easy interaction
- ✅ **Database storage** - Flexible JSON storage in SQLite/PostgreSQL
- ✅ **CORS enabled** - Ready for frontend integration

## 📦 Project Structure

```
backend/
 ┣ app.py                 # Main FastAPI application
 ┣ database.py            # Database configuration
 ┣ models.py              # SQLAlchemy models
 ┣ schemas.py             # Pydantic schemas
 ┣ requirements.txt       # Python dependencies
 ┣ frontend.html          # Web interface
 ┣ test_data.csv          # Sample data for testing
 ┗ uploads/               # Uploaded files storage
```

## 🔧 Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Configuration

The project is configured to use SQLite for local development:

```python
# For local development
DATABASE_URL = "sqlite:///./test.db"

# For Railway deployment (commented out)
# DATABASE_URL = "postgresql://postgres:hCukXsTnUaLQmoVVsICaDhRSBWyXfVIZ@postgres-glu6.railway.internal:5432/railway"
```

### 3. Run the Server

```bash
uvicorn app:app --reload
```

The server will start at `http://127.0.0.1:8000`

## 📋 API Endpoints

### 1. Upload File
```bash
POST /upload
```
Upload a CSV or Excel file and store it in the database.

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/upload" -F "file=@data.csv"
```

### 2. List All Datasets
```bash
GET /datasets
```
Get a list of all uploaded datasets with their data.

**Example:**
```bash
curl http://127.0.0.1:8000/datasets
```

### 3. Get Single Dataset
```bash
GET /datasets/{dataset_id}
```
Get detailed information about a specific dataset.

**Example:**
```bash
curl http://127.0.0.1:8000/datasets/1
```

### 4. Update Dataset
```bash
PUT /datasets/{dataset_id}
```
Update the records in a dataset.

**Example:**
```bash
curl -X PUT "http://127.0.0.1:8000/datasets/1" \
     -H "Content-Type: application/json" \
     -d '[{"Name":"John","Age":30},{"Name":"Anna","Age":25}]'
```

## 🌐 Web Interface

Open `frontend.html` in your browser to access the web interface:

```
file:///path/to/your/project/frontend.html
```

The interface provides:
- **File upload** with drag-and-drop support
- **Dataset listing** with record counts
- **Data viewing** in table format
- **Inline editing** by clicking on cells
- **Real-time updates** via API calls

## 🧪 Testing

### Test with Sample Data

1. **Upload the test CSV:**
```bash
curl -X POST "http://127.0.0.1:8000/upload" -F "file=@test_data.csv"
```

2. **View uploaded datasets:**
```bash
curl http://127.0.0.1:8000/datasets
```

3. **Edit data:**
```bash
curl -X PUT "http://127.0.0.1:8000/datasets/1" \
     -H "Content-Type: application/json" \
     -d '[{"Name":"Updated Name","Age":35,"City":"Updated City","Salary":90000}]'
```

### Test with Your Excel Files

The system has been tested with your `all_order (2).xlsx` file. Note that if Excel files contain only headers without data rows, they will show 0 records.

## 🔄 Database Schema

### Dataset Model
```python
class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)           # Original filename
    data = Column(JSON)                         # Flexible JSON storage
```

## 🚀 Deployment

### For Railway Deployment

1. Uncomment the PostgreSQL URL in `database.py`
2. Comment out the SQLite configuration
3. Deploy to Railway

### For Local Production

1. Install PostgreSQL locally
2. Update the `DATABASE_URL` in `database.py`
3. Run with production ASGI server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 📊 Supported File Formats

- **CSV files** (`.csv`) - Parsed with pandas `read_csv()`
- **Excel files** (`.xlsx`, `.xls`) - Parsed with pandas `read_excel()`

## 🔧 Dependencies

```txt
fastapi          # Web framework
uvicorn          # ASGI server
sqlalchemy       # ORM
pandas           # Data processing
openpyxl         # Excel support
psycopg2-binary  # PostgreSQL driver
python-multipart # File upload support
```

## 🎯 Key Features Implemented

✅ **Flexible Data Storage** - JSON column allows any CSV/Excel structure  
✅ **File Upload Handling** - Temporary storage and pandas processing  
✅ **CORS Support** - Frontend integration ready  
✅ **Error Handling** - Proper HTTP status codes and error messages  
✅ **Auto-reload** - Development server with hot reload  
✅ **Database Auto-creation** - Tables created automatically on startup  

## 🔮 Future Enhancements

- [ ] Add pagination for large datasets
- [ ] Implement search and filtering
- [ ] Add data validation rules
- [ ] Export functionality (CSV/Excel download)
- [ ] User authentication and authorization
- [ ] Batch operations for multiple records
- [ ] Data visualization charts
- [ ] File format conversion

## 📝 Notes

- The system stores data as JSON for maximum flexibility
- Excel files with only headers will show 0 records
- Railway internal hostnames only work in deployed environment
- CORS is enabled for all origins (adjust for production)

---

🎉 **Your FastAPI CSV/Excel Data Manager is ready to use!**# E-INVOICE
