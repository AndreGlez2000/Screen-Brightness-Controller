import sys
import screen_brightness_control as sbc
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QPushButton, QSlider)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class RetroMonitorControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.monitors = sbc.list_monitors()
        self.selected_monitor = self.monitors[0] if self.monitors else ""
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('◢◤ BRIGHTNESS CONTROL ◥◣')
        self.setGeometry(100, 100, 500, 450)
        
        # Retro 80's cyberpunk style
        retro_style = """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a0033, stop:0.5 #2d0052, stop:1 #1a0033);
                border: 3px solid #ff00ff;
            }
            QWidget {
                background: transparent;
                color: #00ffff;
                font-family: 'Courier New';
            }
            QLabel {
                color: #00ffff;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff00ff, stop:1 #8b00ff);
                color: #ffffff;
                border: 2px solid #00ffff;
                border-radius: 5px;
                padding: 10px;
                font-size: 12px;
                font-weight: bold;
                text-transform: uppercase;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff33ff, stop:1 #aa00ff);
                border: 2px solid #ff00ff;
                text-shadow: 0 0 10px #ffffff;
            }
            QPushButton:pressed {
                background: #6600cc;
            }
            QSlider::groove:horizontal {
                background: #2d0052;
                height: 8px;
                border: 2px solid #00ffff;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #ff00ff, stop:1 #00ffff);
                border: 2px solid #ffffff;
                width: 12px;
                height: 12px;
                margin: -5px 0;
                border-radius: 0px;
            }
            QSlider::handle:horizontal:hover {
                background: #ffff00;
            }
        """
        self.setStyleSheet(retro_style)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title with retro font
        title = QLabel('▬▬ι═══════ﺤ  MONITOR CONTROL  ﺤ═══════ι▬▬')
        title_font = QFont('Courier New', 14, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel('[ SELECT YOUR DISPLAY ]')
        subtitle_font = QFont('Courier New', 10)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        # Monitor buttons
        for monitor in self.monitors:
            btn = QPushButton(f'▸ {monitor}')
            btn.setFont(QFont('Courier New', 11, QFont.Bold))
            btn.clicked.connect(lambda checked, m=monitor: self.select_monitor(m))
            layout.addWidget(btn)
        
        # Brightness slider section
        slider_label = QLabel('[ BRIGHTNESS LEVEL ]')
        slider_label.setFont(subtitle_font)
        slider_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(slider_label)
        
        # Slider
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(1)
        self.brightness_slider.setMaximum(100)
        try:
            brightness_value = sbc.get_brightness(self.selected_monitor)
            if isinstance(brightness_value, list):
                current_brightness = brightness_value[0] if brightness_value else 50
            else:
                current_brightness = brightness_value if brightness_value else 50
        except:
            current_brightness = 50
        self.brightness_slider.setValue(int(current_brightness))
        self.brightness_slider.valueChanged.connect(self.update_brightness)
        layout.addWidget(self.brightness_slider)
        
        # Status label
        self.status_label = QLabel(f'► MONITOR: {self.selected_monitor} ◄')
        status_font = QFont('Courier New', 11, QFont.Bold)
        self.status_label.setFont(status_font)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Brightness value display
        self.value_label = QLabel(f'⚡ {int(current_brightness)}% ⚡')
        value_font = QFont('Courier New', 18, QFont.Bold)
        self.value_label.setFont(value_font)
        self.value_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.value_label)
        
        layout.addStretch()
        central_widget.setLayout(layout)
        
    def select_monitor(self, monitor):
        self.selected_monitor = monitor
        brightness_value = sbc.get_brightness(monitor)
        if isinstance(brightness_value, list):
            brightness = brightness_value[0] if brightness_value else 50
        else:
            brightness = brightness_value if brightness_value else 50
        self.brightness_slider.setValue(int(brightness))
        self.status_label.setText(f'► MONITOR: {monitor} ◄')
        self.value_label.setText(f'⚡ {int(brightness)}% ⚡')
        
    def update_brightness(self, value):
        if self.selected_monitor:
            sbc.set_brightness(value, display=self.selected_monitor)
            self.value_label.setText(f'⚡ {value}% ⚡')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RetroMonitorControl()
    window.show()
    sys.exit(app.exec_())
