# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock

class DraggableBoxWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(DraggableBoxWidget, self).__init__(**kwargs)
        
        # إنشاء المربع بتصميم دقيق (لون رمادي، أبعاد احترافية)
        self.btn = Button(
            text='اسحبني',
            size_hint=(None, None),
            size=(160, 110),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # الألوان: رمادي في الوضع العادي، وأزرق عند تفعيل السحب
        self.color_normal = [0.82, 0.83, 0.86, 1]
        self.color_active = [0.75, 0.85, 1.0, 1]
        self.btn.background_color = self.color_normal
        
        self.btn.bind(on_touch_down=self.on_touch_down)
        self.btn.bind(on_touch_move=self.on_touch_move)
        self.btn.bind(on_touch_up=self.on_touch_up)
        
        self.add_widget(self.btn)
        self.is_dragging = False
        self.drag_event = None

    def on_touch_down(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # ضبط عداد الضغط المطول بدقة (نصف ثانية / 500 مللي ثانية)
            self.drag_event = Clock.schedule_once(lambda dt: self.activate_drag(instance), 0.5)
            return True
        return False

    def activate_drag(self, instance):
        self.is_dragging = True
        instance.background_color = self.color_active

    def on_touch_move(self, instance, touch):
        if self.is_dragging:
            instance.center = touch.pos
            return True
        return False

    def on_touch_up(self, instance, touch):
        # إلغاء المؤقت إذا رفع المستخدم يده قبل اكتمال نصف الثاية
        if self.drag_event:
            self.drag_event.cancel()
        self.is_dragging = False
        instance.background_color = self.color_normal
        return True

class ProfessionalApp(App):
    def build(self):
        return DraggableBoxWidget()

if __name__ == '__main__':
    ProfessionalApp().run()
