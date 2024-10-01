import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es: {imc:.2f}" #el .2f sirve para recorrer dos tantos
        page.update()
        
        #funcion para cerrar el cuadro del dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
            
        #validar condiciones del IMC
            if imc<18.5:
                dialog = ft.AlertDialog(
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("Actualmente estas bajo de peso"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
            )
            elif imc >=18.5 and imc < 24.9:
                dialog = ft.AlertDialog(
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("Actualmente estas bajo de peso"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
                )
            elif imc >= 25 and imc <30:
                dialog = ft.AlertDialog(
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("Tienes sobre peso"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
                )
            else:
                dialog = ft.AlertDialog(
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("Tienes obesidad"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
                )
            
    except ValueError:
    
        def cerrar_dialogo(e):
            page.dialog.open=False
            page.update()
        
            dialog=ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Debes ingresar valores numericos"),
                actions=[ft.TextButton("OK", on_click=cerrar_dialogo)]
            )

def main(page: ft.Page):
    page.title = " Calculadora de IMC"
    page.bgcolor= "grey"
    
    txtPeso=ft.TextField(label="Ingresa tu peso: ")
    txtAltura=ft.TextField(label="Ingresa tu altura: ")
    lblIMC=ft.TextField("Tu IMC es: ")

    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=22
                
                )
    
    def on_calcular_click():
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
    
    
    def limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value="Tu IMC es: "
        page.update()
    
    
    btnCalcular=ft.ElevatedButton(text="Calcular",on_click=on_calcular_click)
    btnLimpiar=ft.ElevatedButton(text="Limpiar",on_click=limpiar)
    
    page.add(
        ft.Column(
            controls=[txtPeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"), #center en mayusculas y no en minusculas es por que son diferestes codigos y nos manda error
        ft.Row(
            controls=[
                img
            ], alignment="CENTER"),
        ft.Row(controls=[
            btnCalcular,
            btnLimpiar
        ],alignment="CENTER")
    )



ft.app(target=main,view=ft.AppView.WEB_BROWSER) #nos permite llamar la aplicacion web 