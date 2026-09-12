# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window

Window.size = (400, 800)

class FloatingActionButton(Button):
    def __init__(self, icon_text='✚', **kwargs):
        super(FloatingActionButton, self).__init__(**kwargs)
        self.icon_text = icon_text
        self.text = icon_text
        self.size_hint = (None, None)
        self.size = (64, 64)
        self.color_normal = [0.2, 0.6, 1.0, 1]
        self.color_active = [0.1, 0.5, 0.9, 1]
        self.background_color = self.color_normal
        self.drag_event = None
        self.long_press_threshold = 0.5
        self.is_dragging = False
        self.bind(on_touch_down=self.on_touch_down)
        self.bind(on_touch_move=self.on_touch_move)
        self.bind(on_touch_up=self.on_touch_up)
    
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        touch.grab(self)
        self.background_color = self.color_active
        self.drag_event = Clock.schedule_once(
            lambda dt: self.on_long_press(),
            self.long_press_threshold
        )
        return True
    
    def on_touch_move(self, touch):
        if touch.grab_current is not self:
            return False
        if self.is_dragging:
            self.center_x = touch.x
            self.center_y = touch.y
            return True
        return False
    
    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            return False
        touch.ungrab(self)
        if self.drag_event:
            self.drag_event.cancel()
        self.is_dragging = False
        self.background_color = self.color_normal
        return True
    
    def on_long_press(self):
        self.is_dragging = True
        self.background_color = self.color_active
        anim = Animation(size=(70, 70), duration=0.1)
        anim.start(self)

class DraggableBoxWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(DraggableBoxWidget, self).__init__(**kwargs)
        self.canvas.clear()
        from kivy.graphics import Color, Rectangle
        with self.canvas.before:
            Color(0.95, 0.95, 0.97, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.main_fab = FloatingActionButton(icon_text='✚')
        self.main_fab.pos_hint = {'right': 0.95, 'top': 0.95}
        self.add_widget(self.main_fab)
        
        self.secondary_fab1 = FloatingActionButton(icon_text='✎')
        self.secondary_fab1.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        self.add_widget(self.secondary_fab1)
        
        self.secondary_fab2 = FloatingActionButton(icon_text='⚙')
        self.secondary_fab2.pos_hint = {'left': 0.05, 'top': 0.95}
        self.add_widget(self.secondary_fab2)
        
        self.main_fab.bind(on_press=self.on_fab_press)
        self.secondary_fab1.bind(on_press=self.on_secondary_fab_press)
        self.secondary_fab2.bind(on_press=self.on_settings_press)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def on_fab_press(self, instance):
        if not instance.is_dragging:
            self.show_popup("Main Action", "Main floating button pressed!")
    
    def on_secondary_fab_press(self, instance):
        if not instance.is_dragging:
            self.show_popup("Secondary Action", "Secondary button pressed!")
    
    def on_settings_press(self, instance):
        if not instance.is_dragging:
            self.show_popup("Settings", "Settings button pressed!")
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint_y=0.7, text_size=(self.width - 40, None))
        content.add_widget(label)
        close_btn = Button(text='Close', size_hint_y=0.3)
        content.add_widget(close_btn)
        popup = Popup(title=title, content=content, size_hint=(0.9, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

class FloatingButtonApp(App):
    def build(self):
        self.title = "Floating Button App"
        return DraggableBoxWidget()

if __name__ == '__main__':
    FloatingButtonApp().run()
