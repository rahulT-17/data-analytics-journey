# Spotify Music Trend Intelligence : Detecting Emerging Sounds & Artists

# Project Overview :
Since I have a niche interest in music I thought why not incorporate music and data analysis together,This project analyzes Spotify track-level audio features to understand how **musical characteristics change as popularity increases**. 

# GOAL : 
My goal is to identify sound patterns that are associated with mainstream success and explore how these insights can help detect **emerging music trends**.

---

# Business Question : 
**Do audio features systematically change as track popularity increases?**

Instead of focusing only on popularity scores, this project examines how the *sound* of music evolves as tracks gain more audience engagement.

---

# Dataset
- Source: Spotify Tracks Dataset (Kaggle)
- Size: ~232,000 tracks
- Key attributes:
  - Popularity (business metric)
  - Audio features such as:
    - energy
    - danceability
    - acousticness
    - speechiness
    - loudness
    - tempo
    - valence

---

## Approach

### 1. Data Cleaning & Validation
- Removed tracks with zero popularity to avoid inactive or noisy records
- Checked for missing values and duplicates
- Ensured transformations did not distort the overall data distribution

### 2. Popularity Segmentation
Tracks were grouped into three categories:
- **Low popularity** (popularity < 30)
- **Medium popularity** (30 ≤ popularity < 60)
- **High popularity** (popularity ≥ 60)

This segmentation simplifies comparison across engagement levels.

### 3. Comparative Audio Feature Analysis
Average audio feature values were compared across popularity groups using group-by analysis.

---

## Key Insights :

- During this comparison I had noticed that as popularity increases, tracks tend to have:
  - higher energy
  - higher danceability
  - higher loudness
  - slightly higher tempo and speechiness
- While these all features were increasing i noticed that the "acousticness" consistently decreases as popularity rises**

### Interpretation :
- Using this data I have noticed that the mainstream music increasingly favors **highly produced, electronic, and energetic sound profiles**, while more acoustic tracks are less likely to achieve high popularity.

---

## Why This Matters
Understanding how audio characteristics correlate with popularity can help:
- identify emerging sounds before they go mainstream
- support data-driven decisions in music marketing and A&R
- analyze cultural shifts in listener preferences

---

## Tools :
- Python
- Pandas
- Jupyter Notebook

---

## Future Work : I'm contiuniously working on this project 
- Genre-wise trend analysis
- Identifying “emerging” tracks with medium popularity but high-energy profiles
- Visualization of feature trends
- Time-based popularity analysis

---

Rahul Thakur  
Aspiring Data Analyst | Music & Data Enthusiast
