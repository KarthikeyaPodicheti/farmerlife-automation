# 🚜 FARMERLIFE2.0 YouTube Automation

Automated farming content uploads to the FARMERLIFE2.0 YouTube channel using GitHub Actions.

## 🌾 Features

- **3 uploads per day** (10:30 AM, 2:00 PM, 9:30 PM IST)
- **Random video selection** from Google Drive
- **Farming-focused titles** and descriptions
- **No duplicate uploads** (tracks processed videos)
- **Automatic token refresh**

## 📁 Drive Integration

**Source Folder:** https://drive.google.com/drive/folders/1kocgFg0rzsMCtXsrWiOH_oditWshBpbV

Videos are automatically downloaded from this Drive folder and uploaded to YouTube.

## 📊 Upload Schedule

| Time (IST) | Cron (UTC) | Purpose |
|------------|------------|---------|
| 10:30 AM   | `0 5 * * *` | Morning upload |
| 2:00 PM    | `30 8 * * *` | Afternoon upload |
| 9:30 PM    | `0 16 * * *` | Evening upload |

## 🎬 Content Strategy

**Channel:** FARMERLIFE2.0  
**Niche:** Farming, Agriculture, Rural Life  
**Category:** Howto & Style  

**Sample Titles:**
- "This Farming Technique Will SHOCK You! 🚜"
- "The Truth About Modern Farming Nobody Tells You"
- "Farm Life Reality Check - Raw Truth"

## 🔧 Technical Details

**Authentication:**
- OAuth 2.0 for YouTube uploads
- Service Account for Drive access
- Credentials stored as GitHub secrets

**Tracking Files:**
- `processed_videos.json` - Prevents duplicates
- `upload_history.json` - Complete upload log
- `daily_upload_count.json` - Daily statistics

## 🚀 Status

✅ **LIVE** - Automation is active and running  
🔄 **Next Upload:** Check Actions tab for schedule  
📺 **Channel:** [FARMERLIFE2.0](https://youtube.com/@FARMERLIFE2.0)

---

**Last Updated:** 2026-02-28  
**Total Videos Processed:** Check `upload_history.json`  
**Automation Health:** Monitor via GitHub Actions