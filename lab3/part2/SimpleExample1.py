import toga
from toga.constants import COLUMN
from toga.style import Pack
from toga import validators
import packages
from packages import proton, electron, neitron
class TextInputApp(toga.App):
    def do_extract_values(self, widget, **kwargs):
        self.text_electp_input.enabled = False
        self.text_electm_input.enabled = False
        self.text_electc_input.enabled = False
        self.text_protonp_input.enabled = False
        self.text_protonm_input.enabled = False
        self.text_protonc_input.enabled = False
        self.text_neitronp_input.enabled = False
        self.text_neitronm_input.enabled = False
        self.text_neitronc_input.enabled = False
        m = float(self.text_electm_input.value)
        c = float(self.text_electc_input.value)
        p = float(self.text_electp_input.value)
        self.text_label_el.text = "Рассчитанная комтоновская длина волны для электрона: {}".format(packages.electron.elec(p, m , c))
        m = float(self.text_protonm_input.value)
        c = float(self.text_protonc_input.value)
        p = float(self.text_protonp_input.value)
        self.text_label_pr.text = "Рассчитанная комтоновская длина волны для протона: {}".format(packages.proton.prot(p, m , c))
        m = float(self.text_neitronm_input.value)
        c = float(self.text_neitronc_input.value)
        p = float(self.text_neitronp_input.value)
        self.text_label_nt.text = "Рассчитанная комтоновская длина волны для нейтрона: {}".format(packages.neitron.neitr(p, m , c))

        self.label_el.text = 'Counting down from 5...'
        yield 1
        self.label_el.text = 'Counting down from 4...'
        yield 1
        self.label_el.text = 'Counting down from 3...'
        yield 1
        self.label_el.text = 'Counting down from 2...'
        yield 1
        self.label_el.text = 'Counting down from 1...'
        yield 1
        self.label_el.text = 'Enter some values and press extract.'

        # Renable the inputs again.
        self.text_electm_input.enabled = True
        self.text_electp_input.enabled = True
        self.text_electc_input.enabled = True
        self.text_protonp_input.enabled = True
        self.text_protonm_input.enabled = True
        self.text_protonc_input.enabled = True
        self.text_neitronp_input.enabled = True
        self.text_neitronm_input.enabled = True
        self.text_neitronc_input.enabled = True
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)
        self.label_el = toga.Label(
            'Расчет комтоновской волны для электрона', style=Pack(padding=10)
        )
        self.text_label_el = toga.Label('Ready.', style=Pack(padding=10))
        self.text_label_pr = toga.Label('Ready.', style=Pack(padding=10))
        self.text_label_nt = toga.Label('Ready.', style=Pack(padding=10))
        self.text_electp_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Постоянная планка электрона')
        self.text_electm_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Масса электрона')
        self.text_electc_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Скорость света')
        self.label_pr = toga.Label(
            'Расчет комтоновской волны для протона', style=Pack(padding=10)
        )
        self.text_protonp_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Постоянная планка протона')
        self.text_protonm_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Масса протона')
        self.text_protonc_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Скорость света')
        self.label_nt = toga.Label(
            'Расчет комтоновской волны для нейтрона', style=Pack(padding=10)
        )
        self.text_neitronp_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Постоянная планка нейтрона')
        self.text_neitronc_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Скорость света')
        self.text_neitronm_input = toga.TextInput(style=Pack(padding=10), placeholder = 'Масса нейтрона')
        btn_extract = toga.Button(
            'Nazhmi',
            on_press=self.do_extract_values,
            style=Pack(flex=1),
        )

        box = toga.Box(
            children=[
                self.label_el,
                self.text_electm_input,
                self.text_electp_input,
                self.text_electc_input,
                self.label_pr,
                self.text_protonm_input,
                self.text_protonp_input,
                self.text_protonc_input,
                self.label_nt,
                self.text_neitronm_input,
                self.text_neitronp_input,
                self.text_neitronc_input,
                self.text_label_el,
                self.text_label_pr,
                self.text_label_nt,
                btn_extract,
            ],
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding=10,
            )
        )

        self.main_window.content = box
        self.main_window.show()
def main():
    return TextInputApp('Расчёт удельного заряда коптоновской длины волны', 'org.beeware.widgets.textinput')


if __name__ == '__main__':
    app = main()
    app.main_loop()
