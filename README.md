# 📌 Instagram Influencer Impact Analysis Tool-hi

## 🚀 Project Overview
This project processes the **Instagram Influencer Dataset** and uploads it to **PostgreSQL (structured data)** and **Neo4j (graph-based influencer relationships)**. The goal is to analyze **influencer impact, engagement, audience demographics, and network influence** to help brands find **high-impact influencers**.

---

## 📂 **Dataset Files & Description**
| **File Name** | **Description** |
|--------------|---------------|
| `influencers.txt` | List of influencers with **username, category, followers, followees, total posts**. |
| `post_info.txt` | Contains **post IDs, influencer usernames, sponsorship labels, JSON metadata filenames, and image filenames**. |
| `json_files.zip` | **Post metadata JSON files**, containing **likes, comments, timestamps, sponsorship info, captions, hashtags, user tags**. |
| `profiles_influencers.zip` | Influencer profile details (**++bio, email, phone, profile pic, language, niche**). |
| `profiles_brands.zip` | Brand profile details (**bio, website, category, followers**). |
| `JSON-Image_files_mapping.txt` | Mapping of **JSON files to corresponding images** (Not used in this project). |

**📌 Note:** This project **does not process images**.

---

## 🛠️ **Tech Stack**
- **Database (Structured Data)** → PostgreSQL  
- **Database (Graph Data - Social Network Analysis)** → Neo4j  
- **Data Processing & Upload** → Python (Pandas, SQLAlchemy, Py2Neo)  
- **APIs & Analytics** (Planned) → FastAPI, Flask  

---

## 📌 **Installation & Setup**
### **1️⃣ Install Dependencies**
Run the following command to install the required libraries:
```bash
pip install pandas sqlalchemy psycopg2 py2neo
