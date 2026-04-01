from django.shortcuts import render, get_object_or_404
from .models import PromptItem, Purchase
from django.db import IntegrityError

def index(request):
    query = request.GET.get('q')
    prompts = PromptItem.objects.all()
    if query:
        prompts = prompts.filter(title__icontains=query)
    return render(request, 'index.html', {'prompts': prompts, 'query': query})

def prompt_detail(request, pk):
    item = get_object_or_404(PromptItem, pk=pk)
    unlocked = False
    if request.user.is_authenticated:
        # Yahan 'prompt' ki jagah 'prompt_item' kar diya hai
        unlocked = Purchase.objects.filter(user=request.user, prompt_item=item).exists()
    return render(request, 'prompt_detail.html', {'item': item, 'unlocked': unlocked})

def checkout(request, pk):
    item = get_object_or_404(PromptItem, pk=pk)
    error = None
    if request.method == 'POST':
        utr = request.POST.get('utr_number', '').strip()
        if len(utr) != 12 or not utr.isdigit():
            error = "❌ Invalid UTR! Must be 12 digits."
        else:
            try:
                # Yahan bhi 'prompt_item' kar diya hai
                Purchase.objects.create(user=request.user, prompt_item=item, utr_number=utr)
                return render(request, 'prompt_detail.html', {'item': item, 'unlocked': True})
            except IntegrityError:
                error = "⚠️ This ID is already used. Try again."
    return render(request, 'checkout.html', {'item': item, 'error': error})

def profile_settings(request):
    return render(request, 'profile.html', {'user': request.user})
