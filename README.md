# 🛡️ AI Brand Sentinel (Lingo-Powered)


**AI Brand Sentinel** is an intelligent "AI Diplomat" designed for the **Lingo x Apify Hackathon**. It solves a critical real-world problem for global businesses: **Handling customer support in languages you don't speak.**

Unlike simple scrapers, this is a full **Bi-Directional AI Agent**. It reads feedback in *any* language, analyzes it in English, and then drafts a culturally correct response back in the customer's *native* language.

## 🚀 Key Features

* **🌍 True Multilingual Ingestion:** Uses **Lingo.dev** to detect and translate raw feedback from 50+ languages into English for standardized analysis.
* **🧠 Sentiment Intelligence:** Instantly grades customer sentiment as `Positive`, `Negative`, or `Neutral`.
* **🤝 The "AI Diplomat" (Killer Feature):**
    * **Customer Comfort First:** Instead of forcing users to read English, the Actor replies in **their native language**.
    * **How it works:** If a user complains in **Japanese**, the AI drafts the reply in **Japanese**. This makes the user feel understood and valued instantly.
* **📊 Business-Ready Data:** Outputs clean JSON/Excel data for immediate use in dashboards.

## 📋 How It Works

1.  **Input:** You paste a batch of raw customer reviews (comma-separated).
2.  **Process:** The Actor connects to the **Lingo API** to normalize text to English.
3.  **Analyze:** It scores the sentiment.
4.  **Respond:** It generates a reply and translates it back to the customer's origin language.

## ⚙️ Input Configuration

| Field | Type | Description |
| :--- | :--- | :--- |
| `comments` | String (Text Area) | **Required.** Paste all customer feedbacks here. Separate them with a comma (e.g., `Good service, Muy mal servicio, Das ist gut`). |
| `lingoApiKey` | String | **Required.** Your API Key from [Lingo.dev](https://lingo.dev). Required for the "Diplomat" features. |
| `generateReply` | Boolean | If enabled, the AI will auto-draft responses in the native language (Default: `True`). |

## 📦 Output Example

The Actor produces a detailed dataset including the **original text**, **detected language**, **sentiment score**, and the **translated reply**.

```json
{
  "original_feedback": "Este producto es terrible, estoy muy enojado.",
  "detected_language": "es",
  "translated_en": "This product is terrible, I am very angry.",
  "sentiment_label": "Negative",
  "ai_reply_english": "We are truly sorry to hear this. Please DM us.",
  "ai_reply_native": "Lamentamos mucho escuchar esto. Por favor envíanos un DM."
}
```

## 💡 Use Cases

**Global Support Triage**: Instantly understand tickets from Japan, Brazil, or France without hiring translators.

**Crisis Management**: Detect negative sentiment spikes in real-time across all markets.

**E-Commerce Automation**: Auto-draft "Thank You" notes for positive reviews in the buyer's native language.

## 🧪 Try It Out (Sample Data)
To test the Actor immediately, copy and paste this multilingual text block into the `comments` input field:

> **I absolutely love this product it changed my life, Este servicio es terrible y nunca volveré a comprar aquí, Das ist ganz okay aber die Lieferung war langsam, J'adore la qualité de cet article c'est magnifique, この製品は壊れていました返金してください**

This block contains:
* 🇬🇧 **English:** Positive review
* 🇪🇸 **Spanish:** Negative review
* 🇩🇪 **German:** Neutral review
* 🇫🇷 **French:** Positive review
* 🇯🇵 **Japanese:** Negative review


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