from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from plyer import notification
import time

class WaterReminderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Create a toggle button
        self.toggle_button = ToggleButton(text='Reminder OFF', group='reminder', on_press=self.toggle_reminder)
        self.layout.add_widget(self.toggle_button)
        
        return self.layout

    def toggle_reminder(self, instance):
        if self.toggle_button.state == 'down':
            self.start_reminder()
        else:
            self.stop_reminder()

    def start_reminder(self):
        self.toggle_button.text = 'Reminder ON'
        self.schedule_reminder()

    def stop_reminder(self):
        self.toggle_button.text = 'Reminder OFF'
        Clock.unschedule(self.reminder)

    def reminder(self, dt):
        notification.notify(title="Please drink water now!",
                            message="Hey user! This is Anushree's reminder assistant.Drink your way to better health. Drink water!",
                            timeout=5)

    def schedule_reminder(self):
        # Schedule the reminder to occur every hour
        Clock.schedule_interval(self.reminder, 90*60)

if __name__ == '__main__':
    WaterReminderApp().run()