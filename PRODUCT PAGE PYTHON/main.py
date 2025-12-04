import flet as flt


def main (page: flt.Page):
    page.title = 'Produto'
    page.bgcolor = '#000000'
    page.scroll = flt.ScrollMode.AUTO
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'


    def change_main_image(e):
        for elemento in option.controls:
            if elemento == e.control:
                elemento.opacity=1
                main_imagem.src = elemento.content.src
            else:
                elemento.opacity=0.5

        main_imagem.update()
        option.update()
    

    main_imagem = flt.Image(
                    src='https://files.tecnoblog.net/wp-content/uploads/2020/09/captura-de-tela-2020-09-23-as-14-33-05-700x433.png',
                )

    imagem_produto = flt.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=flt.Colors.WHITE,
        padding=flt.padding.all(30),
        height=700,
        content=flt.Column(
            expand=True,
            alignment=flt.MainAxisAlignment.CENTER,
            horizontal_alignment=flt.CrossAxisAlignment.CENTER,
            controls=[
               main_imagem := flt.Image(
                    src='https://files.tecnoblog.net/wp-content/uploads/2020/09/captura-de-tela-2020-09-23-as-14-33-05-700x433.png',
                    fit=flt.ImageFit.CONTAIN,
                    expand=True,
                    height=700,
                ),
               option := flt.Row(
                    alignment=flt.MainAxisAlignment.CENTER,
                    controls=[
                        flt.Container(
                            content=flt.Image(src='https://images.kabum.com.br/produtos/fotos/sync_mirakl/939944/xlarge/Console-Playstation-5-Slim-Digital-Edition-825GB-USB-HDMI-Branco_1762471114.png'),
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),

                        flt.Container(
                            content=flt.Image(src='https://images.kabum.com.br/produtos/fotos/640516/console-playstation-5-edicao-slim-digital-ssd-1tb-controle-sem-fio-bundle-edicao-limitada-do-30-aniversario-cinza-e-preto-1000046555_1727181034_gg.jpg'),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),

                        flt.Container(
                            content=flt.Image(src='https://m.media-amazon.com/images/I/51EIivRPFNL._AC_UF350,350_QL80_.jpg'),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )


    produto_detalhes = flt.Container(
        col={'xs': 12, 'md': 6},
        padding=flt.padding.all(30),
        bgcolor=flt.Colors.BLACK87,
        height=700,
        content=flt.Column(
            controls=[
                flt.Text(
                    value='Consoles',
                    color='blue',
                    weight=flt.FontWeight.BOLD,
                ),

                flt.Text(
                    value='PlayStation 5',
                    weight=flt.FontWeight.BOLD,
                    color=flt.Colors.WHITE,
                    size=30
                ),
                flt.Text(
                    value='Sony',
                    italic=True,
                    color=flt.Colors.GREY,
                    size=15,
                ),
                flt.ResponsiveRow(
                    vertical_alignment=flt.CrossAxisAlignment.CENTER,
                    columns=12,
                    controls=[
                        flt.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$3999',
                            color=flt.Colors.WHITE,
                            size=30
                    ),
                    flt.Row(
                        col={'xs': 12, 'sm': 6},
                        spacing=10,
                        wrap=False,
                        controls=[
                            flt.Icon(
                                name=flt.Icons.STAR,
                                color=flt.Colors.YELLOW if star < 4 else flt.Colors.WHITE,
                            ) for star in range(5)
                        ]
                    )
                    ]
                ),
                flt.Tabs(
                    selected_index=0,
                    indicator_color=flt.Colors.BLUE,
                    height=150,
                    tabs=[
                        flt.Tab(
                            text='Descrição',
                            content=flt.Container(
                                padding=flt.padding.all(10),
                                content=flt.Text(
                                    value='O PlayStation 5 entrega desempenho rápido com seu SSD ultrarrápido, gráficos em 4K, e o controle DualSense, que oferece vibrações imersivas e gatilhos adaptáveis. Um console moderno, potente e ideal para quem busca jogos com máxima qualidade e fluidez.',
                                    color=flt.Colors.GREY
                                )
                            )
                        ),
                        flt.Tab(
                            text='Detalhes',
                            content=flt.Container(
                                padding=flt.padding.all(10),
                                content=flt.Text(
                                    value='O PS5 traz carregamento super rápido com SSD, gráficos em 4K, suporte a 120 FPS e Ray Tracing. Conta com processador AMD, 16 GB de RAM e áudio 3D. O controle DualSense oferece feedback háptico e gatilhos adaptáveis, garantindo mais imersão nos jogos.',
                                    color=flt.Colors.GREY
                                )
                            )
                        )
                    ]
                ),
                flt.ResponsiveRow(
                    columns=12,
                    controls=[
                        flt.Dropdown(
                            col=6,
                            label='Cor',
                            label_style=flt.TextStyle(flt.Colors.WHITE),
                            border_color=flt.Colors.BLUE,
                            border_width=0.3,
                            options=[
                                flt.dropdown.Option(text='Branco'),
                                flt.dropdown.Option(text='Cinza'),
                                flt.dropdown.Option(text='Azul'),
                            ]
                        ),
                        flt.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=flt.TextStyle(flt.Colors.WHITE),
                            border_color=flt.Colors.BLUE,
                            border_width=0.3,
                            options=[
                                flt.dropdown.Option(text=f'{num} unid')
                                for num in range(1, 11)
                            ]
                        ),
                    ]
                ),
                flt.Container(expand=True),
                flt.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=flt.ButtonStyle(
                        padding=20,
                        bgcolor=flt.Colors.WHITE,
                        color=flt.Colors.BLACK,
                        side=flt.BorderSide(2, flt.Colors.WHITE)
                    )
                ),
                flt.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=flt.ButtonStyle(
                        padding=20,
                        bgcolor=flt.Colors.BLUE,
                        color=flt.Colors.WHITE,
                        side=flt.BorderSide(2, flt.Colors.WHITE)
                    )
                )
            ]
        )
    )


    layout = flt.Container(
        width=900,
        margin=flt.margin.all(50),
        shadow=flt.BoxShadow(blur_radius=300, color='#888888'),
        alignment=flt.alignment.center,
        content=flt.ResponsiveRow(
            run_spacing=0,
            columns=12,
            spacing=0,
            alignment=flt.MainAxisAlignment.CENTER,
            controls=[
                imagem_produto,
                produto_detalhes
            ]
        )
    )

    page.add(layout)
if __name__ == '__main__':
    flt.app(target=main)