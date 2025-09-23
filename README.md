# CDE_2025_Docker_ETL
## ETL Pipeline with Docker, PostgreSQL, and Python

This project demonstrates a simple **Extract, Transform, Load (ETL)** pipeline using:

* **PostgreSQL** (running in a Docker container) as the data warehouse
* **Python (Pandas + SQLAlchemy)** to perform ETL
* **Docker** for containerization and reproducibility

The pipeline extracts a GDP dataset (CSV) from a public URL, transforms it (cleans and renames columns), and loads it into a PostgreSQL table.

---

### 📂 Project Structure

```
.
├── Dockerfile                # Python app container definition
├── requirements.txt          # Python dependencies
├── utils.py                  # ETL helper functions
├── run_etl_pipeline.py       # Main entrypoint for pipeline
├── export_var.sh             # Environment variable definitions
├── docker_pipeline_script.sh # Orchestrates the full pipeline setup
```

---

### ⚡ Prerequisites

Before running, ensure you have installed:

* [Docker](https://docs.docker.com/get-docker/)
* [Bash shell](https://www.gnu.org/software/bash/) (Linux/Mac or WSL on Windows)

---

### ⚙️ Setup and Run

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

#### 2. Make scripts executable

```bash
chmod +x docker_pipeline_script.sh
```

#### 3. Run the full pipeline with one command

```bash
./docker_pipeline_script.sh
```

This will:

1. Load environment variables from `export_var.sh`.
2. Pull the official PostgreSQL image.
3. Create a custom Docker network (`ntwork`) for container communication.
4. Start a PostgreSQL container named `my_postgres_server`.
5. Build the Python ETL app image (`cdedocker`).
6. Run the ETL app container (`cdedock`) connected to the same network.

---

### 🗄️ Database Details

* **Host**: `my_postgres_server`
* **Port**: `5432`
* **User**: `cdeassgn` (default from `export_var.sh`)
* **Password**: `password` (default from `export_var.sh`)
* **Database**: `cdedockdb`

The ETL pipeline loads data into the table:

* **Table name**: `worldgdps`
* **Schema**: `public`

---

### 🔍 Verifying the Data

After the pipeline completes, connect to PostgreSQL to confirm the data was loaded:

```bash
docker exec -it my_postgres_server psql -U postgres -d cdedockdb
```

Inside psql, run:

```sql
\d worldgdps;
SELECT * FROM worldgdps LIMIT 10;
```

---

### 🛠️ Customization

* To change the dataset URL, edit the `CSV_URL` variable in **`export_var.sh`**.
* To change PostgreSQL credentials or database name, edit **`export_var.sh`** as well.
* Add more transformations in `etl_pipeline.py` → `transform_data()`.

---

### 🧹 Cleanup

To stop and remove containers, network, and volumes:

```bash
docker rm -f cdedock my_postgres_server
docker network rm ntwork
docker volume rm postgres_data
```

---
