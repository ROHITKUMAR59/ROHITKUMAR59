from PIL import Image, ImageDraw, ImageFont

# 1. Create base canvas (1200x400 fits GitHub perfectly)
width, height = 1200, 400
background_color = (13, 17, 23)  # GitHub dark theme color
image = Image.new("RGBA", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 2. Draw modern design accents (Glow effects & minimal lines)
# Draw an ambient background circle accent
draw.ellipse([900, -50, 1250, 300], fill=(31, 111, 235, 40)) 
# Structural pipeline layout lines
draw.line([(-50, 200), (300, 200), (400, 300), (1250, 300)], fill=(48, 54, 61), width=2)
draw.ellipse([296, 196, 304, 204], fill=(88, 166, 255))
draw.ellipse([396, 296, 404, 304], fill=(46, 164, 79))

# 3. Load text configurations
try:
    # Uses system font collections, falls back to default if unavailable
    font_title = ImageFont.truetype("arialbd.ttf", 60)
    font_sub = ImageFont.truetype("arial.ttf", 22)
    font_tags = ImageFont.truetype("arialbd.ttf", 15)
    font_italic = ImageFont.truetype("ariali.ttf", 16)
except IOError:
    font_title = font_sub = font_tags = font_italic = ImageFont.load_default()

# 4. Render main text segments
draw.text((80, 110), "ROHIT KUMAR", fill=(255, 255, 255), font=font_title)
draw.text((80, 185), "SENIOR QA AUTOMATION ENGINEER & SDET", fill=(88, 166, 255), font=font_sub)

# 5. Build framework tags/capsules manually
tags = [
    {"text": "Playwright", "color": (46, 164, 79)},
    {"text": "Cypress", "color": (163, 113, 247)},
    {"text": "API Automation", "color": (88, 166, 255)},
    {"text": "AWS & CI/CD", "color": (255, 123, 114)}
]

start_x = 80
for tag in tags:
    tag_text = tag["text"]
    text_color = tag["color"]
    
    # Calculate box width dynamically
    box_width = len(tag_text) * 10 + 40
    box_height = 36
    
    # Draw background badge container
    draw.rounded_rectangle(
        [start_x, 240, start_x + box_width, 240 + box_height], 
        radius=6, 
        fill=(22, 27, 34), 
        outline=(48, 54, 61), 
        width=1
    )
    # Write container metadata text
    draw.text((start_x + 20, 248), tag_text, fill=text_color, font=font_tags)
    start_x += box_width + 15

# 6. Render final engineering philosophy statement
draw.text((80, 320), '"Engineering reliability and scalability into every stage of software delivery."', fill=(139, 148, 158), font=font_italic)

# 7. Export file output
output_path = "github-banner.png"
image.convert("RGB").save(output_path, "PNG")
print(f"Success! Banner safely exported to '{output_path}'")