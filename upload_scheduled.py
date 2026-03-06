#!/usr/bin/env python3
"""
🚜 FARMERLIFE2.0 YouTube Automation
Uploads random videos from Drive to FARMERLIFE2.0 YouTube channel
"""

import os
import json
import pickle
import random
import sys
from datetime import datetime
from typing import Any, Set, Dict
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# FARMERLIFE2.0 Configuration
DRIVE_FOLDER_ID = '1kocgFg0rzsMCtXsrWiOH_oditWshBpbV'  # Your Drive folder
PROCESSED_LOG = 'processed_videos.json'
TOKEN_FILE = 'token.pickle' 
SERVICE_ACCOUNT = 'service-account-key.json'

# Video Titles
TITLES = [
    "#asethetic",
    "#songlyrics",
    "#asethetic",
    "#bulbul",
    "#explore",
    "#asethetic",
    "#birdtrend",
    "#asethetic",
    "#exe",
    "#asethetic",
    "#asethetic",
    "#noads",
    "#asethetic",
    "#asethetic",
    "#aa23",    
    "#exe",
]

def get_youtube_creds():
    """Load YouTube API credentials from token.pickle"""
    with open(TOKEN_FILE, 'rb') as f:
        return pickle.load(f)

def get_drive_creds():
    """Load Drive API credentials from service account"""
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT,
        scopes=['https://www.googleapis.com/auth/drive.readonly']
    )

def get_unprocessed_videos(drive: Any):
    """Get list of videos not yet uploaded"""
    processed: Set[str] = set()
    if os.path.exists(PROCESSED_LOG):
        with open(PROCESSED_LOG, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                processed = set(str(item) for item in data)
    
    videos = []
    page_token = None
    
    while True:
        response = drive.files().list(
            q=f"'{DRIVE_FOLDER_ID}' in parents and trashed = false",
            fields='nextPageToken, files(id, name, mimeType, shortcutDetails)',
            pageToken=page_token,
            pageSize=100
        ).execute()
        
        for f in response.get('files', []):
            # Handle shortcuts to videos (common in shared Drive folders)
            if f['mimeType'] == 'application/vnd.google-apps.shortcut':
                if 'shortcutDetails' in f:
                    real_id = f['shortcutDetails']['targetId']
                    videos.append({'id': f['id'], 'real_id': real_id, 'name': f['name']})
            # Handle direct video files
            elif f['mimeType'].startswith('video/'):
                videos.append({'id': f['id'], 'real_id': f['id'], 'name': f['name']})
        
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    
    unprocessed = [v for v in videos if v['id'] not in processed]
    return unprocessed, processed

def download_video(drive, video_id, name):
    """Download video from Drive to temporary file"""
    # Clean filename for local storage
    clean_name = "".join(c for c in name if c.isalnum() or c in '._-').rstrip()
    if not clean_name.endswith('.mp4'):
        clean_name += '.mp4'
    
    local_path = f"/tmp/farmerlife_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{clean_name}"
    
    request = drive.files().get_media(fileId=video_id)
    
    with open(local_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    
    return local_path

def upload_video():
    """Main upload function"""
    print(f"\n{'='*70}")
    print(f"🚜 FARMERLIFE2.0 YOUTUBE UPLOAD")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{'='*70}\n")
    
    print("[1/5] 🔧 Initializing APIs...")
    youtube_creds = get_youtube_creds()
    youtube = build('youtube', 'v3', credentials=youtube_creds, cache_discovery=False)
    
    drive_creds = get_drive_creds()
    drive = build('drive', 'v3', credentials=drive_creds)
    print("  ✅ APIs ready")
    
    print("\n[2/5] 📁 Checking Drive for farming videos...")
    unprocessed, processed = get_unprocessed_videos(drive)
    
    if not unprocessed:
        print("  ❌ No unprocessed videos found in Drive folder!")
        print(f"  📂 Folder: https://drive.google.com/drive/folders/{DRIVE_FOLDER_ID}")
        return False
    
    print(f"  ✅ {len(unprocessed)} unprocessed videos available")
    print(f"  📊 {len(processed)} videos already uploaded")
    
    # Randomly select video
    video = random.choice(unprocessed)
    print(f"\n[3/5] 🎯 Selected: {video['name']}")
    
    print("\n[4/5] ⬇️ Downloading from Drive...")
    local_path = download_video(drive, video['real_id'], video['name'])
    size_mb = os.path.getsize(local_path) / (1024*1024)
    print(f"  ✅ Downloaded: {size_mb:.1f} MB")
    
    print("\n[5/5] ⬆️ Uploading to FARMERLIFE2.0...")
    
    # Generate title without sequential number
    title = random.choice(TITLES)
    
    # Psychologically engaging description for high retention
    description = f"""Krishna Bhajan
Krishna Song
Radhe Krishna Bhajan
Bhakti Song 2025
Shri Krishna
Krishna Devotional Song
Radhe Radhe
Krishna Bhakti Video
Bhakti Geet
Hare Krishna Mantra
Krishna Bhajan Shorts
Bhakti Ras
New Krishna Bhajan 2025
Krishna Kirtan
Govinda Bhajan
Lord Krishna Song
Spiritual Songs
Krishna Bhajan by @bhaktidhara1996
🌸 परिचय (Introduction) – @bhaktidhara1996
🙏 जय श्री कृष्णा 🙏
आपका स्वागत है हमारे भक्ति परिवार @bhaktidhara1996 में।
इस वीडियो में हम प्रस्तुत कर रहे हैं एक मधुर और दिव्य श्री कृष्ण भजन (Krishna Bhajan) जो आपके मन को शांति, आनंद और भक्ति से भर देगा।
हमारा उद्देश्य है कि हर घर में श्रीकृष्ण की भक्ति गूंजे और हर हृदय में राधे कृष्ण का प्रेम प्रवाहित हो।
🎶 कृष्ण भजन का महत्व (Importance of Krishna Bhajan)
श्रीकृष्ण केवल एक देवता ही नहीं बल्कि प्रेम, करुणा, मित्रता और धर्म के प्रतीक हैं।
कृष्ण भजन सुनने और गाने से:
मन शांत होता है 🕊️
हृदय में प्रेम बढ़ता है 💖
आत्मा पवित्र होती है 🌸
जीवन से नकारात्मकता दूर होती है 🙏
इसी कारण हमारे चैनल @bhaktidhara1996 पर हम निरंतर नए Krishna Bhajan, Radhe Krishna Songs, Bhakti Geet और Kirtan अपलोड करते रहते हैं।
📿 हरे कृष्ण महामंत्र (Hare Krishna Maha Mantra)
👉 "हरे कृष्ण हरे कृष्ण, कृष्ण कृष्ण हरे हरे।
हरे राम हरे राम, राम राम हरे हरे।।"
यह महामंत्र पूरे संसार का सबसे शक्तिशाली मंत्र है। जब भी आप इसे जपते हैं या सुनते हैं, तो मन अपने आप शांत हो जाता है और कृष्ण का प्रेम हृदय में उमड़ने लगता है।
इस मंत्र की महिमा को फैलाने का प्रयास @bhaktidhara1996 परिवार करता है।
🌺 कृष्ण कथा और लीला (Krishna Stories & Leelas)
बाल्यकाल में श्रीकृष्ण ने माखन चुराकर सबको आनंदित किया।
कालिया नाग का मर्दन कर भयमुक्ति दी।
बंसी की मधुर तान से गोपियों को मोहित किया।
कुरुक्षेत्र में अर्जुन को श्रीमद्भगवद गीता का उपदेश दिया।
हर बार जब हम कृष्ण भजन गाते हैं, तो यह केवल संगीत नहीं बल्कि इन दिव्य लीलाओं का स्मरण होता है।
@bhaktidhara1996 पर ऐसे ही भक्तिपूर्ण गीतों और कथाओं के माध्यम से हम आपके हृदय को कृष्णमय बनाने का प्रयास करते हैं।
🎼 हमारे भजन (Our Bhajan Collection @bhaktidhara1996)
👉 Krishna Bhajan
👉 Radhe Krishna Bhajan
👉 Govind Naam Sankirtan
👉 Madhur Bhakti Geet
👉 Hare Krishna Mantra Japa
हर भजन आपको प्रभु के और करीब ले जाने के लिए बनाया गया है।
🌸 भक्ति का मार्ग (Path of Devotion)
भक्ति ही सबसे सरल मार्ग है भगवान तक पहुँचने का।
कृष्ण भजन इसी भक्ति का मुख्य साधन है।
जब हम सच्चे हृदय से गाते हैं, तो कृष्ण स्वयं हमारे दुख हर लेते हैं।
@bhaktidhara1996 चैनल इसी भक्ति मार्ग पर आपका साथी है।
Krishna Bhajan, Krishna Song, Radhe Krishna Bhajan, Bhakti Song 2025, Shri Krishna, Krishna Devotional Song, Radhe Radhe, Krishna Bhakti Video, Bhakti Geet, Hare Krishna Mantra, Krishna Bhajan Shorts, Bhakti Ras, New Krishna Bhajan 2025, Krishna Kirtan, Govinda Bhajan, Lord Krishna Song, Spiritual Songs, Krishna Bhajan by @bhaktidhara1996
🌟 हमारा उद्देश्य (Our Mission) – @bhaktidhara1996
हमारा संकल्प है कि हर घर और हर दिल में कृष्ण भक्ति की धारा बहे।
इसीलिए हम रोज़ाना नए-नए भजन, कीर्तन और कृष्ण गीत अपलोड करते हैं।
👉 यदि आपको हमारे भजन पसंद आएं तो कृपया:
✔️ चैनल @bhaktidhara1996 को सब्सक्राइब करें
✔️ वीडियो को लाइक करें 👍
✔️ दोस्तों और परिवार के साथ शेयर करें 🙏
🙏 समापन (Conclusion)
कृष्ण भजन केवल गीत नहीं है – यह प्रेम, आस्था और आत्मा की आवाज़ है।
हर बार जब आप "राधे कृष्ण" का नाम लेते हैं, जीवन में नई रोशनी आती है।
🌸 आइए मिलकर गाएं:
"राधे कृष्णा... जय श्री कृष्णा... हरे कृष्णा..."
जय श्री राधे कृष्णा 🙏 @bhaktidhara1996
#bhaktidhara1996
#fxyoeditz
#flyxo
#kumarsir
#recitation
#hindudeity
#hindugod
#spiritualvibes
#sprituality
#hindispirituality
#marblemusic
#marriagecentre
⚠️ This video is made by AI and it has no relation with real life, this video is made only for educational and entertainment purpose.
RADHE RADHE 🙏💐
"""
    
    all_tags = [
        "Dp", "Poonam", "Shorts", "Short", "Ytshorts", "Gana", "Dp Poonam vlog",
        "Dp Poonam vlog video", "Poonam bind", "YouTube shorts", "Trending shorts",
        "Comedy shorts", "Funny video", "Viral video", "Bhojpuri song", "Bhojpuri gana",
        "Bhojpuri new song", "Bhojpuri new song 2024", "Bhojpuri movie", "Bhojpuri film",
        "Hindi gana", "Hindi song", "Hindi new song", "Hindi old song", "Hindi new song 2024",
        "Hindi movie", "Hindi film", "Hindi picture", "Vlog video", "Dhobi geet",
        "Hindi vlog", "Village mini vlog", "Pawan Singh", "ai generated story",
        "ai generated video", "ai story generator", "hindi story shorts",
        "create ai animated story video in hindi", "ai story video generator",
        "ai generated image", "hindi story", "ai story video generator free",
        "ai generated movie", "best hindi story", "hindi moral story",
        "ai generated funny video", "story in hindi", "deer story in hindi",
        "moral story in hindi", "hindi story for kids", "hindi story cartoon",
        "how to humanize ai generated text", "love story hindi", "story in hindi",
        "ai animation story video generator free", "hindi stories", "best hindi stories",
        "stories in hindi", "funny hindi stories", "hindi scary stories", "cartoon hindi stories",
        "hindi stories for kids", "hindi moral stories", "hindi comedy stories", "hindi horror stories",
        "kidlogics hindi stories", "hindi stories with moral", "moral stories in hindi",
        "hindi cartoon stories", "hindi animated stories", "comedy stories in hindi",
        "hindi short stories with moral", "moral stories hindi kahaniya", "stories",
        "story hindi", "latest hindi story", "kids hindi story", "moral hindi story"
    ]
    
    # Clean up tags, remove duplicates and stay perfectly within YouTube limits
    # Commas and periods in tags consistently trigger the 400 invalidTags error 
    clean_all_tags = set(t.replace(".", "").replace(",", "").replace("<", "").replace(">", "").strip() for t in all_tags)
    unique_tags = list(clean_all_tags)
    random.shuffle(unique_tags)
    
    selected_tags: list[str] = []
    current_length: int = 0
    
    for tag in unique_tags:
        if not tag:
            continue
            
        # 1 char for commas in the YouTube UI separator
        added_len = len(tag) + 1  
        
        # Max of 15 tags, and comfortably below the 500 API character limit
        if len(selected_tags) < 15 and current_length + added_len <= 400:
            selected_tags.append(tag)
            current_length += added_len

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': selected_tags,
            'categoryId': '26',  # Howto & Style
        },
        'status': {
            'privacyStatus': 'public',
            'madeForKids': False
        }
    }
    
    media = MediaFileUpload(local_path, mimetype='video/mp4', resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status is not None:
            progress = int(status.progress() * 100)
            print(f"  📤 Upload progress: {progress}%")
    
    video_id = response['id']
    
    # Update processed videos log
    processed.add(video['id'])
    with open(PROCESSED_LOG, 'w') as f:
        json.dump(list(processed), f)
    
    # Update upload history
    history = []
    if os.path.exists('upload_history.json'):
        with open('upload_history.json', 'r') as f:
            history = json.load(f)
    
    history.append({
        'timestamp': datetime.now().isoformat(),
        'title': title,
        'video_id': video_id,
        'drive_file': video['name'],
        'file_size_mb': float(round(float(size_mb), 1))
    })
    
    with open('upload_history.json', 'w') as f:
        json.dump(history, f, indent=2)
    
    # Update daily upload count
    today = datetime.now().strftime('%Y-%m-%d')
    daily_count: Dict[str, Any] = {'date': today, 'count': 0}
    
    if os.path.exists('daily_upload_count.json'):
        with open('daily_upload_count.json', 'r') as f:
            loaded_count = json.load(f)
            if isinstance(loaded_count, dict):
                daily_count = loaded_count
    
    if daily_count.get('date') != today:
        daily_count = {'date': today, 'count': 0}
    
    current_count = daily_count.get('count', 0)
    current_count_int = int(current_count) if isinstance(current_count, (str, int)) else 0
    daily_count['count'] = current_count_int + 1
    
    with open('daily_upload_count.json', 'w') as f:
        json.dump(daily_count, f, indent=2)
    
    # Clean up temporary file
    os.remove(local_path)
    
    print(f"\n{'='*70}")
    print(f"🎉 SUCCESS! Video uploaded to FARMERLIFE2.0")
    print(f"📺 Title: {title}")
    print(f"🔗 URL: https://youtu.be/{video_id}")
    print(f"📊 Today's uploads: {daily_count['count']}")
    print(f"🎬 Remaining videos: {len(unprocessed)-1}")
    print(f"💾 File size: {size_mb:.1f} MB")
    print(f"{'='*70}\n")
    
    return True

if __name__ == '__main__':
    try:
        success = upload_video()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n💥 ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)