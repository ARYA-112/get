from django.shortcuts import render

def index(request): return render(request, "decoder/index.html", {"title": "BCD to Decimal Decoder"})
def aim(request): return render(request, "decoder/aim.html", {"title": "Aim"})
def theory(request): return render(request, "decoder/theory.html", {"title": "Theory"})
def procedure(request): return render(request, "decoder/procedure.html", {"title": "Procedure"})
def simulation(request): return render(request, "decoder/simulation.html", {"title": "Simulation"})
def posttest(request): return render(request, "decoder/posttest.html", {"title": "Post Test"})
def references(request): return render(request, "decoder/references.html", {"title": "References"})

def pretest(request): return render(request, "decoder/pretest.html", {"title": "pretest"})
