## Live Application Links
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=19jStdfDXWfG7Pvma_-KPqHT0EoVaYVVE0Rfmbh3zW8g#0)

[![Snowflake](https://img.shields.io/badge/Snowflake-366DBF?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)

[![AWS S3](https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/s3/)

## Problem Statement
The goal of this project is to design and implement a robust data engineering framework that consolidates, organizes, and provides easy access to a wide range of financial professional development resources, which will cater in the future to aid a curated learning experience.

## Project Goals
This project is designed to leverage advanced data engineering techniques for the aggregation and structuring of finance professional development materials. Our approach is methodical and spans four critical phases:

1. Web Scraping and Dataset Creation:
   - Employ web scraping technologies, such as Beautiful Soup or Scrapy, to systematically gather data from selected webpages, starting with the CFA Institute’s site. This involves dynamically navigating from the main page to individual articles, focusing on extracting key information including introductions, learning outcomes, and summaries.
   - The data collected will be structured into a coherent CSV dataset featuring columns for the topic name, publication year, level, introduction summary, learning outcomes, and direct links to both the summary page and associated PDF files.
   - A Python notebook will be developed to automate and document this process for repeatability and scalability.

2. PDF Extraction:
   - Utilize tools like PyPDF2 and Grobid for text extraction from PDF documents to capture detailed topic outlines.
   - Output will be systematically organized into text files, adhering to a specific naming convention, and sorted into designated folders for efficient access and reference.
   - Another Python notebook will be created to streamline this extraction workflow.

3. Database Integration:
   - With SQLAlchemy, the structured data from the initial scraping phase will be uploaded to a Snowflake database, ensuring that our collected data is securely stored and easily accessible for analysis and querying.
   - Detailed documentation of this upload process will be provided through a dedicated Python notebook.

4. Cloud Storage and Database Metadata Management:
   - A Python function will be crafted for the seamless upload of all gathered data (both CSV datasets and extracted text files) to an AWS S3 bucket, ensuring our data is backed up and stored in a scalable, cloud-based environment.
   - Additionally, metadata extracted in the PDF phase will be uploaded to the Snowflake database using SQLAlchemy, with the process thoroughly documented in a Python notebook for transparency and ease of understanding.

## Technologies Used
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful_Soup-4CA3DD?style=for-the-badge&logo=beautifulsoup&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[![Scrapy](https://img.shields.io/badge/Scrapy-1F4C9F?style=for-the-badge&logo=scrapy&logoColor=white)](https://docs.scrapy.org/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-336791?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://pythonhosted.org/PyPDF2/)
[![Grobid](https://img.shields.io/badge/Grobid-007396?style=for-the-badge&logo=git&logoColor=white)](https://github.com/kermitt2/grobid)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/)
[![Snowflake](https://img.shields.io/badge/Snowflake-366DBF?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![AWS S3](https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/s3/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-4A569D?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

## Data Sources
The data sources utilized in this assignment are as follows:

1. CFA Institute’s Website: The primary source for extracting finance professional development    materials, including introductions, learning outcomes, and summaries of various topics.

2. PDF Documents: These documents are Accessed through direct links on the CFA Institute's website and provide in-depth outlines and detailed content on specific finance-related topics.

These sources are pivotal for creating a rich dataset and extracting valuable insights for the finance professional community.

## Pre-requisites
Before running this project, ensure you have the following prerequisites set up:

- **Python**: Ensure Python is installed on your system.
- **Virtual Environment**: Set up a virtual environment to manage dependencies and isolate your project's environment from other Python projects. You can create a virtual environment using `virtualenv` or `venv`.
- **requirements.txt**: Install the required Python dependencies by running the command:
  ```
  pip install -r requirements.txt
  ```
- **Config File**: Set up the `configurations.properties` file with the necessary credentials and configurations.
- **Grobid**: Docker setup is required for running the Grobid server.
  
  Pull the image from docker HUB 
  ```
  docker pull lfoppiano/grobid:0.8.0
  ```
  Run the container:
  ```
  docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
  ```
  From there, you can check on your browser if the service works fine by   accessing the welcome page of the service console, available at the URL http://localhost:8070.
- **Graphviz**: Graphviz is needed for generating the architecture diagram.
 
  On Windows:
  ```
  choco install graphviz
  ```
  On macOS and Linux:
  ```
  brew install graphviz
  ```
- **AWS S3**: Set up an IAM user with appropriate permissions for accessing S3 buckets. Ensure you have the necessary access keys and secrets configured in your AWS CLI or SDK. 
- **Snowflake**: Create a Snowflake warehouse, database, and schema. Ensure you have the necessary credentials and configurations set up in the `configurations.properties` file for connecting to Snowflake.

## Program Structure
```
.
├── .gitignore
├── README.md
├── cloud-storage-integration
│   ├── aws_snowflake_config.py
│   ├── cloud-integration.ipynb
│   └── metadata-grobid.csv
├── database-upload
│   └── upload_to_db.ipynb
├── diagrams-and-script
│   ├── flow_diagram.ipynb
│   ├── flow_diagram.png
│   └── input-icons
│       ├── local_storage.png
│       ├── snowflake.png
│       └── website.png
├── pdf-extractions
│   ├── config.json
│   ├── grobid
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   └── Grobid_RR_2024_l3_combined.txt
│   ├── input-files
│   │   ├── 2024-l1-topics-combined-2.pdf
│   │   ├── 2024-l2-topics-combined-2.pdf
│   │   └── 2024-l3-topics-combined-2.pdf
│   ├── pdf_extractions_pypdf_grobid.ipynb
│   └── pypdf
│       ├── PyPDF_RR_2024_l1_combined.txt
│       ├── PyPDF_RR_2024_l2_combined.txt
│       └── PyPDF_RR_2024_l3_combined.txt
├── requirements.txt
├── screenshots
│   ├── s3
│   │   ├── cfa_data_s3.png
│   │   ├── grobid_s3.png
│   │   ├── pypdf_s3.png
│   │   └── s3_bucket_structure.png
│   └── snowflake
│       ├── snowflake_cfa_refresher_readings.png
│       └── snowflake_grobid_metadata.png
└── web-scraping-and-dataset
    ├── scraped_data.csv
    └── web_scrape.ipynb
```

## How to Run the Application Locally
Follow these steps to run the application locally from scratch:

Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

1. **Installation**: Install the required Python dependencies by running `pip install -r requirements.txt`.

2. **Configurations**: Make changes in the `configurations.properties` file to configure application settings and credentials.

3. **Web Scraping**: Run `web_scrape.ipynb` first to scrape data from the web and save it into a CSV file.

4. **Grobid Setup**: Run the docker container to start the Grobid server. You can check whether the service is up and running by opening the following URL:
http://localhost:8070/

5. **PDF Extractions**: Run `pdf_extractions_pypdf_grobid.ipynb` to extract text from PDF files using PyPDF2 and Grobid.

6. **Snowflake Setup**: Check Snowflake configurations and run `upload_to_db.ipynb` to upload the CSV file generated in step 3 to the Snowflake database.

7. **AWS S3 Setup**: Set up IAM user credentials and a private S3 bucket.

8. **Cloud Integration**: Run `cloud-integration.ipynb` to load CSV and text files into the S3 bucket and to load metadata from Grobid and S3 links to the Snowflake database.

## Learning Outcomes
By completing this assignment, you will:

- **Develop Web Scraping Skills**: Learn to extract structured data from web pages using tools like Beautiful Soup or Scrapy.
  
- **Understand Data Structuring**: Gain proficiency in organizing extracted data into CSV files, adhering to a predefined schema.
  
- **Automate Processes with Python**: Develop automation skills by creating Python notebooks to streamline data extraction processes.
  
- **Extract Text from PDFs**: Gain experience in extracting text from PDF files using PyPDF2 and Grobid libraries.
  
- **Integrate with Databases**: Learn to integrate structured data into a relational database using SQLAlchemy.
  
- **Utilize Cloud Storage**: Understand how to upload and manage files in cloud storage services like AWS S3, and integrate them with database systems.

## Team Information and Contribution
| Name                       | Contribution % |
|----------------------------|----------------|
| Muskan Deepak Raisinghani  | 41%            |
| Rachana Keshav             | 34%            |
| Ritesh Choudhary           | 25%            |
