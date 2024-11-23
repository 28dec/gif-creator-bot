from PIL import Image, ImageDraw, ImageFont


font_path = "./font.ttf"  # Adjust this for your system

def get_font_for_word(word, target_size):
    font = None
    max_font_size = target_size
    for font_size in range(max_font_size, 10, -2):
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise ValueError("Font file not found or inaccessible.")
        bbox = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), word, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if text_width <= target_size and text_height <= target_size:
            return font, text_width, text_height
    return font, None, None

def create_text_gif(text, output_gif_path, size=1000, bg_color=(255, 255, 255),
                    text_color=(0, 0, 0), font_size = 400, duration=500):
    words = text.split()
    frames = []

    # Create a frame for each word
    for word in words:
        img = Image.new("RGB", (size, size), color=bg_color)
        draw = ImageDraw.Draw(img)

        font, text_width, text_height = get_font_for_word(word, int(size * 0.8))

        # text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (size - text_width) // 2
        y = (size - text_height*2) // 2

        # Draw the word
        draw.text((x, y), word, fill=text_color, font=font)

        font_footer = ImageFont.truetype(font_path, size * 0.025)
        footer_color = (0, 255, 0)
        draw.text((size * 0.1, size * 0.95), text="create your own GIF like this with @gif_creator_241123_bot", fill=footer_color, font=font_footer)
        frames.append(img)

    # Save frames as an animated GIF
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:],
                   duration=duration, loop=0, optimize=True, quality=100)
    print(f"GIF saved to {output_gif_path}")
    return output_gif_path