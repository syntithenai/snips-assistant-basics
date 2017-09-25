  - url: ../snips_skill_usb_power
    package_name: usbpowerskill
    class_name: UsbPowerSkill
    requires_tts: True
    intents:
      - intent: UsbPowerOnPort
        action: |
          {%
          skill.usb_power_on_say(intent.usbPortIdentifier,skill.usb_load_devices(skill.usb_get_devices()))
          %}
      - intent: UsbPowerOffPort
        action: |
          {%
          skill.usb_power_off_say(intent.usbPortIdentifier,skill.usb_load_devices(skill.usb_get_devices()))
          %}
      - intent: UsbListPorts
        action: |
          {%
          skill.usb_list_devices_say(skill.usb_load_devices(skill.usb_get_devices()))
          %}
