# מדריך הגדרת ManyChat — שמירת פרטי קשר מדיה חברתית

## סקירה כללית

אוטומציה זו מלכדת לידים מאינסטגרם, פייסבוק וטיקטוק דרך ManyChat, שולחת webhook ל-n8n, וכותבת לטבלת **לקוחות** ב-SivanInvest CRM (Airtable Base: `applwPfaYwZiyJlM6`).

**שם התהליך (זהה ב-ManyChat וב-n8n):** `שמירת פרטי קשר מדיה חברתית`

---

## חלק 1: שדות מותאמים אישית (Custom Fields) ב-ManyChat

לפני יצירת הפלואו, הגדר את השדות הבאים תחת **Settings → Custom Fields**:

| שם השדה | סוג | תיאור |
|---------|-----|-------|
| `email` | Email | כתובת אימייל |
| `phone` | Phone | מספר טלפון |
| `platform` | Text | Instagram / Facebook / TikTok |
| `post_url` | Text | URL הפוסט/וידאו שגרם לאינטראקציה |
| `trigger_message` | Text | ההודעה/תגובה שהפעילה את הפלואו |
| `dm_keyword` | Text | המילה שהפעילה את הטריגר |
| `subscriber_id` | Text | מזהה המנוי ב-ManyChat (לשימוש עם {{ user id }}) |
| `content_id` | Text | מזהה פוסט/וידאו |

---

## חלק 2: בניית הפלואו ב-ManyChat

### צור פלואו חדש
1. עבור לתפריט **Flows → New Flow**
2. שם הפלואו: **`שמירת פרטי קשר מדיה חברתית`**

---

### קטע A: אינסטגרם ופייסבוק

#### טריגרים אפשריים
- **תגובת מילת מפתח**: Triggers → Comment → Keyword → הגדר מילות המפתח
- **הודעה ישירה**: Triggers → Instagram DM / Facebook DM → Keyword

#### מבנה הפלואו

```
[TRIGGER: Comment / DM]
         ↓
[Action: Set User Field]
  platform = "Instagram"   ← (או "Facebook" לפי הפלטפורמה)
         ↓
[Action: Set User Field]
  trigger_message = {{ last user input }}
         ↓
[Action: Set User Field]
  dm_keyword = "YOUR_KEYWORD"
         ↓
[Message Block]
  Text: "היי {{ first name }}! שמח שפנית 😊
         מה כתובת האימייל שלך?"
  ─ User Input (Type: Email) → saves to: email
  ─ Quick Reply: ✉️ השתמש באימייל {{ email }} (1-click Facebook/IG email)
         ↓
[Message Block]
  Text: "מעולה! ומה מספר הטלפון שלך?"
  ─ User Input (Type: Phone) → saves to: phone
         ↓
[Action: External Request (Webhook)]
  → ראה הגדרות ב-חלק 3
         ↓
[Message Block]
  Text: "תודה! פרטייך נשמרו בהצלחה 🙌
         ניצור איתך קשר בקרוב."
```

#### Quick Reply לאימייל (אינסטגרם/פייסבוק בלבד)
1. בתוך User Input לאימייל, לחץ **+ Add Quick Reply**
2. בחר **User Attribute** → **Email**
3. זה יציג את כתובת האימייל של המשתמש כלחצן בלחיצה אחת

---

### קטע B: טיקטוק

> ⚠️ **מגבלת טיקטוק**: אין תמיכה ב-Quick Reply עם אימייל אוטומטי. המשתמש חייב להקליד ידנית.

```
[TRIGGER: Comment Keyword / Private Message]
         ↓
[Action: Set User Field]
  platform = "TikTok"
         ↓
[Action: Set User Field]
  trigger_message = {{ last user input }}
         ↓
[Message Block]
  Text: "היי {{ first name }}! שמח שפנית 😊
         אנא הקלד/י את כתובת האימייל שלך כדי שאוכל לשלוח לך את הפרטים:"
  ─ User Input (Type: Text) → saves to: email
    (הגדר Validation: Email format)
         ↓
[Message Block]
  Text: "מעולה! ומה מספר הטלפון שלך?"
  ─ User Input (Type: Phone) → saves to: phone
         ↓
[Action: External Request (Webhook)]
  → ראה הגדרות ב-חלק 3
         ↓
[Message Block]
  Text: "תודה! פרטייך נשמרו 🙌"
```

---

## חלק 3: הגדרת External Request (Webhook) ב-ManyChat

### הוסף Action Block → External Request

**Method:** `POST`

**URL:** `https://YOUR_N8N_INSTANCE/webhook/manychat-leads-sync`

> 🔔 החלף את `YOUR_N8N_INSTANCE` בכתובת ה-n8n שלך לאחר הפעלת ה-Webhook node.

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "first_name": "{{ first name }}",
  "last_name": "{{ last name }}",
  "email": "{{ email }}",
  "phone": "{{ phone }}",
  "platform": "{{ platform }}",
  "post_url": "{{ post_url }}",
  "trigger_message": "{{ trigger_message }}",
  "subscriber_id": "{{ user id }}",
  "content_id": "{{ content_id }}",
  "dm_keyword": "{{ dm_keyword }}"
}
```

---

## חלק 4: הגדרת n8n

### שלב 1: ייבוא ה-Workflow
1. פתח את n8n
2. לחץ **Import from File**
3. בחר את הקובץ: `n8n-manychat-airtable-workflow.json`
4. ה-workflow יופיע בשם **שמירת פרטי קשר מדיה חברתית**

### שלב 2: הגדרת Credential (מפתח API של Airtable)
1. עבור לתפריט **Credentials → New Credential**
2. בחר **HTTP Header Auth**
3. מלא:
   - **Name:** `Airtable API`
   - **Name (Header):** `Authorization`
   - **Value:** `Bearer YOUR_AIRTABLE_API_KEY`
4. שמור
5. עדכן את ה-credential ID בכל הנודים (4 נודים עם `REPLACE_WITH_YOUR_CREDENTIAL_ID`)

> 💡 מפתח API של Airtable נמצא בכתובת: https://airtable.com/account → API

### שלב 3: הפעלת ה-Webhook
1. לחץ על נוד **ManyChat Webhook**
2. לחץ **Listen for test event** — קבל את ה-URL
3. העתק את ה-URL לשדה ה-Webhook ב-ManyChat
4. הפעל את ה-Workflow (לחץ **Active**)

---

## חלק 5: מבנה ה-Workflow ב-n8n

```
[ManyChat Webhook]
        ↓
[חיפוש לקוח קיים]
  GET Airtable — חיפוש לפי Email או טלפון
        ↓
[לקוח קיים?]
  IF records.length > 0
    ↙ TRUE              FALSE ↘
[בניית עדכון לקוח]    [בניית לקוח חדש]
        ↓                      ↓
[עדכון רשומת לקוח]   [יצירת רשומת לקוח חדשה]
  PATCH Airtable         POST Airtable
    ↓                          ↓
         [רישום אירוע ליד]
      POST → Lead Events table
                 ↓
         [תגובת הצלחה]
           HTTP 200 OK
```

### שדות שנכתבים לטבלת **לקוחות** (tblWPvL8NxFMzpyHJ)

**בעת יצירת רשומה חדשה:**
| שדה Airtable | ערך |
|-------------|-----|
| `שם פרטי` | first_name |
| `שם משפחה` | last_name |
| `שם מלא` | first_name + last_name |
| `טלפון` | phone |
| `Email` | email |
| `Source Platform` | platform (Facebook/Instagram/TikTok) |
| `Source Post URL` | post_url |
| `Source Content ID` | content_id |
| `Source Funnel` | "DM" |
| `ManyChat Subscriber ID` | subscriber_id |
| `DM Keyword Used` | dm_keyword |
| `WhatsApp Comments Log` | לוג האינטראקציה הראשונה |
| `Social Automation Lead` | ✅ true |
| `מקור הגעה` | ["צ׳ט בוט"] |
| `First Attribution Date` | timestamp נוכחי |
| `Last Attribution Date` | timestamp נוכחי |

**בעת עדכון רשומה קיימת:**
| שדה Airtable | פעולה |
|-------------|-------|
| `Source Platform` | עדכון |
| `Source Post URL` | עדכון |
| `DM Keyword Used` | עדכון |
| `Source Content ID` | עדכון |
| `ManyChat Subscriber ID` | עדכון |
| `Last Attribution Date` | עדכון לזמן נוכחי |
| `WhatsApp Comments Log` | **הוספה בראש** (ישמר היסטוריה מלאה) |

**פורמט לוג השיחה (WhatsApp Comments Log):**
```
[24/05/2026 12:30] פלטפורמה: Instagram | פוסט: https://... | הודעה: "הייתי רוצה לדעת עוד"
[20/05/2026 09:15] נוצר דרך Facebook | פוסט: https://... | הודעה: "שלחו לי פרטים"
```

### שדות שנכתבים לטבלת **Lead Events** (tblJCSzne2382Eguj)

| שדה | ערך |
|-----|-----|
| `Lead Event ID` | MC-{subscriber_id}-{timestamp} |
| `Client Phone Ref` | phone |
| `Event Type` | "Social Media DM" |
| `Event DateTime` | timestamp נוכחי |
| `Platform` | platform |
| `Source Post URL` | post_url |
| `ManyChat Subscriber ID` | subscriber_id |
| `Raw Payload` | JSON מלא של ה-webhook |
| `Notes` | trigger_message |

---

## חלק 6: טסטינג

### בדיקה ב-Postman / curl
```bash
curl -X POST https://YOUR_N8N_INSTANCE/webhook/manychat-leads-sync \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "ישראל",
    "last_name": "ישראלי",
    "email": "test@example.com",
    "phone": "+972501234567",
    "platform": "Instagram",
    "post_url": "https://instagram.com/p/TEST123",
    "trigger_message": "אשמח לקבל פרטים",
    "subscriber_id": "sub_test_001",
    "content_id": "POST123",
    "dm_keyword": "פרטים"
  }'
```

### צ'קליסט וידוא
- [ ] רשומה חדשה נוצרה בטבלת לקוחות
- [ ] כל השדות מולאו נכון
- [ ] רשומה חדשה נוצרה ב-Lead Events
- [ ] שליחת POST נוסף עם אותו email → רשומה **מתעדכנת** (לא נוצרת חדשה)
- [ ] WhatsApp Comments Log מציג היסטוריה עם שתי שורות
- [ ] ה-webhook מחזיר `{"status": "ok"}`

---

## טבלאות Airtable

| פרמטר | ערך |
|-------|-----|
| Base ID | `applwPfaYwZiyJlM6` |
| Leads Table | `tblWPvL8NxFMzpyHJ` (לקוחות) |
| Events Table | `tblJCSzne2382Eguj` (Lead Events) |
