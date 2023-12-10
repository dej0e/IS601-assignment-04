from django.shortcuts import render


def calculator(request):
    subtotal = ""
    tip_percent = ""
    totals = 0
    tips = 0
    if (request.method == "POST"):
        subtotal = eval(request.POST.get("subtotal"))
        tip_percent = eval(request.POST.get("tip_percent"))
        actualTipPercentage = tip_percent * 0.01
        totals = subtotal * (1 + actualTipPercentage)
        tips = subtotal * actualTipPercentage
    return render(request, "calc.html",
                  {"total": round(totals, 2),
                   "tip": round(tips, 2)})
