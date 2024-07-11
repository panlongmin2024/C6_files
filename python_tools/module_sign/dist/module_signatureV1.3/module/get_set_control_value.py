from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QComboBox, QDoubleSpinBox, QSpinBox


def get_control_value(ui, config_data) -> dict:
    control_values: dict = {}
    get_methods = {
        QLabel: lambda control: control.text(),
        QLineEdit: lambda control: control.text(),
        QCheckBox: lambda control: control.isChecked(),
        QComboBox: lambda control: control.currentText(),
        QDoubleSpinBox: lambda control: control.value(),
        QSpinBox: lambda control: control.value()
    }
    for control_type in get_methods:
        for control_name in config_data:
            control = ui.findChild(control_type, control_name)
            if control is not None:
                control_value = get_methods[control_type](control)
                control_values[control_name] = control_value
    return control_values


def set_control_value(ui, config_data) -> None:
    set_methods: dict = {
        QLabel: lambda control, data: control.setText(data),
        QLineEdit: lambda control, data: control.setText(data),
        QCheckBox: lambda control, data: control.setChecked(data),
        QComboBox: lambda control, data: control.setCurrentText(data),
        QDoubleSpinBox: lambda control, data: control.setValue(data),
        QSpinBox: lambda control, data: control.setValue(data)
    }
    for control_type in set_methods:
        for control_name in config_data:
            control = ui.findChild(control_type, control_name)
            if control is not None:
                set_methods[control_type](control, config_data[control_name])
