import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx


# Database connection
DB_URI = {db_uri}
engine = create_engine(DB_URI)

# Load influencer data
def load_data():
    query = """
    SELECT i.username, i.category, i.followers, ia.engagement_rate, ia.fake_engagement_score, 
           ia.virality_score, ir.pagerank, ic.community_id, i.influencer_id
    FROM influencers i
    JOIN influencer_analysis ia ON i.influencer_id = ia.influencer_id
    JOIN influencer_rankings ir ON i.influencer_id = ir.influencer_id
    JOIN influencer_communities ic ON i.influencer_id = ic.influencer_id
    """
    return pd.read_sql(query, engine)

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Influencers")
selected_categories = st.sidebar.multiselect("Select Category (1-3)", df['category'].unique(), default=df['category'].unique()[:1])
followers_range = st.sidebar.slider("Followers Range", int(df['followers'].min()), int(df['followers'].max()), (int(df['followers'].min()), int(df['followers'].max())))
min_engagement = st.sidebar.slider("Minimum Engagement Score", float(df['engagement_rate'].min()), float(df['engagement_rate'].max()), float(df['engagement_rate'].min()))
max_fake_engagement = st.sidebar.slider("Maximum Fake Engagement Score", int(df['fake_engagement_score'].min()), int(df['fake_engagement_score'].max()), int(df['fake_engagement_score'].max()))
min_virality = st.sidebar.slider("Minimum Virality Score", float(df['virality_score'].min()), float(df['virality_score'].max()), float(df['virality_score'].min()))
selected_community = st.sidebar.selectbox("Community Filter", ['All'] + df['community_id'].unique().tolist())
pagerank_filter = st.sidebar.slider("Minimum PageRank Score", float(df['pagerank'].min()), float(df['pagerank'].max()), float(df['pagerank'].min()))

# Apply filters
filtered_df = df[
    (df['category'].isin(selected_categories)) &
    (df['followers'].between(followers_range[0], followers_range[1])) &
    (df['engagement_rate'] >= min_engagement) &
    (df['fake_engagement_score'] <= max_fake_engagement) &
    (df['virality_score'] >= min_virality) &
    (df['pagerank'] >= pagerank_filter)
]
if selected_community != 'All':
    filtered_df = filtered_df[filtered_df['community_id'] == selected_community]

# Select top 15 influencers
filtered_df = filtered_df.nlargest(15, 'pagerank')

st.subheader("Top 15 Influencers Based on Filters")
st.dataframe(filtered_df[['username', 'category', 'followers', 'engagement_rate', 'virality_score', 'pagerank']])

# PageRank Score Graph
st.subheader("PageRank Score Distribution")
fig, ax = plt.subplots()
sns.barplot(x=filtered_df['username'], y=filtered_df['pagerank'], ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Community Graph
st.subheader("Influencer Community Network")
G = nx.Graph()
for _, row in filtered_df.iterrows():
    G.add_node(row['username'], community=row['community_id'])
    for _, connection in filtered_df.iterrows():
        if row['community_id'] == connection['community_id'] and row['username'] != connection['username']:
            G.add_edge(row['username'], connection['username'])

fig, ax = plt.subplots(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, edge_color='gray', ax=ax)
st.pyplot(fig)

# Influencer selection
st.subheader("Influencer Details")
selected_influencer = st.selectbox("Select an Influencer", filtered_df['username'].tolist())

if selected_influencer:
    influencer_data = filtered_df[filtered_df['username'] == selected_influencer].iloc[0]
    
    # Display influencer name with Instagram icon & link
    instagram_url = f"https://www.instagram.com/{selected_influencer}/"
    st.markdown(
        f"""
        <h3 style="display: flex; align-items: center;">
            {selected_influencer} 
            <a href="{instagram_url}" target="_blank" style="margin-left: 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="24">
            </a>
        </h3>
        """, 
        unsafe_allow_html=True
    )

    # Influencer details
    st.write(f"**Followers:** {influencer_data['followers']}")
    st.write(f"**Engagement Rate:** {influencer_data['engagement_rate']:.2f}%")
    st.write(f"**Virality Score:** {influencer_data['virality_score']:.2f}")
    st.write(f"**PageRank Score:** {influencer_data['pagerank']:.2f}")
    
    # Fetch brand collaborations
    brand_query = "SELECT DISTINCT brandtags FROM post_details WHERE influencer_id = %(influencer_id)s"
    brand_df = pd.read_sql(brand_query, engine, params={"influencer_id": int(influencer_data['influencer_id'])})



    if not brand_df.empty:
        # Extract unique brand names while handling lists or comma-separated values
        brand_set = set()
        for brand_tags in brand_df['brandtags'].dropna():
            if isinstance(brand_tags, str):
                brand_set.update(brand_tags.split(", "))  # Split if multiple brands exist in a row

        if brand_set:
            st.markdown("### 🔥 Previous Brand Collaborations")
            
            cols = st.columns(3)  # Arrange in 3 columns for better readability
            for i, brand in enumerate(sorted(brand_set)):  # Sort for consistency
                with cols[i % 3]:  
                    st.markdown(f"✅ **{brand}**")
        else:
            st.info("No brand collaborations found.")
    else:
        st.info("This influencer has no recorded brand collaborations.")

