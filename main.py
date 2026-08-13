import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image
import ffmpeg

class UFCScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(UFCScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        self.status_label = Label(
            text="【UFC - 万能フォーマット変換器】\n上からファイルを選び、下の変換ボタンを押してください",
            font_size='14sp', size_hint_y=0.15, halign='center'
        )
        self.add_widget(self.status_label)

        self.file_chooser = FileChooserIconView(size_hint_y=0.55)
        self.add_widget(self.file_chooser)

        # --- ボタン配置エリア（2段に分けてスッキリ並べる） ---
        btn_layout_1 = BoxLayout(size_hint_y=0.15, spacing=10)
        btn_layout_2 = BoxLayout(size_hint_y=0.15, spacing=10)
        
        # 1段目：画像系・AMV
        btn_png = Button(text="→ PNG 画像", on_press=lambda x: self.convert_image_process("PNG", ".png"))
        btn_jpg = Button(text="→ JPG 画像", on_press=lambda x: self.convert_image_process("JPEG", ".jpg"))
        btn_webp = Button(text="→ WEBP 画像", on_press=lambda x: self.convert_image_process("WEBP", ".webp"))
        btn_amv = Button(text="★ AMV 動画\n(MP3Player用)", background_color=(0.2, 0.8, 0.2, 1), on_press=self.convert_to_amv)
        
        btn_layout_1.add_widget(btn_png)
        btn_layout_1.add_widget(btn_jpg)
        btn_layout_1.add_widget(btn_webp)
        btn_layout_1.add_widget(btn_amv)

        # 2段目：動画・音声系
        btn_mp4 = Button(text="→ MP4 動画", on_press=lambda x: self.convert_media_process(".mp4"))
        btn_avi = Button(text="→ AVI 動画", on_press=lambda x: self.convert_media_process(".avi"))
        btn_mp3 = Button(text="→ MP3 音声", on_press=lambda x: self.convert_media_process(".mp3"))
        btn_ogg = Button(text="→ OGG 音声", on_press=lambda x: self.convert_media_process(".ogg"))
        
        btn_layout_2.add_widget(btn_mp4)
        btn_layout_2.add_widget(btn_avi)
        btn_layout_2.add_widget(btn_mp3)
        btn_layout_2.add_widget(btn_ogg)

        self.add_widget(btn_layout_1)
        self.add_widget(btn_layout_2)

    def get_selected_file(self):
        selected = self.file_chooser.selection
        if not selected:
            self.status_label.text = "エラー: ファイルが選択されていません！"
            return None
        return selected

    # 1. 📷 画像の変換処理 (PNG, JPG, WEBP対応 / SVGは読み込みとして対応)
    def convert_image_process(self, format_name, extension):
        input_path = self.get_selected_file()
        if not input_path: return
        try:
            self.status_label.text = "画像を変換中..."
            img = Image.open(input_path)
            if format_name == "JPEG" and img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')
            
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_converted{extension}"
            img.save(output_path, format_name)
            
            self.status_label.text = f"【画像変換成功】\n{os.path.basename(output_path)}"
            self.file_chooser._update_files()
        except Exception as e:
            self.status_label.text = f"画像変換エラー:\n{str(e)}"

    # 2. 🎬 動画・音声の変換処理 (MP4, AVI, MP3, OGG対応 / 動画から音の抽出も可能)
    def convert_media_process(self, extension):
        input_path = self.get_selected_file()
        if not input_path: return
        try:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_converted{extension}"
            
            self.status_label.text = f"{extension.upper()} へ変換中...少々お待ちください"
            ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
            
            self.status_label.text = f"【メディア変換成功】\n{os.path.basename(output_path)}"
            self.file_chooser._update_files()
        except Exception as e:
            self.status_label.text = f"変換エラー:\n{str(e)}"

    # 3. 📟 特化：MP3プレイヤー専用AMV変換
    def convert_to_amv(self, instance):
        input_path = self.get_selected_file()
        if not input_path: return
        try:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_for_player.amv"
            self.status_label.text = "AMV形式へ特殊変換中...\n(液晶サイズと音質を最適化しています)"
            
            (
                ffmpeg
                .input(input_path)
                .output(
                    output_path, vcodec='amv', acodec='adpcm_ima_amv', pix_fmt='yuvj420p',
                    s='160x128', r='16', ac='1', ar='22050', block_size='882'
                )
                .run(overwrite_output=True)
            )
            self.status_label.text = f"【AMV変換成功！】Moviesフォルダへ:\n{os.path.basename(output_path)}"
            self.file_chooser._update_files()
        except Exception as e:
            self.status_label.text = f"AMV変換エラー:\n{str(e)}"

class 真UFCApp(App):
    def build(self):
        return UFCScreen()

if __name__ == '__main__':
    真UFCApp().run()
