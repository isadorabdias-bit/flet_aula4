import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("Gato."))

    page.add(
        ft.Text(
            "Bem-Vindo ao app Indoor Animal",
            size=24,
            color= "blue",
            weight=ft.FontWeight.W_600
        ),

        ft.Image(
            src="images/gato.jpg",
            height=200
        ),
        ft.Button(
            content="Clique aqui",
            # on_click é pra quando clicar em clique aq vai aparecer uma mensagem
            on_click = mostrar_mensagem
        )
    )

ft.app(main)