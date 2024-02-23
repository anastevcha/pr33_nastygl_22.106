from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.animation import Animation

class Animazia(Widget):
    def animate(self, instance):
        anim = Animation(x=100, y=100) + Animation(x=0, y=0)
        anim.start(self)

class Knopka(App):
    def build(self):
        animazia = Animazia()
        button = Button(text='Анимация')
        button.bind(on_press=animazia.animate)
        animazia.add_widget(button)
        return animazia

if __name__ == '__main__':
    Knopka().run()
