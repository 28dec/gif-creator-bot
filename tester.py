from gif_creator import *
import uuid

output_gif_path = uuid.uuid4().hex + ".gif"
create_text_gif(text="thị trường lồn lồn lồn",
                output_gif_path=output_gif_path,
                size=1000,
                bg_color=(0, 0, 0),
                text_color=(255, 0, 0),
                font_size=150,
                duration=175
                )
