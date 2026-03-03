# 🚜 FARMERLIFE2.0 YouTube Automation

![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-YouTube-red)
![Automation](https://img.shields.io/badge/Automation-GitHub_Actions-blue)

A complete, fully automated workflow system designed to consistently upload engaging, high-retention video content to the **[FARMERLIFE2.0](https://www.youtube.com/@FARMERLIFE2.0-n7v)** YouTube channel.

This repository leverages Python scripts combined with GitHub Actions to autonomously download video content from Google Drive, optimize the metadata for YouTube Shorts algorithms, and schedule publication completely hands-free.

---

## 🌟 Key Features

- **Automated Scheduling pipeline:** Deploys 3 optimized uploads daily via GitHub Actions.
- **Dynamic Content Selection:** Connects securely to a source Google Drive and randomly selects videos that have not yet been published.
- **Advanced Title Engine:** Utilizes psychologically triggering, evergreen titles optimized for high CTR and viewer curiosity.
- **Algorithm-Optimized Descriptions:** Automatically attaches high-retention descriptions and SEO-targeted tags for the YouTube Shorts feed.
- **Duplicate Prevention Logging:** Strictly logs every upload ID to a JSON ledger to ensure identical videos are never uploaded twice.
- **Continuous Authentication:** Features a self-refreshing OAuth flow ensuring uninterrupted scheduled actions without manual login prompts.

## 📊 Deployment Schedule

Uploads occur thrice daily on strict predefined intervals (Indian Standard Time):

| Upload Phase | Time (IST) | Cron Trigger (UTC) |
|--------------|------------|--------------------|
| 🌅 Morning   | 10:30 AM   | `0 5 * * *`       |
| 🏙️ Afternoon | 2:00 PM    | `30 8 * * *`      |
| 🌃 Evening   | 9:30 PM    | `0 16 * * *`      |

*To run manually, navigate to the **Actions** tab on GitHub and trigger via `workflow_dispatch`.*

## 🎬 Content Strategy & Target Metrics

**YouTube Channel:** [FARMERLIFE2.0](https://www.youtube.com/@FARMERLIFE2.0-n7v)  
**Content Niche:** Farming, Agriculture, Rural Life, Animals  

The automation now enforces a modernized **curiosity gap** strategy, replacing generic titles with narrative hooks designed to stall scrolling behavior. 

**Titling Psychology Examples:**
- *"You won't believe what happened in the village today 😭"*
- *"Watch what this animal did to save the farm 😭"*
- *"They found this while digging the farm dirt 🤯"*

## 🔧 Technical Overview & Architecture

### Core Files
- `upload_scheduled.py`: The main controller. Handles API interactions for both Google Drive indexing and YouTube API uploads. Injects generated metadata onto media.
- `.github/workflows/youtube-uploads.yml`: The CI/CD instructions. Maps GitHub repository secrets cleanly into the temporary worker nodes used to fire the python script.

### State & Tracking Ledger
- `processed_videos.json`: Stores successfully handled Google Drive item IDs.
- `upload_history.json`: Comprehensive structured logging containing file sizes, upload timestamps, and URLs.
- `daily_upload_count.json`: Ratelimiting and analytical counter for the day's total payloads.

### Authentication Strategy
Keys are entirely handled via GitHub Secrets to secure cloud configurations:
- **`GOOGLE_CLIENT_SECRET`** & **`GOOGLE_SERVICE_ACCOUNT`**
- **`YOUTUBE_TOKEN`**

## 🚀 Live Status

📺 **Channel Link:** Subscribe and view at **[FARMERLIFE2.0](https://www.youtube.com/@FARMERLIFE2.0-n7v)**  
🔄 **Workflow Health:** Monitor active runs under the Actions panel. Total historical uploads can be traced by reading the local `upload_history.json`.

---
*Maintained by the FARMERLIFE2.0 Bot.*