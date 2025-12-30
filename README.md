# 🛡️ AI Brand Sentinel (Lingo-Powered)

[![Apify](https://img.shields.io/badge/Built%20on-Apify-orange?style=for-the-badge&logo=apify)](https://apify.com)
[![Lingo](https://img.shields.io/badge/Powered%20By-Lingo.dev-blue?style=for-the-badge)](https://lingo.dev)
[![Python](https://img.shields.io/badge/Code-Python-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Monetization](https://img.shields.io/badge/Pricing-Pay%20Per%20Use-green?style=for-the-badge)](https://apify.com/store)


> **The Problem:** 75% of global customers prefer support in their native language, but hiring multilingual staff is expensive.
> **The Solution:** AI Brand Sentinel is your automated **"AI Diplomat."** It reads reviews in 50+ languages, analyzes them in English, and drafts culturally accurate replies in the customer's *native* language.

---

## 🚀 Key Features

### 1. 🌍 Universal Ingestion
We use **Lingo.dev** to normalize feedback from **50+ languages** (Japanese, Spanish, German, etc.) into standardized English. This allows for consistent analysis regardless of the source language.

### 2. 🧠 Sentiment Intelligence
The Actor automatically grades every piece of feedback:
* `Positive` 🟢
* `Negative` 🔴
* `Neutral` ⚪

### 3. 🛡️ The "Lingo Test" (Safety Check)
**New Feature!** To prevent embarrassing mistranslations, the Actor performs a **Round-Trip Verification**:
1.  Drafts the reply in the native language (e.g., Spanish).
2.  Translates it *back* to English.
3.  Compares the meaning. If they don't match, it flags the reply as `⚠️ Needs Review`.

### 4. 🤝 The "Diplomat" Reply
Instead of replying in English, the AI generates a response in the **customer's native language**.
* *User:* "この製品は素晴らしい" (Japanese)
* *AI Reply:* "ありがとうございます！" (Japanese)

---

## 🛠️ How It Works

1.  **Input:** You provide a batch of reviews (Text or CSV).
2.  **Normalize:** The Actor identifies the language and translates it to English.
3.  **Analyze:** Sentiment is scored (-1.0 to +1.0).
4.  **Draft:** A response is generated based on the sentiment.
5.  **Verify:** The "Lingo Test" confirms the translation quality.
6.  **Output:** A structured JSON/Excel report is generated.

---

## ⚙️ Input Configuration

| Field | Type | Required? | Description |
| :--- | :--- | :--- | :--- |
| `comments` | String (TextArea) | **Yes** | Paste raw feedback here (comma-separated). <br> *Example:* `Good service, Muy mal servicio` |
| `lingoApiKey` | String | **No** | Your API Key from [Lingo.dev](https://lingo.dev). <br> **Leave empty** to use our Premium Managed Key (Pay-Per-Use rates apply). |
| `generateReply` | Boolean | No | If `true`, the AI auto-drafts responses. (Default: `True`) |
| `enableLingoTest` | Boolean | No | If `true`, runs the safety verification check. (Default: `True`) |

---

## 📊 Output Example

The Actor produces a detailed dataset with safety metrics:

```json
{
  "original_feedback": "Este producto es terrible.",
  "detected_language": "es",
  "translated_en": "This product is terrible.",
  "sentiment_label": "Negative",
  "ai_reply_native": "Lo sentimos mucho. Por favor contáctenos.",
  "lingo_test_status": "✅ SAFE",
  "lingo_test_score": 0.98
}
```

## 💡 Use Cases

**Global Support Triage**: Instantly understand tickets from Japan, Brazil, or France without hiring translators.

**Crisis Management**: Detect negative sentiment spikes in real-time across all markets.

**E-Commerce Automation**: Auto-draft "Thank You" notes for positive reviews in the buyer's native language.

## 💰 Pricing & Monetization

We offer a flexible Hybrid Model to suit everyone:

**Free Trial**: If you have your own Lingo.dev API Key, you pay only for Apify compute usage.

**Pay-Per-Use (Premium)**: Don't have a key? No problem. Use our Managed Key for just $0.10 per 1,000 items. We handle the API costs for you.

## ⚠️ Limitations
Sentiment Context: Sarcasm ("Oh great, another delay") can sometimes be misclassified as Positive depending on the translation nuance.

**Text Length**: extremely short comments (e.g., "Ok") may not trigger accurate language detection.

**Rate Limits**: If using your own Free Tier Lingo key, you may hit rate limits on large batches (500+ items).

## 🔮 Future Enhancements (Roadmap)
**Direct Integrations**: Connect directly to Slack, Discord, and Zendesk to pull tickets automatically.

**Custom Tone**: Allow users to select "Formal", "Playful", or "Apologetic" tones for the replies.

**Fine-Tuned Models**: Implement industry-specific sentiment models (e.g., specific to E-commerce vs. SaaS).


## 🧪 Try It Out (Sample Data)
To test the Actor immediately, copy and paste this multilingual text block into the `comments` input field:

> **I absolutely love this product it changed my life, Este servicio es terrible y nunca volveré a comprar aquí, Das ist ganz okay aber die Lieferung war langsam, J'adore la qualité de cet article c'est magnifique, この製品は壊れていました返金してください**

This block contains:
* 🇬🇧 **English:** Positive review
* 🇪🇸 **Spanish:** Negative review
* 🇩🇪 **German:** Neutral review
* 🇫🇷 **French:** Positive review
* 🇯🇵 **Japanese:** Negative review

## 👨‍💻 Support
Created for the **Lingo x Apify Hackathon**.