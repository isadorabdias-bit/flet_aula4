import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(
            "Bem-Vinda ao meu app !",
            size=24,
            weight=ft.FontWeight.W_600,
            color="red"
        ),
        ft.Text("Eu me chamo Isadora"),
        ft.Button(
            content="Botão ativado"
        ),
        ft.Button(
            content="Botão desativado",
            disabled=True
        ),
        ft.Button(
            content="Botão colorido",
            bgcolor="blue",
            color="white"
        ),
        ft.Image(
            src="https://www.sp.senai.br/images/senai.svg",
            width=150,
            height=150
        )
    )
    
ft.app(main)