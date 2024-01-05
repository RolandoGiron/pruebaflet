import flet as ft
import time 

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

    def button_clicked(e):
        page.add(ft.Text("Botoniado!"))


    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ]))
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!" , on_click=button_clicked)
    ])
    )   



    #for i in range(10):
    ##    page.controls.append(ft.Text(f"Line {i}"))
     #   if i > 4:
     #       page.controls.pop(0)
     #   page.update()
     #   time.sleep(0.3)


ft.app(target=main, view=ft.AppView.WEB_BROWSER,port=8550)