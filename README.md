# 🚜 FARMERLIFE2.0 YouTube Automation

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232088FF.svg?logo=githubactions&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube%20Data%20API%20v3-red?logo=youtube&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive%20API-4285F4?logo=googledrive&logoColor=white)

A high-performance, fully automated system for managing YouTube content distribution. This project synchronizes cloud storage assets with YouTube, utilizing advanced content strategies to maximize engagement and channel growth.

## 📺 Target Channel
**FARMERLIFE2.0**: [View Channel](https://www.youtube.com/@FARMERLIFE2.0-n7v)

---

## � Features & Architecture

- **Autonomous Distribution:** Fully automated 3x daily upload schedule via GitHub Actions.
- **Cloud Synchronization:** Deep integration with Google Drive for seamless asset management.
- **Smart Tracking:** Comprehensive JSON-based state management to prevent duplicate uploads and track performance.
- **Dynamic Optimization:** Real-time generation of SEO-optimized metadata, including curiosity-gap titles and high-retention descriptions.
- **Secure Auth:** Enterprise-grade security using OAuth 2.0 and encrypted GitHub Secrets for credential management.

## 📁 System Integration

### Google Drive
- **Source Folder:** [Drive Assets](https://drive.google.com/drive/folders/1kocgFg0rzsMCtXsrWiOH_oditWshBpbV)
- **Handler:** Service Account integration for secure read access to high-quality video files.

### 📊 Upload Schedule (IST)

| Time (IST) | Cron Strategy | Goal |
|:---|:---|:---|
| **10:30 AM** | `0 5 * * *` | Peak Morning Browsing |
| **02:00 PM** | `30 8 * * *` | Afternoon Engagement |
| **09:30 PM** | `0 16 * * *` | Prime Time Viewership |

---

## 🎬 Content Strategy (v2.0)

Our distribution strategy leverages modern psychological triggers and the "Curiosity Gap" to maximize CTR (Click-Through Rate) and retention for YouTube Shorts.

### 1. Evergreen Storytelling
Titles are engineered to be universally applicable to farming, animals, and rural life content, ensuring a perfect match even with randomized selection.

### 2. Psychological Triggers
- **Emotional Hooks:** Frequent use of high-impact emojis (😭, 🤯) to signal emotional stakes.
- **Knowledge Gaps:** Using phrases that demand a click to resolve, such as *"Wait for the end"* or *"Then what happened"*.

### 3. SEO Optimization
- **Tags:** Targeted mix of niche-specific (`#farming`, `#agriculture`) and broad-reach (`#shorts`, `#viral`, `#satisfying`) tags.
- **Description:** Optimized for the "Shorts Shelf" with call-to-actions (CTA) and subscription triggers.

---

## 🔧 File Structure

| File | Description |
|:---|:---|
| `upload_scheduled.py` | Core engine for API orchestration and upload logic. |
| `processed_videos.json` | Persistent state log of processed Google Drive file IDs. |
| `upload_history.json` | Detailed historical logs of every successful upload event. |
| `daily_upload_count.json` | Daily performance tracking and quota management. |
| `token.pickle` | Authenticated YouTube session (automatically refreshed). |

---

## 🚀 Automation Health

The system is currently **ACTIVE**. You can monitor real-time execution logs, credential refreshment, and upload status via the **GitHub Actions** tab.

**Last Strategy Update:** March 2026.