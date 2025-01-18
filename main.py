from fasthtml.common import *
from monsterui.all import *

app, rt = fast_app(hdrs=(Theme.slate.headers(), Script(src="https://unpkg.com/tone")))


listen_now_albums = (
    ("Tone.js Hello World", "Tone.js","synth.triggerAttackRelease('C4', '8n');Tone.start();"),
    ("Roar", "Catty Perry", "synth.triggerAttackRelease('D4', '8n');"), 
    ("Feline on a Prayer", "Cat Jovi", "synth.triggerAttackRelease('E4', '8n');"),
    ("Fur Elise", "Ludwig van Beethovpurr", "synth.triggerAttackRelease('F4', '8n');"),
    ("Purrple Rain", "Prince's Cat", "synth.triggerAttackRelease('G4', '8n');")
)

alarm_sounds = (
    ("Classic", "Repeating beeps", """const synth = new Tone.Synth().toDestination();
        const loopA = new Tone.Loop((time) => {
            synth.triggerAttackRelease("C5", "16n");
        }, "4n").start(0);
     Tone.getTransport().start();"""),
    ("Good Morning", "Bright polyphonic tones", """const synth = new Tone.PolySynth(Tone.Synth).toDestination();
        const now = Tone.now();
        synth.triggerAttack("D4", now);
        synth.triggerAttack("F4", now + 0.5);
        synth.triggerAttack("A4", now + 1);
        synth.triggerAttack("C5", now + 1.5);
        synth.triggerAttack("E5", now + 2);
        synth.triggerRelease(["D4", "F4", "A4", "C5", "E5"], now + 4);"""),
    ("Birds", "Chirping birds in the morning", """// create two monophonic synths
const synthA = new Tone.FMSynth().toDestination();
const synthB = new Tone.AMSynth().toDestination();
//play a note every quarter-note
const loopA = new Tone.Loop((time) => {
	synthA.triggerAttackRelease("C2", "8n", time);
}, "4n").start(0);
//play another note every off quarter-note, by starting it "8n"
const loopB = new Tone.Loop((time) => {
	synthB.triggerAttackRelease("C4", "8n", time);
}, "4n").start("8n");
// all loops start when the Transport is started
Tone.getTransport().start();
// ramp up to 800 bpm over 10 seconds
Tone.getTransport().bpm.rampTo(800, 10);"""),
    ("Ocean", "Gentle ocean waves", """const synth = new Tone.Synth().toDestination();
        synth.triggerAttackRelease("C5", "16n");
        synth.triggerAttackRelease("G4", "8n", "+0:1");"""),
    ("Rain", "Soft raindrops", """const synth = new Tone.Synth().toDestination();
        synth.triggerAttackRelease("C5", "16n");
        synth.triggerAttackRelease("G4", "8n", "+0:1");""")
)

def MusicLi(t,hk=''): return Li(A(DivFullySpaced(t,P(hk,cls=TextFont.muted_sm))))


def Album(title,artist,scr):
    return Div(
        Div(
            UkIcon('alarm-clock', height=150, width=150,
                cls="transition-transform duration-200 hover:scale-105", 
                onmousedown=scr),
            cls="overflow-hidden rounded-md"),
        Div(cls='space-y-1')(P(title,cls=TextT.bold),P(artist,cls=TextT.muted)))

def MusicTab():
    return (
        Script('const synth = new Tone.Synth().toDestination();'),
        Div(H2("Listen Now"), cls="mt-6 space-y-1"),
                    P("Top picks for you. Updated daily.",cls=TextFont.muted_sm),
                    DividerLine(),
                    Grid(*[Album(t,a,s) for t,a,s in listen_now_albums], cls='gap-8'))

def AlarmsTab():
    return (
        Div(
            H2("Alarms"),
            P("Listen to your favorite alarm clock sounds.", cls=TextFont.muted_sm),
            cls="mt-6 space-y-1"
        ),
        DividerLine(),
        Grid(*[Album(t,a,s) for t,a,s in alarm_sounds], cls='gap-8'))

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
            Div(cls="col-span-4")(
                Div(
                    DivFullySpaced(
                        Div(
                            TabContainer(
                                Li(A('Alarms', href='#'), cls='uk-active'),
                                # Li(A('Music',    href='#')),
                                # Li(A('Podcasts', href='#')),
                                # Li(A('Live', cls='opacity-50'), cls='uk-disabled'),
                                uk_switcher='connect: #component-nav; animation: uk-animation-fade',
                                alt=True), 
                            cls="max-w-80"),
                    ),
                    Ul(
                        Li(AlarmsTab()),
                        # Li(MusicTab()),
                        # Li(podcast_tab()),
                        id="component-nav", 
                        cls="uk-switcher")
                )
            ),
            cols=5)

serve()