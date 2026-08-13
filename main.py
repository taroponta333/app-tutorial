import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
import ffmpeg

class UFCScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(UFCScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        self.status_label = Label(
            text="【UFC - MP3プレイヤー用AMV変換器】\n上の画面から動画や音楽ファイルを選んでください",
            font_size='16sp', size_hint_y=0.15, halign='center'
        )
        self.add_widget(self.status_label)

        self.file_chooser = FileChooserIconView(size_hint_y=0.6)
        self.add_widget(self.file_chooser)

        # 変換ボタン
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        
        # ★大本命のAMV変換ボタン
        btn_amv = Button(
            text="★ MP3Player用\nAMVに変換する", 
            background_color=(0.2, 0.8, 0.2, 1), # 目立つ緑色
            on_press=self.convert_to_amv
        )
        btn_mp3 = Button(text="通常の音楽\n(MP3に変換)", on_press=self.convert_audio_auto)
        
        btn_layout.add_widget(btn_amv)
        btn_layout.add_widget(btn_mp3)
        self.add_widget(btn_layout)

    def get_selected_file(self):
        selected = self.file_chooser.selection
        if not selected:
            self.status_label.text = "エラー: ファイルが選択されていません！"
            return None
        return selected[0]

    # 🔥 革命：MP3プレイヤー専用のAMV変換処理
    def convert_to_amv(self, instance):
        input_path = self.get_selected_file()
        if not input_path: return
        
        try:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_for_player.amv"
            
            self.status_label.text = "AMV形式へ特殊変換中...\n(液晶サイズと音質を最適化しています)"
            
            # 💡 安価なプレイヤーが一番読み込める王道の基準規格にカチッと変換します
            # 画面サイズ: 160x128, フレームレート: 16fps, 音声: モノラル 22050Hz
            (
                ffmpeg
                .input(input_path)
                .output(
                    output_path,
                    vcodec='amv',
                    acodec='adpcm_ima_amv',
                    pix_fmt='yuvj420p',
                    s='160x128',      # 多くの1.8インチプレイヤーの標準サイズ
                    r='16',            # 16フレーム
                    ac='1',            # 絶対にモノラル
                    ar='22050',        # サンプリングレート
                    block_size='882'   # AMV特有の同期エラーを防ぐブロックサイズ
                )
                .run(overwrite_output=True)
            )
            
            self.status_label.text = f"【AMV変換大成功！】\nプレイヤーのMoviesフォルダに移してね:\n{os.path.basename(output_path)}"
            self.file_chooser._update_files()
        except Exception as e:
            self.status_label.text = f"AMV変換エラー:\n{str(e)}"

    def convert_audio_auto(self, instance):
        input_path = self.get_selected_file()
        if not input_path: return
        
        try:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_converted.mp3"
            self.status_label.text = "MP3に変換中..."
            ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
            self.status_label.text = f"【MP3変換成功】\n{os.path.basename(output_path)}"
            self.file_chooser._update_files()
        except Exception as e:
            self.status_label.text = f"エラー:\n{str(e)}"

class 真UFCApp(App):
    def build(self):
        return UFCScreen()

if __name__ == '__main__':
    真UFCApp().run()
