import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import plyer
import subprocess

class SMSForwarderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="SMS Forwarder")
        layout.add_widget(self.label)
        return layout

    def on_start(self):
        self.request_sms_permission()
        self.request_internet_permission()
        self.start_listening_sms()

    def request_sms_permission(self):
        plyer.sms.request_permission()

    def request_internet_permission(self):
        plyer.internet.request_permission()

    def start_listening_sms(self):
        # Simulated listening for incoming SMS
        received_sms = "remove K-233"  # Replace with actual SMS content
        if received_sms.lower() == "remove k-233":
            self.uninstall_app()

    def uninstall_app(self):
        try:
            # Use subprocess to run the uninstall command (Android only)
            subprocess.run(["pm", "uninstall", "com.example.smsforwarder"], check=True)
        except subprocess.CalledProcessError:
            # Handle any potential errors here
            pass
        finally:
            # Exit the app after attempting uninstall
            App.get_running_app().stop()

if _name_ == '_main_':
    SMSForwarderApp().run()