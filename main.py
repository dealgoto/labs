from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class ScreenVideo(Screen):
    def __init__(self, **kwargs):
        super(ScreenVideo, self).__init__(**kwargs)
        self.vid = None

    def test_on_enter(self, media_name):
        if media_name.endswith('.mp4'):
            self.vid = VideoPlayer(source=media_name, state='play',
                                   options={'allow_stretch': False,
                                            'eos': 'loop'})
            self.add_widget(self.vid)

    def on_leave(self):
        if self.vid:
            self.vid.state = 'stop'
            self.remove_widget(self.vid)

    def onBackBtn(self):
        self.on_leave()
        self.manager.current = self.manager.list_of_prev_screens.pop()

class ScreenAudio(Screen):
    def __init__(self, **kwargs):
        super(ScreenAudio, self).__init__(**kwargs)
        self.sound = None
        self.audio_button = Button(text="Відтворити аудіо", on_release=self.toggle_audio)
        self.add_widget(self.audio_button)

    def test_on_enter(self, media_name):
        if media_name.endswith('.mp3'):
            self.sound = SoundLoader.load(media_name)

    def toggle_audio(self, *args):
        if self.sound:
            if self.sound.state == 'play':
                self.sound.stop()
                self.audio_button.text = "Відтворити аудіо"
            else:
                self.sound.play()
                self.audio_button.text = "Зупинити аудіо"

    def on_leave(self):
        if self.sound:
            self.sound.stop()

    def onBackBtn(self):
        self.on_leave()
        self.manager.current = self.manager.list_of_prev_screens.pop()

class ScreenOne(Screen):
    def onNextScreen(self, btn, fileName):
        self.manager.list_of_prev_screens.append(btn.parent.name)
        if fileName == 'audio':
            self.manager.current = 'screen_audio'
            self.manager.screen_audio.test_on_enter('Resources/Videos/' + fileName + '.mp3')
        else:
            self.manager.current = 'screen_video'
            self.manager.screen_video.test_on_enter('Resources/Videos/' + fileName + '.mp4')

class Manager(ScreenManager):
    transition = NoTransition()
    screen_one = ObjectProperty(None)
    screen_video = ObjectProperty(None)
    screen_audio = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.list_of_prev_screens = []

class ScreensApp(App):
    def build(self):
        self.title = "Kivy лабораторна робота" 
        return Manager()

if __name__ == "__main__":
    ScreensApp().run()"# �� ��?�� � feature-1" 
