"""
Elementor Data Generator for Sivan Invest Group
Builds JSON payload for the _elementor_data post meta.

Brand palette (extracted from live site globals):
  Primary Blue: #0038B8
  Deep Navy:    #111F2A
  Gold Accent:  #BD9132
  Soft Tan:     #C6B18B
  Light BG:     #E8EFFD
  White:        #FFFFFF
  Ink:          #1A1A1A
"""
import json
import secrets


def eid():
    """Elementor-style 7 hex id."""
    return secrets.token_hex(4)[:7]


# ---------- palette ----------
PRIMARY = "#0038B8"
NAVY = "#111F2A"
GOLD = "#BD9132"
TAN = "#C6B18B"
LIGHT = "#E8EFFD"
WHITE = "#FFFFFF"
INK = "#1A1A1A"
SUBTLE = "#6B7280"

LOGO_URL = "https://sivaninvestgroup.com/wp-content/uploads/2025/07/SivanInvest-960-x-160-px.png"
WHATSAPP_URL = "https://wa.me/972559210057?text=%D7%94%D7%99%D7%99%20%D7%A8%D7%95%D7%A6%D7%94%20%D7%9C%D7%A9%D7%9E%D7%95%D7%A2%20%D7%A2%D7%95%D7%93%20%D7%A2%D7%9C%20%D7%94%D7%A9%D7%A7%D7%A2%D7%95%D7%AA%20%D7%91%D7%99%D7%95%D7%95%D7%9F"
FORM_ANCHOR = "download-form"
GUIDE_URL = "/guide"


# =========================================================================
# BUILDING BLOCKS
# =========================================================================

def heading(text, tag="h2", color=NAVY, size="xl", align="center", weight="800"):
    """Heading widget."""
    size_map = {
        "xxl": {"size": "60", "line_height": "1.1"},
        "xl": {"size": "44", "line_height": "1.15"},
        "lg": {"size": "32", "line_height": "1.25"},
        "md": {"size": "24", "line_height": "1.35"},
        "sm": {"size": "18", "line_height": "1.4"},
    }
    mobile_size = {"xxl": "34", "xl": "28", "lg": "24", "md": "20", "sm": "16"}[size]
    s = size_map[size]
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "heading",
        "settings": {
            "title": text,
            "header_size": tag,
            "align": align,
            "title_color": color,
            "typography_typography": "custom",
            "typography_font_family": "Heebo",
            "typography_font_weight": weight,
            "typography_font_size": {"unit": "px", "size": int(s["size"])},
            "typography_font_size_mobile": {"unit": "px", "size": int(mobile_size)},
            "typography_line_height": {"unit": "em", "size": float(s["line_height"])},
            "typography_letter_spacing": {"unit": "px", "size": -0.5},
        },
        "elements": [],
    }


def text(html, color=INK, size=16, align="right", max_width=None, weight="400"):
    """Text editor widget."""
    s = {
        "editor": html if html.startswith("<") else f"<p>{html}</p>",
        "align": align,
        "text_color": color,
        "typography_typography": "custom",
        "typography_font_family": "Assistant",
        "typography_font_weight": weight,
        "typography_font_size": {"unit": "px", "size": size},
        "typography_line_height": {"unit": "em", "size": 1.7},
    }
    if max_width:
        s["_element_custom_width"] = {"unit": "px", "size": max_width}
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "text-editor",
        "settings": s,
        "elements": [],
    }


def button(label, link, variant="primary", size="lg", align="center", icon=None, css_id=None):
    """Button widget. variant: primary|secondary|outline|whatsapp"""
    if variant == "primary":
        bg, bg_hover, txt_color, border = GOLD, NAVY, WHITE, GOLD
    elif variant == "secondary":
        bg, bg_hover, txt_color, border = NAVY, GOLD, WHITE, NAVY
    elif variant == "whatsapp":
        bg, bg_hover, txt_color, border = "#25D366", "#128C7E", WHITE, "#25D366"
    else:  # outline
        bg, bg_hover, txt_color, border = "transparent", GOLD, NAVY, NAVY

    font_size = {"lg": 18, "md": 16, "sm": 14}[size]
    pad_v = {"lg": 18, "md": 14, "sm": 10}[size]
    pad_h = {"lg": 36, "md": 28, "sm": 20}[size]

    settings = {
        "text": label,
        "link": {"url": link, "is_external": "", "nofollow": ""},
        "align": align,
        "size": "sm",
        "background_color": bg,
        "button_text_color": txt_color,
        "hover_color": txt_color,
        "button_background_hover_color": bg_hover,
        "border_radius": {"unit": "px", "top": "999", "right": "999", "bottom": "999", "left": "999", "isLinked": True},
        "text_padding": {"unit": "px", "top": str(pad_v), "right": str(pad_h), "bottom": str(pad_v), "left": str(pad_h), "isLinked": False},
        "typography_typography": "custom",
        "typography_font_family": "Heebo",
        "typography_font_weight": "700",
        "typography_font_size": {"unit": "px", "size": font_size},
        "button_box_shadow_box_shadow_type": "yes",
        "button_box_shadow_box_shadow": {"horizontal": 0, "vertical": 12, "blur": 32, "spread": 0, "color": "rgba(11,42,74,0.18)"},
        "hover_animation": "grow",
    }
    if icon:
        settings["selected_icon"] = {"value": icon, "library": "fa-brands" if icon.startswith("fab-") else "fa-solid"}
        settings["icon_align"] = "right"
    if css_id:
        settings["_element_id"] = css_id

    if variant == "whatsapp" and link.startswith("http"):
        settings["link"]["is_external"] = "on"

    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "button",
        "settings": settings,
        "elements": [],
    }


def image(url, width=None, height=None, align="center", border_radius=12, css_classes=None):
    s = {
        "image": {"url": url, "id": ""},
        "align": align,
        "image_border_radius": {"unit": "px", "top": str(border_radius), "right": str(border_radius), "bottom": str(border_radius), "left": str(border_radius), "isLinked": True},
    }
    if width:
        s["width"] = {"unit": "px", "size": width}
    if css_classes:
        s["_css_classes"] = css_classes
    return {"id": eid(), "elType": "widget", "widgetType": "image", "settings": s, "elements": []}


def spacer(h=40, h_mobile=24):
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "spacer",
        "settings": {
            "space": {"unit": "px", "size": h},
            "space_mobile": {"unit": "px", "size": h_mobile},
        },
        "elements": [],
    }


def divider(color=TAN, weight=2, gap=30):
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "divider",
        "settings": {
            "color": color,
            "weight": {"unit": "px", "size": weight},
            "gap": {"unit": "px", "size": gap},
            "width": {"unit": "px", "size": 80},
            "align": "center",
        },
        "elements": [],
    }


def icon_list(items, color=PRIMARY, icon_color=GOLD, text_color=INK, size=17, align="right"):
    """items: list of dicts {text, icon, link?}"""
    li = []
    for it in items:
        entry = {
            "text": it["text"],
            "selected_icon": {"value": it.get("icon", "fas fa-check-circle"), "library": "fa-solid"},
            "_id": eid(),
        }
        if it.get("link"):
            entry["link"] = {"url": it["link"], "is_external": "", "nofollow": ""}
        li.append(entry)
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "icon-list",
        "settings": {
            "icon_list": li,
            "space_between": {"unit": "px", "size": 14},
            "icon_color": icon_color,
            "text_color": text_color,
            "icon_size": {"unit": "px", "size": 20},
            "typography_typography": "custom",
            "typography_font_family": "Assistant",
            "typography_font_weight": "500",
            "typography_font_size": {"unit": "px", "size": size},
            "align": align,
        },
        "elements": [],
    }


def stat_card(number, label, sublabel=""):
    return column(
        [
            heading(number, tag="div", color=GOLD, size="xxl", align="center", weight="900"),
            heading(label, tag="h4", color=NAVY, size="md", align="center"),
            text(f"<p style='text-align:center'>{sublabel}</p>", color=SUBTLE, size=14, align="center") if sublabel else spacer(4),
        ],
        col_size=25,
        bg=WHITE,
        padding=(32, 20, 32, 20),
        border_radius=16,
        box_shadow="0 4px 24px rgba(11,42,74,0.08)",
    )


def chapter_card(num, icon, title, desc, anchor):
    """Teaser card for a chapter on the landing page."""
    return column(
        [
            heading(f"פרק {num:02d}", tag="div", color=GOLD, size="sm", align="right", weight="700"),
            heading(title, tag="h3", color=NAVY, size="md", align="right", weight="700"),
            text(f"<p>{desc}</p>", color=INK, size=15, align="right"),
        ],
        col_size=33,
        bg=LIGHT,
        padding=(28, 28, 28, 28),
        border_radius=16,
    )


def column(widgets, col_size=100, bg=None, padding=None, border_radius=0, box_shadow=None, vertical_align=None, inner_margin=None):
    """Column with inner widgets."""
    settings = {"_column_size": col_size, "_inline_size": None}
    if bg:
        settings["background_background"] = "classic"
        settings["background_color"] = bg
    if padding:
        t, r, b, l = padding
        settings["padding"] = {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}
    if border_radius:
        settings["border_radius"] = {"unit": "px", "top": str(border_radius), "right": str(border_radius), "bottom": str(border_radius), "left": str(border_radius), "isLinked": True}
    if box_shadow:
        settings["box_shadow_box_shadow_type"] = "yes"
        settings["box_shadow_box_shadow"] = {"horizontal": 0, "vertical": 4, "blur": 24, "spread": 0, "color": "rgba(11,42,74,0.08)"}
    if vertical_align:
        settings["content_position"] = vertical_align
    if inner_margin:
        t, r, b, l = inner_margin
        settings["margin"] = {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}
    return {
        "id": eid(),
        "elType": "column",
        "settings": settings,
        "elements": widgets,
        "isInner": False,
    }


def section(columns, bg=None, bg_image=None, padding=(100, 20, 100, 20), padding_mobile=(60, 16, 60, 16),
            structure=None, css_id=None, overlay=False, sticky=None, container_width=1140):
    """Outer section."""
    if structure is None:
        structure = {1: "10", 2: "20", 3: "30", 4: "40"}.get(len(columns), "10")

    s = {
        "structure": structure,
        "padding": {"unit": "px", "top": str(padding[0]), "right": str(padding[1]), "bottom": str(padding[2]), "left": str(padding[3]), "isLinked": False},
        "padding_mobile": {"unit": "px", "top": str(padding_mobile[0]), "right": str(padding_mobile[1]), "bottom": str(padding_mobile[2]), "left": str(padding_mobile[3]), "isLinked": False},
        "content_width": {"unit": "px", "size": container_width},
        "gap": "default",
    }
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if bg_image:
        s["background_background"] = "classic"
        s["background_image"] = {"url": bg_image, "id": ""}
        s["background_position"] = "center center"
        s["background_size"] = "cover"
    if overlay:
        s["background_overlay_background"] = "classic"
        s["background_overlay_color"] = "rgba(17,31,42,0.6)"
    if css_id:
        s["_element_id"] = css_id
    if sticky:
        s["sticky"] = sticky
        s["sticky_on"] = ["desktop", "tablet", "mobile"]
        s["sticky_effects_offset"] = 0
        s["z_index"] = 9999
    return {
        "id": eid(),
        "elType": "section",
        "settings": s,
        "elements": columns,
        "isInner": False,
    }


def inner_section(columns, bg=None, padding=(0, 0, 0, 0), gap="extended"):
    s = {
        "structure": {1: "10", 2: "20", 3: "30", 4: "40"}.get(len(columns), "10"),
        "padding": {"unit": "px", "top": str(padding[0]), "right": str(padding[1]), "bottom": str(padding[2]), "left": str(padding[3]), "isLinked": False},
        "gap": gap,
    }
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    return {
        "id": eid(),
        "elType": "section",
        "settings": s,
        "elements": columns,
        "isInner": True,
    }


# =========================================================================
# HEADER (shared, minimal: logo + CTA button, no main menu)
# =========================================================================

def minimal_header(cta_label="הורדת המדריך", cta_link=f"#{FORM_ANCHOR}", cta_variant="primary"):
    """Top bar with logo (right side for RTL) and CTA button (left side for RTL)."""
    logo_col = column(
        [image(LOGO_URL, width=160, align="right", border_radius=0)],
        col_size=50,
        padding=(8, 0, 8, 0),
        vertical_align="middle",
    )
    btn_col = column(
        [button(cta_label, cta_link, variant=cta_variant, size="sm", align="left")],
        col_size=50,
        padding=(8, 0, 8, 0),
        vertical_align="middle",
    )
    return section(
        [logo_col, btn_col],
        bg=WHITE,
        padding=(12, 24, 12, 24),
        padding_mobile=(10, 16, 10, 16),
        structure="20",
        sticky="top",
        container_width=1280,
    )


# =========================================================================
# FOOTER (minimal)
# =========================================================================

def minimal_footer():
    logo = column(
        [
            image(LOGO_URL, width=140, align="center", border_radius=0),
            spacer(16),
            text(
                "<p style='text-align:center'>Sivan Invest Group — בית להשקעות, נדל״ן ופיננסים | "
                "<a href='mailto:support@sivaninvest.co.il' style='color:#C6B18B'>support@sivaninvest.co.il</a> | "
                "<a href='tel:+972559210057' style='color:#C6B18B'>055-921-0057</a></p>",
                color="#B7C2CE", size=14, align="center"),
            spacer(8),
            text(
                "<p style='text-align:center;font-size:12px;color:#7A8592'>"
                "© 2026 Sivan Invest Group. כל הזכויות שמורות. המידע אינו מהווה ייעוץ השקעות או המלצה לרכישת נכס. "
                "<a href='/privacy-policy-terms-of-use/' style='color:#C6B18B'>מדיניות פרטיות</a></p>",
                color="#7A8592", size=12, align="center"),
        ],
        col_size=100,
    )
    return section([logo], bg=NAVY, padding=(48, 20, 36, 20), padding_mobile=(40, 16, 28, 16))


# =========================================================================
# FORM (Elementor Pro form widget with email + DB submissions + redirect)
# =========================================================================

def elementor_form(redirect_url=GUIDE_URL, email_to="support@sivaninvest.co.il"):
    form_fields = [
        {"custom_id": "full_name", "field_type": "text", "field_label": "שם מלא", "placeholder": "ישראל ישראלי",
         "required": "true", "width": "100", "_id": eid()},
        {"custom_id": "email", "field_type": "email", "field_label": "אימייל", "placeholder": "you@example.com",
         "required": "true", "width": "50", "_id": eid()},
        {"custom_id": "phone", "field_type": "tel", "field_label": "טלפון", "placeholder": "050-0000000",
         "required": "true", "width": "50", "_id": eid()},
        {"custom_id": "area", "field_type": "select", "field_label": "אזור התעניינות",
         "field_options": "סלוניקי\nאתונה\nשניהם\nעדיין לא בטוח",
         "required": "true", "width": "50", "_id": eid()},
        {"custom_id": "budget", "field_type": "select", "field_label": "תקציב משוער (€)",
         "field_options": "עד 150,000\n150,000 - 300,000\n300,000 - 500,000\nמעל 500,000",
         "required": "true", "width": "50", "_id": eid()},
        {"custom_id": "consent", "field_type": "acceptance", "field_label": "אני מאשר/ת קבלת תכנים שיווקיים ועדכונים במייל",
         "acceptance_text": "אני מאשר/ת קבלת תכנים שיווקיים ועדכונים במייל",
         "required": "false", "width": "100", "_id": eid()},
    ]
    return {
        "id": eid(),
        "elType": "widget",
        "widgetType": "form",
        "settings": {
            "form_name": "הורדת מדריך השקעות ביוון",
            "form_fields": form_fields,
            "button_text": "שלחו לי את המדריך",
            "button_size": "sm",
            "button_align": "stretch",
            "submit_actions": ["email", "redirect"],
            "redirect_to": redirect_url,
            "email_to": email_to,
            "email_subject": "[ליד חדש] מדריך השקעות ביוון — [field id=\"full_name\"]",
            "email_content": 'שם: [field id="full_name"]\nאימייל: [field id="email"]\nטלפון: [field id="phone"]\nאזור: [field id="area"]\nתקציב: [field id="budget"]\nהסכמה לשיווק: [field id="consent"]',
            "email_from_name": "SivanInvest Group - Landing",
            "email_from": "noreply@sivaninvestgroup.com",
            "email_reply_to": "[field id=\"email\"]",
            "success_message": "מצוין! מעבירים אותך למדריך. המייל בדרך ✓",
            "error_message": "משהו השתבש. נסו שוב או צרו קשר בוואטסאפ.",
            "required_field_message": "שדה חובה",
            "button_css_id": "form-submit-btn",
            "field_typography_typography": "custom",
            "field_typography_font_family": "Assistant",
            "field_typography_font_size": {"unit": "px", "size": 16},
            "label_typography_typography": "custom",
            "label_typography_font_family": "Heebo",
            "label_typography_font_weight": "600",
            "label_typography_font_size": {"unit": "px", "size": 15},
            "field_border_color": "#D9DEE5",
            "field_border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
            "field_border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
            "field_background_color": WHITE,
            "label_color": NAVY,
            "button_background_color": GOLD,
            "button_background_color_hover": NAVY,
            "button_text_color": WHITE,
            "button_typography_typography": "custom",
            "button_typography_font_family": "Heebo",
            "button_typography_font_weight": "700",
            "button_typography_font_size": {"unit": "px", "size": 18},
            "button_border_radius": {"unit": "px", "top": "999", "right": "999", "bottom": "999", "left": "999", "isLinked": True},
        },
        "elements": [],
    }


# =========================================================================
# UTILITIES
# =========================================================================

def build_json(elements):
    """Return the _elementor_data string."""
    return json.dumps(elements, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    # quick self-test
    h = heading("בדיקה", "h1", size="xxl")
    print(json.dumps(h, ensure_ascii=False, indent=2)[:200])
