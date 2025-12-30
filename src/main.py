import asyncio
import os
import difflib
from apify import Actor
from textblob import TextBlob
from langdetect import detect
import httpx  # Standard async HTTP client

# --- CUSTOM LINGO ENGINE (No External SDK Needed) ---
class LingoEngine:
    """
    A robust wrapper for Lingo.dev API to handle translations
    without needing a specific Python SDK installed.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        # Use the official endpoint (or fallback to a mock for hackathon demo if API is strict)
        self.base_url = "https://api.lingo.dev/v1/translate" 

    async def translate(self, text, source, target):
        """Sends text to Lingo API for translation."""
        if not self.api_key:
            return f"[MOCK MODE] {text}"  # Fallback if no key
            
        if source == target:
            return text

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "source": source,
            "target": target,
            "content": text
        }
        
        try:
            async with httpx.AsyncClient() as client:
                # NOTE: Adjust endpoint if Lingo releases a new v2 API
                response = await client.post(self.base_url, json=payload, headers=headers, timeout=10.0)
                
                if response.status_code == 200:
                    return response.json().get("translation", text)
                else:
                    # Log error but return original text to keep actor running
                    print(f"⚠️ Lingo API Error {response.status_code}: {response.text}")
                    return text
        except Exception as e:
            print(f"⚠️ Lingo Connection Error: {e}")
            return text

# --- MAIN ACTOR LOGIC ---
async def main():
    async with Actor:
        # 1. GET INPUT
        actor_input = await Actor.get_input() or {}
        input_string = actor_input.get('comments', "")
        user_key = actor_input.get('lingoApiKey')
        enable_test = actor_input.get('enableLingoTest', True)
        
        # 2. SMART KEY LOGIC (Monetization 💰)
        # Check environment for YOUR secret premium key
        premium_key = os.environ.get('MY_SECRET_LINGO_KEY')
        
        active_key = user_key if user_key else premium_key
        key_source = "User Key" if user_key else "Premium Managed Key"
        
        if not active_key:
            Actor.log.warning("⚠️ No API Key found (User or Premium). Running in MOCK Mode.")

        Actor.log.info(f"🚀 Starting AI Brand Sentinel using: {key_source}")
        
        # Initialize Engine
        lingo = LingoEngine(active_key)

        # Parse Input
        if not input_string:
            Actor.log.error("No comments provided!")
            return
        
        # Handle CSV format or newlines
        raw_texts = [t.strip() for t in input_string.replace('\n', ',').split(',') if t.strip()]
        
        results = []
        
        # 3. PROCESS LOOP
        for text in raw_texts:
            row = {"original_feedback": text}
            
            try:
                # A. Detect Language
                try:
                    lang = detect(text)
                except:
                    lang = "en"
                row["detected_lang"] = lang

                # B. Translate to English (for Analysis)
                translated_en = await lingo.translate(text, source=lang, target="en")
                row["translated_en"] = translated_en

                # C. Sentiment Analysis
                blob = TextBlob(translated_en)
                score = blob.sentiment.polarity
                if score > 0.1:
                    label = "Positive"
                    draft = "Thank you so much! We are thrilled you enjoyed our service."
                elif score < -0.1:
                    label = "Negative"
                    draft = "We are truly sorry. Please DM us so we can fix this immediately."
                else:
                    label = "Neutral"
                    draft = "Thank you for your feedback."
                
                row["sentiment_score"] = round(score, 2)
                row["sentiment_label"] = label
                row["ai_reply_english"] = draft

                # D. Draft Native Reply (The Diplomat)
                native_reply = await lingo.translate(draft, source="en", target=lang)
                row["ai_reply_native"] = native_reply

                # E. THE LINGO TEST (Round Trip Verification) 🛡️
                if enable_test and lang != "en":
                    # Translate BACK to English to check meaning
                    back_to_english = await lingo.translate(native_reply, source=lang, target="en")
                    
                    # Compare similarity (0.0 to 1.0)
                    matcher = difflib.SequenceMatcher(None, draft, back_to_english)
                    similarity = matcher.ratio()
                    
                    row["lingo_test_score"] = round(similarity, 2)
                    row["lingo_test_result"] = back_to_english
                    
                    # Safety Threshold
                    if similarity > 0.8:
                        row["lingo_test_status"] = "✅ SAFE"
                    elif similarity > 0.5:
                        row["lingo_test_status"] = "⚠️ REVIEW"
                    else:
                        row["lingo_test_status"] = "❌ UNSAFE"
                else:
                    row["lingo_test_status"] = "Skipped"

                results.append(row)

            except Exception as e:
                Actor.log.error(f"Error on '{text}': {e}")
                row["error"] = str(e)
                results.append(row)

        # 4. OUTPUT
        await Actor.push_data(results)
        Actor.log.info(f"✅ Processed {len(results)} items successfully.")

if __name__ == '__main__':
    asyncio.run(main())