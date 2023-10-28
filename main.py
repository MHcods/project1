from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pandas as pd
from kivy.clock import Clock



df = pd.read_excel("###BANCO PAI###.xlsx")


class Aplicativo_ferreira(App):
    def build(self):
        return Builder.load_file("tela.kv")

    def update_codigo(self):

        codigo = self.root.ids.cod_barra_input.text
        produtos = self.root.ids.products
        try:
            codigo = int(codigo)

            if codigo in df["Cod. Barra"].values:

                produto = df[df['Cod. Barra'] == codigo].iloc[0]
                descrição = produto["Descrição  do produto"]
                Fornecedor = produto["idempresa"]
                discarte = produto["discarte"]
                tipo_avaria = produto["tipo de avaria"]
                pagamento_nf = produto["forma de pg. Da nf"]

                detalhes = BoxLayout(orientation='vertical', size_hint_y=None, width=500, height=470, pos_hint={'top': 1}, spacing=40)
                produtos.add_widget(detalhes)

                codigo_label = Label(text=str(codigo), size_hint_x=0.1, size_hint_y=None, height=80, color=(1, 1, 1, 1))
                name_label = Label(text=descrição, size_hint_x=0.1, size_hint_y=None, height=40, color=(1, 1, 1, 1))
                Fornecedor_label = Label(text=Fornecedor, size_hint_x=0.1, size_hint_y=None, height=40, color=(1, 1, 1, 1))
                discarte_label = Label(text=discarte, size_hint_x=0.1, size_hint_y=None, height=40, color=(1, 1, 1, 1))
                tipo_avaria_label = Label(text=tipo_avaria, size_hint_x=0.1, size_hint_y=None, height=40, color=(1, 1, 1, 1))
                pagamento_nf_label = Label(text=pagamento_nf, size_hint_x=0.1, size_hint_y=None, height=40, color=(1, 1, 1, 1))

                detalhes.add_widget(codigo_label)
                detalhes.add_widget(name_label)
                detalhes.add_widget(Fornecedor_label)
                detalhes.add_widget(discarte_label)
                detalhes.add_widget(tipo_avaria_label)
                detalhes.add_widget(pagamento_nf_label)

                self.root.ids.cod_barra_input.select_all()
                Clock.schedule_once(lambda dt: self.select_bar(), 0.1)

                Clock.schedule_once(lambda dt: self.select_text_input(), 0.1)



            else:
                print("discarte de avaria")
        except ValueError:
            print('valor inválido')
    def select_text_input(self):
        # Função para selecionar o texto no TextInput
        self.root.ids.cod_barra_input.select_all()
    def select_bar(self):
        self.root.ids.cod_barra_input.focus = True



Aplicativo = Aplicativo_ferreira()
Aplicativo.run()