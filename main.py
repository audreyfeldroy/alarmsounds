from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=Theme.slate.headers())


listen_now_albums = (("Roar", "Catty Perry"), ("Feline on a Prayer", "Cat Jovi"),("Fur Elise", "Ludwig van Beethovpurr"),("Purrple Rain", "Prince's Cat"))

def MusicLi(t,hk=''): return Li(A(DivFullySpaced(t,P(hk,cls=TextFont.muted_sm))))


def Album(title,artist):
    img_url = 'https://ucarecdn.com/e5607eaf-2b2a-43b9-ada9-330824b6afd7/music1.webp'
    return Div(
        Div(cls="overflow-hidden rounded-md")(Img(cls="transition-transform duration-200 hover:scale-105", src=img_url)),
        Div(cls='space-y-1')(P(title,cls=TextT.bold),P(artist,cls=TextT.muted)))

def MusicTab():
    return (Div(H3("Listen Now"), cls="mt-6 space-y-1"),
                    P("Top picks for you. Updated daily.",cls=TextFont.muted_sm),
                    DividerLine(),
                    Grid(*[Album(t,a) for t,a in listen_now_albums], cls='gap-8'))

def podcast_tab():
    return Div(
        Div(cls='space-y-3 mt-6')(
            H3("New Episodes"),
            P("Your favorite podcasts. Updated daily.", cls=TextFont.muted_sm)),
        Div(cls="uk-placeholder flex h-[450px] items-center justify-center rounded-md",uk_placeholder=True)(
            DivVStacked(cls="space-y-6")(
                UkIcon("microphone", 3),
                H4("No episodes added"),
                P("You have not added any podcasts. Add one below.", cls=TextFont.muted_sm),
                Button("Add Podcast", cls=ButtonT.primary))))


@rt('/')
def page():
    return Container(
            Div(cls="col-span-4 border-l border-border")(
                Div(
                    DivFullySpaced(
                        Div(
                            TabContainer(
                                Li(A('Music',    href='#'),    cls='uk-active'),
                                Li(A('Podcasts', href='#')),
                                Li(A('Live', cls='opacity-50'), cls='uk-disabled'),
                                uk_switcher='connect: #component-nav; animation: uk-animation-fade',
                                alt=True), 
                            cls="max-w-80"),
                    ),
                    Ul(
                        Li(MusicTab()),
                        Li(podcast_tab()),
                        id="component-nav", 
                        cls="uk-switcher")
                )
            ),
            cols=5)

serve()