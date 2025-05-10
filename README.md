# 📊 Influencer Analysis App (Streamlit)

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

A Streamlit-based interactive dashboard to analyze and visualize influencer data with advanced filtering, ranking (PageRank), and community detection (Louvain algorithm). Connects to a database, supports influencer profiling, and includes dynamic visualizations.

---

## 🚀 Features

- ✅ Load influencer data from a SQL database
- 🎯 Sidebar filters: Categories, Followers, Engagement, and Community
- 🏆 Display top 15 influencers ranked by PageRank score
- 📈 Visualizations: PageRank score distribution and influencer network graph
- 🔎 Detailed influencer profile with brand collaboration history

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Data Analysis & ML:** scikit-learn, pandas, numpy, matplotlib, seaborn  
- **Graph Analysis:** networkx, python-louvain (community)  
- **Database:** SQLAlchemy (for DB connection)  

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/influencer-analysis-app.git
cd influencer-analysis-app
```
### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
###  4. Add Your Environment Variables

```bash
DATABASE_URL=your-database-url-here
```

### ▶️ Run the App
```bash
streamlit run app.py
```
Then open the browser at http://localhost:8501 if it doesn’t open automatically.

### 📁 Project Structure

```bash
influencer-analysis-app/
│
├── algorithms              # This is where I cooked
├── imagesofresults         # results
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # (Not tracked by Git) Contains DB credentials
├── .gitignore              # Ignoring sensitive & junk files
├── README.md               # You're here :)
```
