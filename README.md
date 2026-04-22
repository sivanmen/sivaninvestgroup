# Sivan Invest Group – Landing Page & Guide Package

חבילה מוכנה לייבוא ל-WordPress + Elementor Pro לאתר **sivaninvestgroup.com**.

## מה בחבילה

1. **עמוד נחיתה** (Landing Page) – להורדת המדריך בהשארת פרטים דרך Elementor Form.
2. **עמוד מדריך** (Guide Page) – 18 פרקים עם תפריט דביק נפתח/נסגר בראש העמוד.
3. **תוכן מלא** לכל 18 הפרקים – כתוב מחדש בטון שיווקי, מכירתי, בונה אמון.
4. **קופי שיווקי** לעמוד הנחיתה – ממוקד המרה מקמפיינים של Meta ו-Google.
5. **18 בריפים לתמונות** – לייצור עצמאי במחולל תמונות AI (Midjourney / ChatGPT / Firefly).
6. **מדריך התקנה מלא בעברית** – צעד אחר צעד.

## מבנה התיקייה

```
├── README.md                         ← הקובץ הזה
├── elementor-templates/
│   ├── landing-page.json             ← ייבוא כ-Template בעמוד Elementor
│   └── guide-page.json               ← ייבוא כ-Template בעמוד Elementor
├── content/
│   ├── landing-copy.md               ← כל הטקסטים של עמוד הנחיתה
│   ├── chapters.md                   ← תוכן מלא של 18 הפרקים
│   └── brand-guidelines.md           ← פלטת צבעים, טיפוגרפיה, טון דיבור
├── images/
│   └── image-briefs.md               ← 18+ בריפים לתמונות AI
└── docs/
    ├── install-guide-he.md           ← מדריך התקנה בעברית
    ├── form-setup-he.md              ← הגדרת Elementor Form (מייל + DB)
    └── redirect-logic-he.md          ← כיצד להפנות מטופס לעמוד המדריך
```

## התחלה מהירה

1. היכנס לאתר **sivaninvestgroup.com → pages → Add New**.
2. פתח ב-Elementor → לחץ על אייקון התיקייה → **My Templates → Import**.
3. העלה את `elementor-templates/landing-page.json`.
4. חזור ועשה אותו דבר ל-`guide-page.json`.
5. קרא את `docs/install-guide-he.md` להמשך (טופס, הפניה, פיקסלים).

## הנחיה חשובה לעיצוב

כל הטקסטים הם RTL בעברית. ודא ש-WordPress מוגדר לעברית (`he_IL`) וש-Elementor Pro מותקן ופעיל. התבניות משתמשות רק ב-widgets סטנדרטיים של Elementor Pro – אין צורך בתוספים חיצוניים.
